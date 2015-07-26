Name:           Cadence
Version:        master
Release:        5.git13c3ca8%{?dist}
Summary:        A JACK control center

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/falkTX/Cadence
Source0:        https://github.com/falkTX/Cadence/archive/master.zip

BuildRequires: python3-qt4-devel
BuildRequires: qt-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-module-jack
BuildRequires: python3-dbus
BuildRequires: a2jmidid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: jack_capture

%description
A JACK control center

%prep
%setup -q -n Cadence-master

%build
make PREFIX=/usr DESTDIR=%{buildroot}

%install 
make PREFIX=/usr DESTDIR=%{buildroot} install

# Remove RPM_BUILD_ROOT from scripts
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_sysconfdir}/X11/xinit/xinitrc.d/21cadence-session-inject
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-session-start
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-logs
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/catia
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-render
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-pulse2jack
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/catarina
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/claudia-launcher
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-aloop-daemon
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/claudia
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-jacksettings
sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/cadence-pulse2loopback

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/
%{_datadir}/applications
%{_datadir}/cadence
%{_datadir}/icons
%{_sysconfdir}/

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - master
- Initial build
