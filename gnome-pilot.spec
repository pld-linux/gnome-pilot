Summary:	GNOME pilot programs
Summary(da):	GNOME pilot programmer
Summary(pl):	Programy pilota GNOME
Summary(pt_BR):	Programas do GNOME Pilot
Summary(ru):	��������� GNOME ��� ������ � PalmPilot
Summary(uk):	�������� GNOME ��� ������ � PalmPilot
Summary(zh_CN):	����GNOME��PalmPilot�ĳ���
Name:		gnome-pilot
Version:	2.0.15
Release:	1
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
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME pilot is a collection of programs and daemon for integrating
GNOME and the PalmPilot<tm>. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l da
GNOME st�r for GNU Network Object Model Environment, GNU Netv�rk
Objekt Model Milj�. Et smart navn, men GNOME er i virkeligheden en
p�nt GUI desktop milj�. Det g�r brugen af din computer nemmere,
kraftiger og nemmere at s�tte op.

%description -l pl
GNOME pilot jest kolekcj� program�w i demon�w integruj�cych GNOME z
PalmPilotem(TM).

%description -l pt_BR
GNOME pilot � um conjunto de programas para integrar o GNOME ao
PalmPilot(tm).

%description -l ru
GNOME pilot - ��� ��������� �������� � ����� ��� ���������� GNOME �
PalmPilot (tm).

%description -l uk
GNOME pilot - �� �����æ� ������� �� ����� ��� �������æ� GNOME ��
PalmPilot (tm).

%package libs
Summary:	GNOME pilot library
Summary(pl):	Biblioteka GNOME pilot
Group:		Development/Libraries

%description libs
GNOME pilot library.

%description libs -l da
Biblioteka GNOME pilot.

%package devel
Summary:	GNOME pilot includes, etc
Summary(da):	GNOME pilot include filer etc
Summary(ru):	����� ���������� ��� GNOME pilot
Summary(pl):	Biblioteki i pliki nag��wkowe gpilotd
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o do GNOME pilot
Summary(uk):	����� �������� ��� GNOME pilot
Summary(zh_CN):	GNOME pilot������
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgnomeui-devel >= 2.16.0
Requires:	pilot-link-devel >= 0.11.8

%description devel
gpilotd libraries and includes.

%description devel -l da
gpilotd include filer og biblioteker.

%description devel -l pl
Biblioteki i pliki nag��wkowe gpilotd.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento baseado no
GNOME pilot.

%description devel -l ru
����� ���������� ��� GNOME pilot.

%description devel -l uk
����� �������� ��� GNOME pilot.

%package static
Summary:	GNOME pilot static libraries
Summary(pl):	Biblioteki statyczne pakietu gnome-pilot
Summary(pt_BR):	Bibliotecas est�ticas do GNOME pilot
Summary(ru):	����������� ���������� ��� GNOME pilot
Summary(uk):	������Φ ¦�̦����� ��� GNOME pilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNOME pilot static libraries

%description static -l pl
Biblioteki statyczne pakietu gnome-pilot.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento baseado no GNOME pilot.

%description static -l ru
����������� ���������� ��� GNOME pilot.

%description static -l uk
������Φ ¦�̦����� ��� GNOME pilot.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-usb \
	--enable-network

# regenerate
rm -f applet/gpilot-applet-progress.c gpilotd/gnome-pilot-client.c gpilotd/gnome-pilot-conduit.c gpilotd/gnome-pilot-conduit-backup.c
rm -f gpilotd/gnome-pilot-conduit-file.c gpilotd/gnome-pilot-conduit-standard.c libgpilotdCM/gnome-pilot-conduit-management.c
rm -f libgpilotdCM/gnome-pilot-conduit-config.c

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/conduits/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

install -d $RPM_BUILD_ROOT%{_desktopdir}

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
