# Global variables for github repository
%global commit0 4fb33f8c3754424ed325c1eb6806d8ae65c3b5a4
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           Carla
Version:        2.0.0
Release:        1%{?dist}
Summary:        A rack manager JACK

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/falkTX/Carla
Source0:        https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: python-qt5-devel
BuildRequires: python-magic
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fluidsynth-devel
BuildRequires: fftw-devel
BuildRequires: mxml-devel
BuildRequires: zlib-devel
BuildRequires: non-ntk-devel
BuildRequires: mesa-libGL-devel
#BuildRequires: linuxsampler-devel
#BuildRequires: libprojectM-devel

%description
A rack manager for JACK

%prep
%setup -qn %{name}-%{commit0}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=/usr/lib64 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=/usr/lib64  %{?_smp_mflags} install

# Remove RPM_BUILD_ROOT from scripts
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla-settings
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla-single
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla-database
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla-patchbay
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla-rack
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_bindir}/carla-control
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_libdir}/pkgconfig/carla-standalone.pc
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_libdir}/pkgconfig/carla-utils.pc
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_libdir}/carla/carla-bridge-lv2-modgui
#sed -i "s|${RPM_BUILD_ROOT}||g" %{buildroot}/%{_datadir}/carla/carla_shared.py
    
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
%{_includedir}/carla
%{_libdir}/carla
#%{_libdir}/debug
%{_libdir}/lv2
%{_libdir}/pkgconfig
%{_libdir}/python3
%{_libdir}/vst
%{_datadir}/applications
%{_datadir}/carla
%{_datadir}/icons
%{_datadir}/mime

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- Initial build
