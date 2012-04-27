Summary:	XSB Prolog Distribution
Summary(pl.UTF-8):	Dystrybucja XSB Prologa
Name:		XSB
Version:	3.3.6
Release:	0.1
License:	LGPL v2
Group:		Development/Languages
Source0:	http://xsb.sourceforge.net/downloads/%{name}336.tar.gz
# Source0-md5:	bd43680832cbe9a33ce1a9fc21d81d83
Patch0:		%{name}-configure.patch
URL:		http://xsb.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSB Prolog Distribution - a logic programming and deductive database
system.

%description -l pl.UTF-8
Dystrybucja XSB Prologa - system programowania w logice oraz
dedukcyjnych baz danych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
installdir=$(pwd)/install
cd build
%{__autoconf}
%configure \
	--prefix=$installdir
%{__make} -f ../config/%{_target_platform}*/topMakefile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/XSB

cp -a install/* $RPM_BUILD_ROOT%{_libdir}/XSB

cd build
%{__make} -f ../config/%{_target_platform}*/topMakefile \
	prefix=$RPM_BUILD_ROOT%{_libdir}/XSB

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE README
%attr(755,root,root) %{_bindir}/*
# TODO
