Summary:	Steve's Portable Game Library
Name:		plib
Version:	1.8.5
Release:	4
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

%package -n	%{name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description -n %{name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
%makeinstall includedir=%{buildroot}%{_includedir}/%{name}

%files -n %{name}-devel
%doc README ChangeLog AUTHORS KNOWN_BUGS
%{_libdir}/lib*
%{_includedir}/plib

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8.5-3mdv2010.0
+ Revision: 430746
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.8.5-2mdv2009.0
+ Revision: 259099
- rebuild

* Thu Jul 31 2008 Frederik Himpe <fhimpe@mandriva.org> 1.8.5-1mdv2009.0
+ Revision: 258422
- Update to new upstream version 1.8.5

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.8.4-6mdv2009.0
+ Revision: 247022
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.8.4-4mdv2008.1
+ Revision: 140733
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 14 2007 Couriousous <couriousous@mandriva.org> 1.8.4-4mdv2007.1
+ Revision: 143491
- mkrel
- Patch for gcc ( Thanks to baud123 )

  + Jérôme Soyer <saispo@mandriva.org>
    - Import plib

* Sun Oct 09 2005 Couriousous <couriousous@mandriva.org> 1.8.4-3mdk
- Compile with -fPIC

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.4-2mdk
- versioned provides

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.4-1mdk
- 1.8.4

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.3-2mdk
- rebuild

* Sun May 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.3-1mdk
- 1.8.3
- update docs

* Fri Apr 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.2-1mdk
- 1.8.2

* Fri Apr 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.0-1mdk
- 1.8.0

