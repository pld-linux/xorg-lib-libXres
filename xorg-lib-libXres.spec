Summary:	X-Resource extension client library
Summary(pl.UTF-8):	Biblioteka kliencka rozszerzenia X-Resource
Name:		xorg-lib-libXres
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2
# Source0-md5:	80d0c6d8522fa7a645e4f522e9a9cd20
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-resourceproto-devel >= 1.0
BuildRequires:	xorg-util-util-macros >= 1.8
Obsoletes:	libXres
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
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-resourceproto-devel >= 1.0
Obsoletes:	libXres-devel

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
Obsoletes:	libXres-static

%description static
X-Resource extension client library.

This package contains the static libXres library.

%description static -l pl.UTF-8
Biblioteka kliencka rozszerzenia X-Resource.

Pakiet zawiera statyczną bibliotekę libXres.

%prep
%setup -q -n libXres-%{version}

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXRes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXRes.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXRes.so
%{_includedir}/X11/extensions/XRes.h
%{_pkgconfigdir}/xres.pc
%{_mandir}/man3/XRes*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXRes.a
