Summary:	X Resource usage extension library
Summary(pl):	Biblioteka rozszerzenia X Resource usage
Name:		xorg-lib-libXres
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/lib/libXres-%{version}.tar.bz2
# Source0-md5:	63e624cd9ee5dd571366b494b1e64dff
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-resourceproto-devel >= 0.99
BuildRequires:	xorg-util-util-macros >= 0.99.1
Obsoletes:	libXres
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Resource usage extension library.

%description -l pl
Biblioteka rozszerzenia X Resource usage, s�u��cego do uzyskiwania
informacji o wykorzystaniu zasob�w X.

%package devel
Summary:	Header files libXres development
Summary(pl):	Pliki nag��wkowe do biblioteki libXres
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-resourceproto-devel >= 0.99
Obsoletes:	libXres-devel

%description devel
X Resource usage extension library.

This package contains the header files needed to develop programs that
use these libXres.

%description devel -l pl
Biblioteka rozszerzenia X Resource usage, s�u��cego do uzyskiwania
informacji o wykorzystaniu zasob�w X.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libXres.

%package static
Summary:	Static libXres library
Summary(pl):	Biblioteka statyczna libXres
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXres-static

%description static
X Resource usage extension library.

This package contains the static libXres library.

%description static -l pl
Biblioteka rozszerzenia X Resource usage, s�u��cego do uzyskiwania
informacji o wykorzystaniu zasob�w X.

Pakiet zawiera statyczn� bibliotek� libXres.

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
	libmandir=%{_mandir}/man3 \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXRes.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXRes.so
%{_libdir}/libXRes.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xres.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXRes.a
