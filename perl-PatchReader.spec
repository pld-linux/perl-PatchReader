#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PatchReader
Summary:	PatchReader - utilities to read and manipulate patches and CVS
Summary(pl):	PatchReader - narz�dzia do czytania i manipulowania �atami i CVS
Name:		perl-PatchReader
Version:	0.9.5
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JK/JKEISER/%{pdir}-%{version}.tar.gz
# Source0-md5:	8aca86b807aec3c82dcb981c7730f022
URL:		http://search.cpan.org/~jkeiser/PatchReader-0.9.2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl library allows you to manipulate patches programmatically by
chaining together a variety of objects that read, manipulate, and
output patch information.

%description -l pl
Ten modu� Perla pozwala programowo manipulowa� �atami poprzez ��czenie
obiekt�w czytaj�cych, modyfikuj�cych i zwracaj�cych informacje o
�atach.

%prep
%setup -q -n %{pdir}-%{version}

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
%{perl_vendorlib}/PatchReader.pm
%{perl_vendorlib}/PatchReader
%{_mandir}/man3/*
