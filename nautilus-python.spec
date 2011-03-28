Name:		nautilus-python
Summary:        Python bindings for GNOME 2's nautilus
Version:        0.7.3
Release: %mkrel 1
Source:		http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/%{name}-%{version}.tar.bz2
#gw hardcode libpython soname for dlopening to libpython2.6.so.1.0
URL: http://www.gnome.org
License:        GPLv2+ and LGPLv2+
Group:          Development/Python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	gnome-python-gconf
BuildRequires:  pygtk2.0-devel >= 2.8.0
BuildRequires:  gnome-python-devel >= 2.12.0
BuildRequires:  python-devel
BuildRequires:  nautilus-devel >= 2.22
BuildRequires:	gnome-common
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
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;
mv %buildroot%_datadir/doc/%name installed-docs

mkdir $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS installed-docs/*
%{_libdir}/nautilus-python
%{_libdir}/nautilus/extensions-2.0/*
%{_libdir}/pkgconfig/nautilus-python.pc


