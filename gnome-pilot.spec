#
# Note that this is NOT a relocatable package
# $Id: gnome-pilot.spec,v 1.1 2000-02-17 06:40:42 kloczek Exp $
#
%define ver      0.1.47
%define rel      1
%define prefix   /usr
%define name	 gnome-pilot

Summary: GNOME pilot programs
Summary(da): GNOME pilot programmer
Name: %name
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Communications
Source: http://www.gnome.org/gnome-pilot/download/%name-%ver.tar.gz
BuildRoot: /var/tmp/gnome-pilot
Obsoletes: gnome-pilot
Packager: Eskil Heyn Olsen <deity@eskil.dk>
URL: http://www.gnome.org/gnome-pilot
Prereq: /sbin/install-info
Prefix: %{prefix}
Docdir: %{prefix}/doc
Requires: pilot-link >= 0.9.0
Requires: gnome-core >= 1.0.7
Requires: ORBit >= 0.4.3

%description
GNOME pilot is a collection of programs and daemon for integrating
GNOME and the PalmPilot<tm>.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l da

GNOME står for GNU Network Object Model Environment, GNU Netværk Objekt
Model Miljø. Et smart navn, men GNOME er i virkeligheden en pænt GUI
desktop miljø. Det gør brugen af din computer nemmere, kraftiger og nemmere
at sætte op.

%package devel
Summary: GNOME pilot libraries, includes, etc
Summary(da): GNOME pilot biblioteker, include filer etc.
Group: Development/Libraries
Requires: gnome-core-devel
Requires: ORBit-devel
Requires: pilot-link-devel
Requires: gnome-pilot = %{ver}
PreReq: /sbin/install-info

%description devel
gpilotd libraries and includes.

%description devel -l da
gpilotd include filer og biblioteker.

%changelog

* Wed Feb 17 1999 Eskil Heyn Olsen <deity@eskil.dk>

- Created the .spec file

%prep
%setup

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT/etc
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=$RPM_BUILD_ROOT/etc
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin
%{prefix}/lib
%{prefix}/share
%config /etc

%files devel
%defattr(-, root, root)
%{prefix}/include/
