#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	libmutil - different utilities classes for portable C++ development
Summary(pl.UTF-8):	libmutil - różne klasy narzędziowe do przenośnego programowania w C++
Name:		libmutil
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.minisip.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	3fd720e036a8b1ccc8eedcdce3bcfa47
URL:		http://www.minisip.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmutil contains different classes useful for C++ programming, mostly
string handling, cryptography and portable thread control. It is used
by the minisip SIP user agent.

%description -l pl.UTF-8
Biblioteka libmutil zawiera różne klasy przydatne do programowania w
C++, głównie obsługi łańcuchów znaków, kryptografii i przenośnego
sterowania wątkami. Jest używana przez agenta SIP minisip.

%package devel
Summary:	Header files for libmutil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmutil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	openssl-devel >= 0.9.7d

%description devel
Header files for libmutil library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmutil.

%package static
Summary:	Static libmutil library
Summary(pl.UTF-8):	Statyczna biblioteka libmutil
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmutil library.

%description static -l pl.UTF-8
Statyczna biblioteka libmutil.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmutil.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutil.so
%{_libdir}/libmutil.la
%{_includedir}/libmutil

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmutil.a
%endif
