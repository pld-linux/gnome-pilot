Summary:	GNOME pilot programs
Summary(da):	GNOME pilot programmer
Summary(pl):	Programy pilota GNOME
Summary(pt_BR):	Programas do GNOME Pilot
Summary(ru):	Программы GNOME для работы с PalmPilot
Summary(uk):	Програми GNOME для роботи з PalmPilot
Summary(zh_CN):	╪╞ЁиGNOME╨мPalmPilot╣дЁлпР╪╞
Name:		gnome-pilot
Version:	0.1.69
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-pilot/0.1/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/gnome-pilot/
BuildRequires:	ORBit-devel >= 0.4.3
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	gettext-devel
BuildRequires:	gnome-core-devel >= 1.0.7
BuildRequires:	gnome-libs-devel
BuildRequires:	gob >= 1.0.4
BuildRequires:	libglade-gnome-devel
#BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	pilot-link-devel >= 0.11.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME pilot is a collection of programs and daemon for integrating
GNOME and the PalmPilot<tm>. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l da
GNOME stЕr for GNU Network Object Model Environment, GNU NetvФrk
Objekt Model MiljЬ. Et smart navn, men GNOME er i virkeligheden en
pФnt GUI desktop miljЬ. Det gЬr brugen af din computer nemmere,
kraftiger og nemmere at sФtte op.

%description -l pl
GNOME pilot jest kolekcj╠ programСw i demonСw integruj╠cych GNOME z
PalmPilotem(TM).

%description -l pt_BR
GNOME pilot И um conjunto de programas para integrar o GNOME ao
PalmPilot(tm).

%description -l ru
GNOME pilot - это коллекция программ и демон для интеграции GNOME и
PalmPilot (tm).

%description -l uk
GNOME pilot - це колекц╕я програм та демон для ╕нтеграц╕╖ GNOME та
PalmPilot (tm).

%package devel
Summary:	GNOME pilot includes, etc
Summary(da):	GNOME pilot include filer etc
Summary(ru):	Файлы разработки для GNOME pilot
Summary(pl):	Biblioteki i pliki nagЁСwkowe gpilotd
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo do GNOME pilot
Summary(uk):	Файли розробки для GNOME pilot
Summary(zh_CN):	GNOME pilot©╙╥╒©Б
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
gpilotd libraries and includes.

%description devel -l da
gpilotd include filer og biblioteker.

%description devel -l pl
Biblioteki i pliki nagЁСwkowe gpilotd.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo para desenvolvimento baseado no
GNOME pilot.

%description devel -l ru
Файлы разработки для GNOME pilot.

%description devel -l uk
Файли розробки для GNOME pilot.

%package static
Summary:	GNOME pilot static libraries
Summary(pl):	Biblioteki statyczne pakietu gnome-pilot
Summary(pt_BR):	Bibliotecas estАticas do GNOME pilot
Summary(ru):	Статические библиотеки для GNOME pilot
Summary(uk):	Статичн╕ б╕бл╕отеки для GNOME pilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME pilot static libraries

%description static -l pl
Biblioteki statyczne pakietu gnome-pilot.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento baseado no GNOME pilot.

%description static -l ru
Статические библиотеки для GNOME pilot.

%description static -l uk
Статичн╕ б╕бл╕отеки для GNOME pilot.

%prep
%setup -q

%build
#rm -f missing
#%{__gettextize}
#%{__libtoolize}
#%{__aclocal} -I macros
#%{__autoconf}
#%{__automake}
%configure
%{__make} PISOCK_LIBS="-lpisock -lpisync"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pPalmPilotdir=%{_applnkdir}/Settings/GNOME/Peripherals

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gnome-pilot
%dir %{_libdir}/gnome-pilot/conduits
%attr(755,root,root) %{_libdir}/gnome-pilot/conduits/lib*.so

%{_datadir}/applets/Utility/*
%{_datadir}/control-center/Peripherals/*
%{_applnkdir}/Settings/GNOME/Peripherals/*
%{_mandir}/man1/*
%{_datadir}/gnome-pilot
%{_datadir}/mime-info/*
%{_datadir}/idl/*
%{_datadir}/oaf/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
