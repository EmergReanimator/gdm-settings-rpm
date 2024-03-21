%global         forgeurl https://github.com/gdm-settings/gdm-settings
%global         uuid io.github.gdm-settings.GdmSettings

Name:      gdm-settings
Version:   4.3
Release:   %autorelease
Summary:   A settings app for Gnome Login Manager (GDM)
BuildArch: noarch

%global tag v%{version}
%forgemeta

License:   AGPL-3.0-or-later
URL:       %{forgeurl}
Source0:   %{forgesource}

BuildRequires: meson
BuildRequires: gobject-introspection
BuildRequires: desktop-file-utils

Requires: gdm
Requires: polkit
Requires: libadwaita-devel
Requires: glib2-devel
Requires: pygobject3-devel
Requires: gettext

%description
A tool for customizing GNOME Display Manager.

With User Login Manager you can:
* Import user/session settings (currently not working on Flatpak)
* Change Background/Wallpaper (Image/Color)
* Apply themes
* Font Settings 
* Top Bar Settings 
* Display settings 


%prep
%forgeautosetup


%build
%meson --buildtype=release
%meson_build


%install
%meson_install

%find_lang %{name}


%check
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/gdm-settings
%{_datadir}/gdm-settings
%{python3_sitelib}/gdm_settings
%{_datadir}/metainfo/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}*
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog
