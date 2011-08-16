# We require this gtk version to pick up support for the
# window-xid (gtk_status_icon_x11_get_window_id)
%define gtk2_version		2.13.2
%define glib2_version		2.2.2
%define dbus_version		0.90
%define dbus_glib_version	0.70

Summary: Desktop notification library
Name: libnotify
Version: 0.5.0
Release: 1%{?dist}
URL: http://live.gnome.org/libnotify
Source0: http://download.gnome.org/sources/%{name}/0.5/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtool
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
Requires: glib2 >= %{glib2_version}
Requires: desktop-notification-daemon

%description
libnotify is a library for sending desktop notifications to a notification
daemon, as defined in the freedesktop.org Desktop Notifications spec. These
notifications can be used to inform the user about an event or display some
form of information without getting in the user's way.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:       glib2-devel >= %{glib2_version}
Requires:       gtk2-devel >= %{gtk2_version}
Requires:	dbus-devel >= %{dbus_version}
Requires:	dbus-glib-devel >= %{dbus_glib_version}
Requires:	pkgconfig

%description devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
%setup -q

%build

%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING NEWS AUTHORS

%{_bindir}/notify-send
%{_libdir}/libnotify.so.*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/libnotify
%{_includedir}/libnotify/*
%{_libdir}/libnotify.so
%{_libdir}/pkgconfig/libnotify.pc
%dir %{_datadir}/gtk-doc/html/libnotify
%{_datadir}/gtk-doc/html/libnotify/*

%changelog
* Tue Jun 29 2010 Jon McCann <jmccann@redhat.com> 0.5.0-1
- Update to 0.5.0
  Resolves: #609244

* Wed Nov 11 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.5-4
- Close notifications with non-default actions on uninit

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.5-1
- Update to 0.4.5
- Drop obsolete patches
- Tweak %%summary and %%description

* Sat Aug 23 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.4-12
- Handle extra parameter of the closed signal

* Tue Jun 10 2008 Colin Walters <walters@redhat.com> - 0.4.4-11
- Add patch neccessary for reliable notification positioning

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.4-10
- Autorebuild for GCC 4.3

* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-9
- Rebuild against new dbus-glib

* Wed Oct 10 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-8
- Rebuild

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-7
- Update licence field

* Wed Jun  6 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-6
- Re-add notification-daemon requirement again

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-5
- Temporarily remove the notification-daemon requires 
  for bootstrapping

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-4
- Re-add notification-daemon requirement

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-3
- Temporarily remove the notification-daemon requires 
  for bootstrapping

* Sun Mar 25 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-2
- Require gtk2-devel in the -devel package (#216946)

* Fri Mar 23 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.4-1
- Update to 0.4.4, which contains important bug fixes 
  and memory leak fixes
- Require pkgconfig in the -devel package

* Sat Dec  9 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.3-2
- Another typo (#214275)

* Sat Nov 11 2006 Ray Strode <rstrode@redhat.com> - 0.4.3-1
- Update 0.4.3

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.2-5
- Fix typos in the spec (#214275)
 
* Sun Sep 17 2006 Christopher Aillon <caillon@redhat.com> - 0.4.2-4
- Add upstream patch (r2899) to correct an invalid assertion when
  creating notifications using status icons

* Tue Aug 15 2006 Luke Macken <lmacken@redhat.com> - 0.4.2-3
- Add upstream patch libnotify-0.4.2-status-icon.patch to emit the correct
  property change notification 'status-icon' instead of 'attach-icon'

* Fri Jul 21 2006 John (J5) Palmieri <johnp@redhat.com> - 0.4.2-2
- Add developer docs to the devel section

* Fri Jul 21 2006 John (J5) Palmieri <johnp@redhat.com> - 0.4.2-1
- Update to upstream version 0.4.2
- Add dist tag to release
- Add Requires to devel package

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.4.0-3.2
- reinstate desktop-notification dependency

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.4.0-3.1
- comment out desktop-notification dependency so we can build the
  notification daemon

* Tue Jul 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.4.0-3
- Add BR on dbus-glib-devel

* Wed Jul 13 2006 Jesse Keating <jkeating@redhat.com> - 0.4.0-2
- rebuild
- add missing brs

* Fri May 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Sat Mar 11 2006 Bill Nottingham <notting@redhat.com> - 0.3.0-6
- define %%{glib2_version} if it's in a requirement

* Thu Mar  2 2006 Ray Strode <rstrode@redhat.com> - 0.3.0-5
- patch out config.h include from public header

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Jan 12 2006 Christopher Aillon <caillon@redhat.com> - 0.3.0-4
- Require a desktop-notification-daemon to be present.  Currently,
  this is notify-daemon, but libnotify doesn't specifically require
  that one.  Require 'desktop-notification-daemon' which daemons
  providing compatible functionality are now expected to provide.

* Wed Jan 11 2006 Christopher Aillon <caillon@redhat.com> - 0.3.0-3
- Let there be libnotify-devel...

* Tue Nov 15 2005 John (J5) Palmieri <johnp@redhat.com> - 0.3.0-2
- Actual release of the 0.3.x series

* Tue Nov 15 2005 John (J5) Palmieri <johnp@redhat.com> - 0.3.0-1
- Bump version to not conflict with older libnotify libraries

* Tue Nov 15 2005 John (J5) Palmieri <johnp@redhat.com> - 0.0.2-1
- inital build
