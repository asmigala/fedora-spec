Summary: Software Synthesizer
Name: drumgizmo
Version: 0.9.8.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL:            http://git.drumgizmo.org/drumgizmo.git
Source0:        drumgizmo-0.9.8.1.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: zita-resampler-devel
BuildRequires: expat-devel
BuildRequires: libpng-devel
BuildRequires: cppunit-devel
BuildRequires: libsmf-devel
BuildRequires: gettext-devel
BuildRequires: libxcb-devel
BuildRequires: mesa-libGLU-devel

%description
DrumGizmo is an open source cross-platform drum plugin and stand-alone application. It is comparable to several commercial drum plugin products. 

%prep
%setup -q -c %{name}

%build

./autogen.sh
%configure
%{__make} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# desktop file categories
BASE="X-PlanetCCRMA X-Fedora Application AudioVideo"
XTRA="X-Synthesis X-MIDI X-Jack"
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/drumgizmo
%{_libdir}/*
%{_datadir}/man/*


%changelog
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.9.8.1-1
- Initial release of spec fil to 0.9.8.1
