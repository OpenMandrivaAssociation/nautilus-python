Name:		nautilus-python
Summary:        Python bindings for GNOME 2's nautilus
Version:        0.5.1
Release: %mkrel 2
Source:		http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/%{name}-%{version}.tar.bz2
Source1:	nautilus-python-0.5.1-m4.tar.bz2
Patch0:		nautilus-python-0.5.1-fix-include.patch
URL: http://www.gnome.org
License:        GPLv2+ and LGPLv2+
Group:          Development/Python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
BuildRequires:  pygtk2.0-devel
BuildRequires:  gnome-python-devel
BuildRequires:  gnome-python-gnomevfs >= 2.12.0
BuildRequires:  python-devel
BuildRequires:  nautilus-devel >= 2.8
BuildRequires:	eel-devel gnome-vfs2-devel
BuildRequires:	gnome-common
Provides: python-nautilus
Obsoletes: python-nautilus

%description
These are unstable bindings for the nautilus extension library
introduced in Gnome 2.6.

%prep
%setup -q -n %{name}-%{version} -a1
%patch0 -p0

%build
NOCONFIGURE=yes ACLOCAL_FLAGS="-I m4" gnome-autogen.sh
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


