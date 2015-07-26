Summary:          A multitrack tablature editor and player written in Java-SWT
Name:             tuxguitar
Version:          1.3
Release:          20%{?dist}
URL:              http://tuxguitar.sourceforge.com
Source0:          tuxguitar-1.3-SVN.zip
Source1:          tuxguitar-1.3.sh
License:          LGPLv2+
Group:            Applications/Multimedia

Requires:         itext-core
Requires:         java >= 1.7
Requires:         jpackage-utils
Requires:         eclipse-swt
Requires:         soundfont2-default
BuildRequires:    alsa-lib-devel
BuildRequires:    itext-core
BuildRequires:    desktop-file-utils
BuildRequires:    fluidsynth-devel
BuildRequires:    jack-audio-connection-kit-devel
BuildRequires:    java-devel >= 1.7
BuildRequires:    jpackage-utils
BuildRequires:    maven

BuildRequires:    eclipse-swt

%description
TuxGuitar is a guitar tablature editor with player support through midi. It can
display scores and multitrack tabs. Various features TuxGuitar provides include
autoscrolling while playing, note duration management, bend/slide/vibrato/
hammer-on/pull-off effects, support for tuplets, time signature management, 
tempo management, gp3/gp4/gp5/gp6 import and export.

%prep
%setup -q -n tuxguitar-1.3-SVN

%build

cd build-scripts/tuxguitar-linux-x86_64
mvn clean package -Dnative-modules=true
cd ../..

%install

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
install -m 755 -d %{buildroot}/%{_datadir}/appdata/
cat > %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/tuxguitar/support-requests/8/
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">tuxguitar.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A multitrack tablature editor and player</summary>
  <description>
  <p>
    Tuxguitar is a multitrack tablature editor and player.
    It provides the following features:
  </p>
  <ul>
    <li>Tablature editor</li>
    <li>Score Viewer</li>
    <li>Multitrack display</li>
    <li>Autoscroll while playing</li>
    <li>Note duration management</li>
    <li>Various effects (bend, slide, vibrato, hammer-on/pull-off)</li>
    <li>Support for triplets (5,6,7,9,10,11,12)</li>
    <li>Repeat open and close</li>
    <li>Time signature management</li>
    <li>Tempo management</li>
    <li>Imports and exports gp3,gp4,gp5 and gp6 files</li>
  </ul>
  </description>
  <url type="homepage">http://tuxguitar.sourceforge.com/</url>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/tuxguitar/screenshots/163395.jpg</screenshot>
  </screenshots>
</application>
EOF

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 misc/%{name}.desktop %{buildroot}%{_datadir}/applications/

%__install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
%__install -m 644 misc/%{name}.xml %{buildroot}%{_datadir}/mime/packages/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 misc/%{name}.xpm %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/
mv %{buildroot}/%{_bindir}/tuxguitar-1.3.sh %{buildroot}/%{_bindir}/tuxguitar

cd build-scripts/tuxguitar-linux-x86_64/target/tuxguitar-1.3-SNAPSHOT-linux-x86_64/

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/dist/
%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc/
%__install -m 755 -d %{buildroot}%{_libdir}/
%__install -m 755 -d %{buildroot}%{_javadir}/%{name}/

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/dist/
%__install -m 644 dist/* %{buildroot}/%{_datadir}/%{name}/dist/

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
%__install -m 644 doc/* %{buildroot}/%{_datadir}/%{name}/doc/

%__install -m 644 lib/*.so  %{buildroot}/%{_libdir}/
%__install -m 644 lib/*.jar %{buildroot}/%{_javadir}/%{name}/

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/css/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/images/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/images/edit
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/images/start
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/images/tools
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/lang/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/plugins/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/scales/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/skins/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/skins/blue_serious/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/skins/ersplus/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/skins/Lavender
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/skins/Oxygen/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/templates/

%__cp -r share/help/       %{buildroot}/%{_datadir}/%{name}/help/
%__cp -r share/lang/*      %{buildroot}/%{_datadir}/%{name}/lang/
%__cp -r share/plugins/*   %{buildroot}/%{_datadir}/%{name}/plugins/
%__cp -r share/scales/*    %{buildroot}/%{_datadir}/%{name}/scales/
%__cp -r share/skins/*     %{buildroot}/%{_datadir}/%{name}/skins/
%__cp -r share/templates/* %{buildroot}/%{_datadir}/%{name}/templates/

#chmod 555 %{buildroot}/%{_bindir}/
#chmod 555 %{buildroot}/%{_libdir}/

cd ../..

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-desktop-database &> /dev/null

%postun
if [ $1 -eq 0 ] ; then
   touch --no-create %{_datadir}/icons/hicolor &>/dev/null
   gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
   update-mime-database %{_datadir}/mime >& /dev/null ||:
fi
update-desktop-database &> /dev/null

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files
%{_libdir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_bindir}/%{name}
%{_javadir}/%{name}

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette dot nospam at free.fr> - 1.3-20
- Package version 1.3 SVN

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2-20
- Add an AppData file for the software center

* Mon Feb 02 2015 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-19
- Set SWT_GTK3=0 workaround for blank setting dialogs. RHBZ#1187848

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2-18
- update mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-15
- Unversioned docdir https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sun Aug 04 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-14
- Removed the BuildRequires: ant-nodeps as the virtual provides was removed from
  ant >= 1.9.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-12
- Changed swt.jar location specification RHBZ#923597

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-10
- Enabled the tuner plugin

* Sun Sep 23 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-9
- Disable cairo graphics to prevent garbled output on "Score Edition Mode" 
  RHBZ#827746,859734.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-7
- Require itext-core instead of itext to drop gcj dependency

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-5
- Remove gcj bits as per the new guidelines.
- Change Requires: libswt3-gtk2 to eclipse-swt

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 01 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-3
- Fix CVE-2010-3385 insecure library loading vulnerability - RHBZ#638396

* Sat Nov 28 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-2
- Change build system (we'll use our build-fedora.xml rather than patching Debian's
  Makefile). 
- Disable system tray and oss plugins by default.
- Make fluidsynth/alsa/fluid soundfont combination the default output so that the
  software works out of the box.

* Sat Nov 14 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-1
- New upstream version

* Wed Aug 05 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.1-3
- Update the .desktop file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 04 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.1-1
- New upstream version
- Clean-up the SPEC file
- Include GCJ-AOT-bits

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 15 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-8
- Enabled the PDF plugin since all the dependencies are now provided in repos

* Thu Oct 02 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-7
- Added "exec" to replace the called shell to java process in the launching script

* Wed Oct 01 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-6
- Required libswt3-gtk2 since rpmbuild doesn't pick it up.
- Some more cleanup in the spec file
- Fixed a typo regarding installation of icons
- Called update-desktop-database in %%post and %%postun
- jni files put in %%_libdir_/%%name.

* Mon Sep 29 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-5
- Compiled the package with openjdk instead of gcj.
- ExcludeArch'ed ppc/ppc64 on F-8.

* Sun Sep 28 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-4
- Added the comment about %%{?_smp_mflags}
- Used macros more extensively.
- Changed the license to LGPLv2+
- Fixed java requirement issue by requiring java >= 1.7
- Required jpackage-utils
- Removed pre-shipped binaries
- Fixed %%defattr

* Sun Sep 28 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-3
- Fixed java requirement issue by requiring icedtea for F-8 and openjdk for F-9+
- Patched the source to enable the fluidsynth plugin
- Added DistTag
- Patched the source in order to pass RPM_OPT_FLAGS to gcc
- Removed ExclusiveArch

* Thu Sep 25 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-2
- Added desktop-file-utils to BuildRequires.
- Replaced java-1.7.0-icedtea with java-1.6.0-openjdk in Requires.

* Wed Sep 24 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-1
- Initial build.
