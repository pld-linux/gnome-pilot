Summary:	GNOME pilot programs
Summary(da):	GNOME pilot programmer
Name:		gnome-pilot
Version:	0.1.50
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.gnome.org/gnome-pilot/download/%{name}-%{version}.tar.gz
Patch1:		gnome-pilot-DESTDIR.patch
URL:		http://www.gnome.org/gnome-pilot
BuildRequires:	pilot-link-devel >= 0.9.0
BuildRequires:	gnome-core-devel >= 1.0.7
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-devel
BuildRequires:	ORBit-devel >= 0.4.3
BuildRequires:	gob >= 0.92.4
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	pilot-link-devel
BuildRequires:	libxml-devel
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

%package devel
Summary:	GNOME pilot includes, etc
Summary(da):	GNOME pilot include filer etc
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
gpilotd libraries and includes.

%description -l da devel
gpilotd include filer og biblioteker.

%package static
Summary:	GNOME pilot static libraries
Summary(pl):	Biblioteki statyczne pakietu gnome-pilot
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME pilot static libraries

%description -l pl devel
Biblioteki statyczne pakietu gnome-pilot.

%prep
%setup -q
%patch1 -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/gnome-pilot/conduits/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
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
%{_datadir}/control-center/Peripherals/PalmPilot
%{_datadir}/gnome-pilot
%{_datadir}/gob/*
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-pilot-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_datadir}/idl/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-pilot/conduits/lib*.a
