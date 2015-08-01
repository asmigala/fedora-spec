Summary:       alsa / jack midi bridge
Name:          zita-ajbridge
Version:       0.4.0
Release:       1%{?dist}
License:       GPLv3+
Group:          Applications/Multimedia
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-alsa-pcmi-devel

%description
%{name} alsa / jack midi bridge.

%prep
%setup -q

# Preserve timestamps
sed -i 's|install |install -p |' source/Makefile

%build
cd source
make PREFIX=%{_prefix} %{?_smp_mflags}
cd ..

%install
cd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_lib}  %{?_smp_mflags} install
cd ..

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/

%changelog
* Fri Jun 19 2015 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- initial release

