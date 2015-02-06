%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Steve's Portable Game Library
Name:		plib
Version:	1.8.5
Release:	7
License:	LGPLv2+
Group:		Development/C++
URL:		http://plib.sourceforge.net/
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
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

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
%makeinstall \
	includedir=%{buildroot}%{_includedir}/%{name}

