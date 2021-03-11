%define _disable_ld_no_undefined 1

Name:		nautilus-python
Summary:        Python bindings for GNOME nautilus
Version:        1.2.3
Release:        2
Source:		http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/%{name}-%{version}.tar.xz
#gw hardcode libpython soname for dlopening to libpython2.6.so.1.0
URL: http://www.gnome.org
License:        GPLv2+ and LGPLv2+
Group:          Development/Python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(libnautilus-extension) >= 2.32
BuildRequires:  pkgconfig(gtk-doc)
#Not required anymore (also not available for armv7) but make it recommend to pass tests.
Recommends: gnome-python-gconf

Provides: python-nautilus
Obsoletes: python-nautilus

%description
These are unstable bindings for the nautilus extension library
introduced in Gnome 2.6.

%prep
%setup -q -n %{name}-%{version} 

%build
%ifarch x86_64
export CFLAGS="%optflags -fPIC"
%endif
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;
mv %buildroot%_datadir/doc/%name installed-docs

mkdir $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS installed-docs/*
%{_libdir}/nautilus/extensions-3.0/*
%{_libdir}/pkgconfig/nautilus-python.pc




%changelog
* Wed Apr 18 2012 Götz Waschk <waschk@mandriva.org> 1.0-2mdv2012.0
+ Revision: 791646
- build with current nautilus
- yearly rebuild

* Sun Apr 17 2011 Götz Waschk <waschk@mandriva.org> 1.0-1
+ Revision: 654789
- new version
- update file list

* Mon Mar 28 2011 Götz Waschk <waschk@mandriva.org> 0.7.3-1
+ Revision: 648687
- update to new version 0.7.3

* Fri Mar 04 2011 Götz Waschk <waschk@mandriva.org> 0.7.2-1
+ Revision: 641617
- update to new version 0.7.2

* Wed Mar 02 2011 Götz Waschk <waschk@mandriva.org> 0.7.1-1
+ Revision: 641331
- new version

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 593006
- rebuild for new python 2.7

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 563368
- update to new version 0.7.0

* Tue Jan 19 2010 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 493772
- new version
- drop patch

* Fri Jan 15 2010 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 491862
- new version
- drop patches 0,1
- drop extra m4 files
- rediff patch 2
- update build deps

* Thu Oct 08 2009 Götz Waschk <waschk@mandriva.org> 0.5.1-5mdv2010.0
+ Revision: 456032
- fix loading of libpython (bug #39416)

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.5.1-4mdv2010.0
+ Revision: 440238
- rebuild

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 0.5.1-3mdv2009.1
+ Revision: 347046
- fix for CVS-2009-0317

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.5.1-2mdv2009.1
+ Revision: 320311
- fix BRs
- BR eel
- rebuild for new python

* Tue Sep 16 2008 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2009.0
+ Revision: 285336
- new version
- drop patch
- fix installation
- fix license

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-5mdv2009.0
+ Revision: 253611
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - create python extensions dir

* Wed Jan 23 2008 Götz Waschk <waschk@mandriva.org> 0.5.0-3mdv2008.1
+ Revision: 157106
- really fix extensions dir

* Wed Jan 23 2008 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdv2008.1
+ Revision: 157089
- new nautilus extensions dir

* Sun Jan 13 2008 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2008.1
+ Revision: 151032
- new version
- fix installation

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 05 2007 Götz Waschk <waschk@mandriva.org> 0.4.3-4mdv2008.1
+ Revision: 115623
- fix buildrequires


* Thu Nov 30 2006 Götz Waschk <waschk@mandriva.org> 0.4.3-3mdv2007.0
+ Revision: 88874
- Import nautilus-python

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.4.3-3mdv2007.1
- Rebuild

* Fri Jul 14 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.3-2mdv2007.0
- Rebuild with latest libgail

* Thu Feb 16 2006 Götz Waschk <waschk@mandriva.org> 0.4.3-1mdk
- New release 0.4.3

* Mon Feb 13 2006 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdk
- New release 0.4.2
- use mkrel

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.4.1-2mdk
- fix buildrequires

* Sun Oct 09 2005 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdk
- rename from python-nautilus
- fix buildrequires
- New release 0.4.1

* Wed Jun 01 2005 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdk
- initial mdk package

* Sat Dec 11 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- initial spec file

