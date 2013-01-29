Name:           harfbuzz
Version:        0.9.12
Release:        0
License:        MIT
Summary:        An OpenType text shaping engine
Url:            http://www.freedesktop.org/wiki/Software/HarfBuzz
Group:          Productivity/Text/Utilities
Source:         %{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo) >= 1.8.0
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(freetype2) >= 2.3.8
BuildRequires:  pkgconfig(glib-2.0) >= 2.16
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(icu-uc)

%description
HarfBuzz is an OpenType text shaping engine.

%package -n libharfbuzz
Summary:        An OpenType text shaping engine
Group:          System/Libraries

%description -n libharfbuzz
HarfBuzz is an OpenType text shaping engine.

%package tools
Summary:        An OpenType text shaping engine -- Tools
Group:          Productivity/Text/Utilities

%description tools
HarfBuzz is an OpenType text shaping engine.

%package devel
Summary:        An OpenType text shaping engine -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libharfbuzz = %{version}

%description devel
HarfBuzz is an OpenType text shaping engine.

%prep
%setup -q

%build
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -n libharfbuzz -p /sbin/ldconfig

%postun -n libharfbuzz -p /sbin/ldconfig

%files -n libharfbuzz
%defattr(-,root,root)
%license COPYING
%{_libdir}/libharfbuzz.so.0*

%files tools
%defattr(-,root,root)
%{_bindir}/hb-ot-shape-closure
%{_bindir}/hb-shape
%{_bindir}/hb-view

%files devel
%defattr(-,root,root)
%{_includedir}/harfbuzz/
%{_libdir}/*.so
%{_libdir}/pkgconfig/harfbuzz.pc
