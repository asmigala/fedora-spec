# Global variables for github repository
%global commit0 867ebc6897c236518315835018c72ce311511d5d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           mod-pitchshifter
Version:        0.9
Release:        1%{?dist}
Summary:        mod-pitchshifter LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/mod-pitchshifter
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: fftw
BuildRequires: python3
BuildRequires: python3-mpmath
BuildRequires: armadillo-devel

%description
mod-pitchshifter LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
