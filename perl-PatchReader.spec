#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam    PatchReader
Summary:	Utilities to read and manipulate patches and CVS
Summary(pl):	Narzêdzia do czytania i manipulowania patchami i CVS
Name:		perl-%{pnam}
Version:	0.9.2
Release:	0.1
License:	unknow
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/author/JKEISER/%{pnam}-%{version}.tar.gz
# Source0-md5:	c0d48aa7025426ac4da04edcccccd8b0
URL:		http://search.cpan.org/~jkeiser/PatchReader-0.9.2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities to read and manipulate patches and CVS.

%description -l pl
Narzêdzia do czytania i manipulowania patchami i CVS.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*
%{perl_vendorarch}/*
%{_mandir}/man?/*
