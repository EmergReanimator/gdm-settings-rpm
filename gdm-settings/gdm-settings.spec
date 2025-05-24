%global         forgeurl https://github.com/gdm-settings/gdm-settings
%global         uuid io.github.gdm-settings.GdmSettings

Name:      gdm-settings
Version:   5.0
Release:   %autorelease
Summary:   A settings app for Gnome Login Manager (GDM)
BuildArch: noarch

%global tag v%{version}
%forgemeta

License:   AGPL-3.0-or-later
URL:       %{forgeurl}
Source0:   %{forgesource}

BuildRequires: meson cmake
BuildRequires: gobject-introspection
BuildRequires: glib2-devel python3-gobject-devel gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: blueprint-compiler
BuildRequires: desktop-file-utils

# Needed for python3_sitelib
BuildRequires: python3-devel

Requires: gdm
Requires: polkit
Requires: glib2
Requires: gettext
Requires: blueprint-compiler

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
mv %{buildroot}/%{_datadir}/applications/io.github.realmazharhussain.GdmSettings.desktop %{buildroot}/%{_datadir}/applications/%{uuid}.desktop
mv %{buildroot}/%{_datadir}/metainfo/io.github.realmazharhussain.GdmSettings.metainfo.xml %{buildroot}/%{_datadir}/metainfo/io.github.gdm-settings.GdmSettings.appdata.xml
# mv %{buildroot}/%{_datadir}/usr/share/glib-2.0/schemas/ %{buildroot}/%{_datadir}/usr/share/glib-2.0/schemas/io.github.gdm-settings.GdmSettings*
mv %{buildroot}/%{_datadir}/dbus-1/services/io.github.realmazharhussain.GdmSettings.service %{buildroot}/%{_datadir}/dbus-1/services/io.github.GdmSettings.appdata.xml

# Rename files by replacing 'realmazharhussain' with 'gdm-settings' in the filename
for file in %{buildroot}/%{_datadir}/glib-2.0/schemas/*realmazharhussain*; do
    mv "$file" "${file/realmazharhussain/gdm-settings}"
done

%find_lang %{name}


%check
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/gdm-settings
%{_datadir}/gdm-settings
%{_datadir}/dbus-1/services
%{_datadir}/metainfo/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}*
%{_datadir}/icons/hicolor/*/*/*.svg
%{python3_sitelib}/gdms

%changelog
%autochangelog
