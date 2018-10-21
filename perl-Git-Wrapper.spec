#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Git
%define		pnam	Wrapper
%include	/usr/lib/rpm/macros.perl
Summary:	Git::Wrapper - Wrap git(7) command-line interface
Name:		perl-Git-Wrapper
Version:	0.048
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Git/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8dcb01a160c400b655c0ba69f57f054f
URL:		https://metacpan.org/release/Git-Wrapper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Devel-CheckBin
%if %{with tests}
BuildRequires:	perl-File-chdir
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Git::Wrapper provides an API for git(7) that uses Perl data structures for
argument passing, instead of CLI-style --options as Git does.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL
%{perl_vendorlib}/Git/*.pm
%{perl_vendorlib}/Git/Wrapper
%{_mandir}/man3/*
