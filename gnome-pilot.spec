Summary:	GNOME pilot programs
Summary(da):	GNOME pilot programmer
Summary(pl):	Programy pilota GNOME
Summary(pt_BR):	Programas do GNOME Pilot
Summary(ru):	ðÒÏÇÒÁÍÍÙ GNOME ÄÌÑ ÒÁÂÏÔÙ Ó PalmPilot
Summary(uk):	ðÒÏÇÒÁÍÉ GNOME ÄÌÑ ÒÏÂÏÔÉ Ú PalmPilot
Name:		gnome-pilot
Version:	0.1.54
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://www.gnome.org/gnome-pilot/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fix.patch
URL:		http://www.gnome.org/gnome-pilot
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-core-devel >= 1.0.7
BuildRequires:	gnome-libs-devel
BuildRequires:	gob >= 1.0.4
BuildRequires:	libglade-devel
BuildRequires:	libxml-devel
BuildRequires:	ORBit-devel >= 0.4.3
BuildRequires:	pilot-link-devel >= 0.9.0
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME pilot is a collection of programs and daemon for integrating
GNOME and the PalmPilot<tm>. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l da
GNOME står for GNU Network Object Model Environment, GNU Netværk
Objekt Model Miljø. Et smart navn, men GNOME er i virkeligheden en
pænt GUI desktop miljø. Det gør brugen af din computer nemmere,
kraftiger og nemmere at sætte op.

%description -l pl
GNOME pilot jest kolekcj± programów i demonów integruj±cych GNOME z
PalmPilotem(TM).

%description -l pt_BR
GNOME pilot é um conjunto de programas para integrar o GNOME ao
PalmPilot(tm).

%description -l ru
GNOME pilot - ÜÔÏ ËÏÌÌÅËÃÉÑ ÐÒÏÇÒÁÍÍ É ÄÅÍÏÎ ÄÌÑ ÉÎÔÅÇÒÁÃÉÉ GNOME É
PalmPilot (tm).

%description -l uk
GNOME pilot - ÃÅ ËÏÌÅËÃ¦Ñ ÐÒÏÇÒÁÍ ÔÁ ÄÅÍÏÎ ÄÌÑ ¦ÎÔÅÇÒÁÃ¦§ GNOME ÔÁ
PalmPilot (tm).

%package devel
Summary:	GNOME pilot includes, etc
Summary(da):	GNOME pilot include filer etc
Summary(ru):	æÁÊÌÙ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ GNOME pilot
Summary(pl):	Biblioteki i pliki nag³ówkowe gpilotd
Summary(pt_BR):	Bibliotecas e arquivos de inclusão do GNOME pilot
Summary(uk):	æÁÊÌÉ ÒÏÚÒÏÂËÉ ÄÌÑ GNOME pilot
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
gpilotd libraries and includes.

%description devel -l da
gpilotd include filer og biblioteker.

%description devel -l pl
Biblioteki i pliki nag³ówkowe gpilotd.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento baseado no
GNOME pilot.

%description devel -l ru
æÁÊÌÙ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ GNOME pilot.

%description devel -l uk
æÁÊÌÉ ÒÏÚÒÏÂËÉ ÄÌÑ GNOME pilot.

%package static
Summary:	GNOME pilot static libraries
Summary(pl):	Biblioteki statyczne pakietu gnome-pilot
Summary(pt_BR):	Bibliotecas estáticas do GNOME pilot
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ GNOME pilot
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ GNOME pilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME pilot static libraries

%description static -l pl
Biblioteki statyczne pakietu gnome-pilot.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento baseado no GNOME pilot.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ GNOME pilot.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ GNOME pilot.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pPalmPilotdir=%{_applnkdir}/Settings/GNOME/Peripherals \
	paneldir=%{_applnkdir}/Settings/GNOME/Peripherals/Conduits \

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/backup-conduit-control-applet
%attr(755,root,root) %{_bindir}/email-conduit-control-applet
%attr(755,root,root) %{_bindir}/expense-conduit-control-applet
%attr(755,root,root) %{_bindir}/file-conduit-control-applet
%attr(755,root,root) %{_bindir}/gnome-pilot-make-password
%attr(755,root,root) %{_bindir}/gpilot-install-file
%attr(755,root,root) %{_bindir}/gpilotd
%attr(755,root,root) %{_bindir}/gpilotd-client
%attr(755,root,root) %{_bindir}/gpilotd-control-applet
%attr(755,root,root) %{_bindir}/gpilotd-session-wrapper
%attr(755,root,root) %{_bindir}/gpilotdcm-client
%attr(755,root,root) %{_bindir}/memo_file_capplet
%attr(755,root,root) %{_bindir}/pilot_applet
%{_sysconfdir}/CORBA/servers/*

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gnome-pilot
%dir %{_libdir}/gnome-pilot/conduits
%attr(755,root,root) %{_libdir}/gnome-pilot/conduits/lib*.so*

%{_datadir}/applets/Utility/*
%dir %{_datadir}/control-center/Peripherals/Conduits
%{_datadir}/control-center/Peripherals/Conduits/*desktop
%{_datadir}/control-center/Peripherals/Conduits/.directory
%{_datadir}/control-center/Peripherals/gpilotd-control-applet.desktop
%dir %{_applnkdir}/Settings/GNOME/Peripherals/Conduits
%{_applnkdir}/Settings/GNOME/Peripherals/Conduits/*desktop
%{_applnkdir}/Settings/GNOME/Peripherals/Conduits/.directory
%{_applnkdir}/Settings/GNOME/Peripherals/gpilotd-control-applet.desktop
%{_datadir}/gnome-pilot
%{_datadir}/mime-info/*
%{_datadir}/oaf/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*
%{_datadir}/idl/*
%{_datadir}/gob/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-pilot/conduits/lib*.a
