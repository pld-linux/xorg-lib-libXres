
#
Summary:	X Resource usage extension library
Summary(pl):	Biblioteka rozszerzenia X Resource usage
Name:		xorg-lib-libXres
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXres-%{version}.tar.bz2
# Source0-md5:	cb705942677fb7bc28ef42db5e602ff4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXres
BuildRoot:	%{tmpdir}/libXres-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Resource usage extension library.

%description -l pl
Biblioteka rozszerzenia X Resource usage, s³u¿±cego do uzyskiwania
informacji o wykorzystaniu zasobów X.


%package devel
Summary:	Header files libXres development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXres
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXres = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-resourceproto-devel
Obsoletes:	libXres-devel

%description devel
X Resource usage extension library.

This package contains the header files needed to develop programs that
use these libXres.

%description devel -l pl
Biblioteka rozszerzenia X Resource usage, s³u¿±cego do uzyskiwania
informacji o wykorzystaniu zasobów X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXres.


%package static
Summary:	Static libXres libraries
Summary(pl):	Biblioteki statyczne libXres
Group:		Development/Libraries
Requires:	xorg-lib-libXres-devel = %{version}-%{release}
Obsoletes:	libXres-static

%description static
X Resource usage extension library.

This package contains the static libXres library.

%description static -l pl
Biblioteka rozszerzenia X Resource usage, s³u¿±cego do uzyskiwania
informacji o wykorzystaniu zasobów X.

Pakiet zawiera statyczn± bibliotekê libXres.


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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXRes.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXRes.la
%attr(755,root,wheel) %{_libdir}/libXRes.so
%{_pkgconfigdir}/xres.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXRes.a
