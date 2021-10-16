%define _empty_manifest_terminate_build 0

%define _disable_lto 1

Summary:	Steve's Portable Game Library
Name:		plib
Version:	1.8.5
Release:	10
License:	LGPLv2+
Group:		Development/C++
URL:		http://plib.sourceforge.net/
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
Patch1:		plib-1.8.5-CVE-2011-4620.patch
Patch2:		plib-1.8.5-CVE-2012-4552.patch
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xmu)

%description
Write games and other realtime interactive applications that are 100% portable
across a wide range of hardware and operating systems.

#----------------------------------------------------

%package devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files devel
%doc README ChangeLog AUTHORS KNOWN_BUGS
%{_libdir}/lib%{name}*.a
%{_includedir}/plib/

#----------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%configure
%make_build

%install
%makeinstall \
	includedir=%{buildroot}%{_includedir}/%{name}

