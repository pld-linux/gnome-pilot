Summary:	GNOME pilot programs
Summary(da):	GNOME pilot programmer
Summary(pl):	Programy pilota GNOME
Summary(pt_BR):	Programas do GNOME Pilot
Summary(ru):	��������� GNOME ��� ������ � PalmPilot
Summary(uk):	�������� GNOME ��� ������ � PalmPilot
Summary(zh_CN):	����GNOME��PalmPilot�ĳ���
Name:		gnome-pilot
Version:	2.0.10
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-pilot/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	840ed31beddf1398ea4bb3c01b6caa70
URL:		http://www.gnome.org/gnome-pilot/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 2.7.5-1
BuildRequires:	gnome-panel-devel >= 2.3.4.1-2
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gob2 >= 2.0.3
Buildrequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libxml2-devel
BuildRequires:	pilot-link-devel >= 0.11.8
BuildRequires:	pkgconfig
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post):	GConf2 >= 2.3.0
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

%package devel
Summary:	GNOME pilot includes, etc
Summary(da):	GNOME pilot include filer etc
Summary(ru):	����� ���������� ��� GNOME pilot
Summary(pl):	Biblioteki i pliki nag��wkowe gpilotd
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o do GNOME pilot
Summary(uk):	����� �������� ��� GNOME pilot
Summary(zh_CN):	GNOME pilot������
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libgnomeui-devel >= 2.3.3.1-2
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
Requires:	%{name}-devel = %{version}

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

%build
%configure \
	--enable-usb \
	--enable-network

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/conduits/*.{la,a}

install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets
mv $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/*.desktop $RPM_BUILD_ROOT%{_datadir}/gnome/capplets


%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gpilot*
%dir %{_libdir}/gnome-pilot
%dir %{_libdir}/gnome-pilot/conduits
%attr(755,root,root) %{_libdir}/gnome-pilot/conduits/lib*.so
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome/capplets/*
%{_datadir}/gnome-pilot
%{_datadir}/mime-info/*
%{_datadir}/idl/*
%{_sysconfdir}/gconf/schemas/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
