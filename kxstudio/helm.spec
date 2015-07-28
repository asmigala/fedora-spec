# Global variables for github repository
%global commit0 86ee95743b4d698cfde08d0846313b79ac134153
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           helm
Version:        1.0.0
Release:        1%{?dist}
Summary:        A LV2 / standalone synth

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/mtytel/helm
Source0:        https://github.com/mtytel/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel

%description
A LV2 / standalone synth

%prep
%setup -qn %{name}-%{commit0}

sed -i "s/\/lib\//\/lib64\//g" Makefile

%build
make DESTDIR=%{buildroot} standalone lv2 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} standalone lv2 %{?_smp_mflags} install

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
%{_libdir}/lv2
%{_datadir}/helm

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
