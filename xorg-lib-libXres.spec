Summary:	X-Resource extension client library
Summary(pl.UTF-8):	Biblioteka kliencka rozszerzenia X-Resource
Name:		xorg-lib-libXres
Version:	1.2.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.xz
# Source0-md5:	66c9e9e01b0b53052bb1d02ebf8d7040
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-resourceproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	libXres < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Resource extension client library. This extension gives information
about X resources usage.

%description -l pl.UTF-8
Biblioteka kliencka rozszerzenia X-Resource, służącego do uzyskiwania
informacji o wykorzystaniu zasobów X.

%package devel
Summary:	Header files for libXres library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXres
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-resourceproto-devel >= 1.2.0
Requires:	xorg-proto-xextproto-devel
Obsoletes:	libXres-devel < 1.1

%description devel
X-Resource extension client library.

This package contains the header files needed to develop programs that
use libXres.

%description devel -l pl.UTF-8
Biblioteka kliencka rozszerzenia X-Resource.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXres.

%package static
Summary:	Static libXres library
Summary(pl.UTF-8):	Biblioteka statyczna libXres
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXres-static < 1.1

%description static
X-Resource extension client library.

This package contains the static libXres library.

%description static -l pl.UTF-8
Biblioteka kliencka rozszerzenia X-Resource.

Pakiet zawiera statyczną bibliotekę libXres.

%prep
%setup -q -n libXres-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXRes.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXRes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXRes.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXRes.so
%{_includedir}/X11/extensions/XRes.h
%{_pkgconfigdir}/xres.pc
%{_mandir}/man3/XRes*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXRes.a
