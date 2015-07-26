Summary: Additional DrumKits for Hydrogen
Name: hydrogen-drumkits
Version: 0.9.3
Release: 4.20080907%{?dist}
License: GPLv2+ and GPLv3 and Green OpenMusic
Group: Applications/Multimedia
URL: http://www.hydrogen-music.org
Source0: http://downloads.sourceforge.net/hydrogen/Classic-626.h2drumkit
Source1: http://downloads.sourceforge.net/hydrogen/Classic-808.h2drumkit
Source2: http://downloads.sourceforge.net/hydrogen/ColomboAcousticDrumkit.h2drumkit
Source3: http://downloads.sourceforge.net/hydrogen/ElectricEmpireKit.h2drumkit
Source4: http://downloads.sourceforge.net/hydrogen/HardElectro1.h2drumkit
Source5: http://downloads.sourceforge.net/hydrogen/K-27_Trash_Kit.h2drumkit
Source6: http://downloads.sourceforge.net/hydrogen/Millo-Drums_v.1.h2drumkit
Source7: http://downloads.sourceforge.net/hydrogen/Millo_MultiLayered2.h2drumkit
Source8: http://downloads.sourceforge.net/hydrogen/Millo_MultiLayered3.h2drumkit
Source9: http://downloads.sourceforge.net/hydrogen/VariBreaks.h2drumkit

# URL: http://www.ardaeden.net/asma_davul/
Source10: http://www.ardaeden.net/asma_davul/files/asma_davul.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: hydrogen >= 0.9.3

%description
A collection of additional drumkits for the 
Hydrogen advanced drum machine for GNU/Linux.

%prep
%setup -q -c -n %{name} -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10
# Rename the doc files to avoid confusion:
for licencedir in Classic-626 Classic-808 \
    ElectricEmpireKit HardElectro1 Millo-Drums_v.1 \
    Millo_MultiLayered2 Millo_MultiLayered3 ; do
  mv $licencedir/LICENCE LICENCE.$licencedir
done

mv asma_davul/GPLv.3 license.asma_davul

mv ColomboAcousticDrumkit/COPYING COPYING.ColomboAcousticDrumkit
mv ColomboAcousticDrumkit/README README.ColomboAcousticDrumkit
iconv -f iso-8859-1 -t utf8 README.ColomboAcousticDrumkit \
                         -o README.tmp
touch -r README.ColomboAcousticDrumkit README.tmp
mv -f README.tmp README.ColomboAcousticDrumkit

mv K-27_Trash_Kit/license.html license.K-27_Trash_Kit.html

# The demo songs need to be separated from drumkits:
find . -name *.h2song -exec mv {} . \;

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT

# These directories are owned by hydrogen:
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs

# Now copy everything into the $RPM_BUILD_ROOT
for drumkitdir in asma_davul Classic-626 Classic-808 \
                  ColomboAcousticDrumkit ElectricEmpireKit \
                  HardElectro1 K-27_Trash_Kit \
                  Millo-Drums_v.1 Millo_MultiLayered2 \
                  Millo_MultiLayered3 VariBreaks ; do
  cp -a $drumkitdir  $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
done

find . -name *.h2song -exec cp -a {} $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING.* LICENCE.* license.* README.*
%{_datadir}/hydrogen/data/demo_songs/*
%{_datadir}/hydrogen/data/drumkits/*

%changelog
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4.20080907
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3.20080907
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2.20080907
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT} com> 0.9.3-1.20080907
- Change versioning
- Some cosmetics on the SPEC file
- Added Asma Davul (GPLv3) to the drumkits

* Fri Nov 07 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT} com> 0-0.20080907.4
- Preserve the timestamp of README.ColomboAcousticDrumkit

* Sun Nov 06 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT} com> 0-0.20080907.3
- Updated sources

* Sun Nov 02 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT} com> 0-0.20080907.2
- Fixed the license

* Wed Oct 22 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT} com> 0-0.20080907.1
- Initial build
