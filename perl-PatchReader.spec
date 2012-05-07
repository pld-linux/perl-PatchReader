#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PatchReader
Summary:	PatchReader - utilities to read and manipulate patches and CVS
Summary(pl.UTF-8):	PatchReader - narzędzia do czytania i manipulowania łatami i CVS
Name:		perl-PatchReader
Version:	0.9.6
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TM/TMANNERM/%{pdir}-%{version}.tar.gz
# Source0-md5:	bd8da2388cd5ebc99a860b6d6bfeb8ad
URL:		http://search.cpan.org/~tmannerm/PatchReader-0.9.6/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl library allows you to manipulate patches programmatically by
chaining together a variety of objects that read, manipulate, and
output patch information.

%description -l pl.UTF-8
Ten moduł Perla pozwala programowo manipulować łatami poprzez łączenie
obiektów czytających, modyfikujących i zwracających informacje o
łatach.

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
