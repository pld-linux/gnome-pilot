Summary:	GNOME pilot programs
Summary(da.UTF-8):	GNOME pilot programmer
Summary(pl.UTF-8):	Programy pilota GNOME
Summary(pt_BR.UTF-8):	Programas do GNOME Pilot
Summary(ru.UTF-8):	Программы GNOME для работы с PalmPilot
Summary(uk.UTF-8):	Програми GNOME для роботи з PalmPilot
Summary(zh_CN.UTF-8):	集成GNOME和PalmPilot的程序集
Name:		gnome-pilot
Version:	2.0.15
Release:	4
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-pilot/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	460a1fdd2206e1bbf820639831ca88f8
Patch0:		%{name}-capplet.patch
Patch1:		%{name}-ldadd.patch
URL:		http://www.gnome.org/gnome-pilot/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel >= 1:2.14.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gnome-panel-devel >= 2.16.0
BuildRequires:	gnome-vfs2-devel >= 2.16.0
BuildRequires:	gob2 >= 2.0.14
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pilot-link-devel >= 0.11.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	%{name}-libs = %{version}-%{release}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME pilot is a collection of programs and daemon for integrating
GNOME and the PalmPilot<tm>. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l da.UTF-8
GNOME står for GNU Network Object Model Environment, GNU Netværk
Objekt Model Miljø. Et smart navn, men GNOME er i virkeligheden en
pænt GUI desktop miljø. Det gør brugen af din computer nemmere,
kraftiger og nemmere at sætte op.

%description -l pl.UTF-8
GNOME pilot jest kolekcją programów i demonów integrujących GNOME z
PalmPilotem(TM).

%description -l pt_BR.UTF-8
GNOME pilot é um conjunto de programas para integrar o GNOME ao
PalmPilot(tm).

%description -l ru.UTF-8
GNOME pilot - это коллекция программ и демон для интеграции GNOME и
PalmPilot (tm).

%description -l uk.UTF-8
GNOME pilot - це колекція програм та демон для інтеграції GNOME та
PalmPilot (tm).

%package libs
Summary:	GNOME pilot library
Summary(pl.UTF-8):	Biblioteka GNOME pilot
Group:		Development/Libraries

%description libs
GNOME pilot library.

%description libs -l da.UTF-8
Biblioteka GNOME pilot.

%package devel
Summary:	GNOME pilot includes, etc
Summary(da.UTF-8):	GNOME pilot include filer etc
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe gpilotd
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão do GNOME pilot
Summary(ru.UTF-8):	Файлы разработки для GNOME pilot
Summary(uk.UTF-8):	Файли розробки для GNOME pilot
Summary(zh_CN.UTF-8):	GNOME pilot开发库
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgnomeui-devel >= 2.16.0
Requires:	pilot-link-devel >= 0.11.8

%description devel
gpilotd libraries and includes.

%description devel -l da.UTF-8
gpilotd include filer og biblioteker.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe gpilotd.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento baseado no
GNOME pilot.

%description devel -l ru.UTF-8
Файлы разработки для GNOME pilot.

%description devel -l uk.UTF-8
Файли розробки для GNOME pilot.

%package static
Summary:	GNOME pilot static libraries
Summary(pl.UTF-8):	Biblioteki statyczne pakietu gnome-pilot
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do GNOME pilot
Summary(ru.UTF-8):	Статические библиотеки для GNOME pilot
Summary(uk.UTF-8):	Статичні бібліотеки для GNOME pilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNOME pilot static libraries

%description static -l pl.UTF-8
Biblioteki statyczne pakietu gnome-pilot.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento baseado no GNOME pilot.

%description static -l ru.UTF-8
Статические библиотеки для GNOME pilot.

%description static -l uk.UTF-8
Статичні бібліотеки для GNOME pilot.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# regenerate
rm -f applet/gpilot-applet-progress.c gpilotd/gnome-pilot-client.c gpilotd/gnome-pilot-conduit.c gpilotd/gnome-pilot-conduit-backup.c
rm -f gpilotd/gnome-pilot-conduit-file.c gpilotd/gnome-pilot-conduit-standard.c libgpilotdCM/gnome-pilot-conduit-management.c
rm -f libgpilotdCM/gnome-pilot-conduit-config.c

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-usb \
	--enable-network
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/conduits/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

install -d $RPM_BUILD_ROOT%{_desktopdir}

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install pilot.schemas

%preun
%gconf_schema_uninstall pilot.schemas

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gpilot*
%dir %{_libdir}/gnome-pilot
%dir %{_libdir}/gnome-pilot/conduits
%attr(755,root,root) %{_libdir}/gnome-pilot/conduits/lib*.so
%{_libdir}/bonobo/servers/*
%{_desktopdir}/*.desktop
%{_datadir}/gnome-pilot
%{_datadir}/idl/*
%{_sysconfdir}/gconf/schemas/pilot.schemas
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
