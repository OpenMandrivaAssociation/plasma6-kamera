Summary:	Kamera ioslave
Name:		plasma6-kamera
Version:	24.01.90
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kamera-%{version}.tar.xz
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	pkgconfig(libgphoto2)

%description
Kamera ioslave.

%files -f kcmkamera.lang
%{_datadir}/qlogging-categories6/kamera.categories
%{_qtdir}/plugins/kf6/kio/kio_kamera.so
%{_datadir}/solid/actions/solid_camera.desktop
%{_datadir}/metainfo/org.kde.kamera.metainfo.xml
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kamera.so
%{_datadir}/applications/kcm_kamera.desktop

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kamera-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcmkamera --all-name --with-html
