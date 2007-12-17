%define	name	plib
%define	version	1.8.4
%define	release	%mkrel 4

Summary:	Steve's Portable Game Library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Development/C++
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.bz2
Patch0:		plib-gcc.patch
URL:		http://plib.sourceforge.net/
Buildrequires:	MesaGLU-devel Mesa-common-devel
# Author: Steve J. Baker <sjbaker1@airmail.net>

%description
Write games and other realtime interactive applications that are 100% portable
across a wide range of hardware and operating systems.

%package -n	%{name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}
Provides:	%{name} = %{version}-%{release}

%description -n %{name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export LDFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} includedir=$RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}-devel
%defattr(-, root, root)
%doc README ChangeLog AUTHORS KNOWN_BUGS
%{_libdir}/lib*
%{_includedir}/plib


