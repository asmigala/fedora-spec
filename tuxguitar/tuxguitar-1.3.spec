# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Summary:          A multitrack tablature editor and player written in Java-SWT
Name:             tuxguitar3
Version:          1.3.1
Release:          1%{?dist}

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 1427 http://svn.code.sf.net/p/tuxguitar/code/trunk tuxguitar-1.3-1427
#  tar -czvf tuxguitar-1.3-1427.tar.gz tuxguitar-1.3-1427
URL:              http://tuxguitar.sourceforge.com
Source0:          tuxguitar-1.3-1427.tar.gz
Source1:          tuxguitar-1.3.sh
Source2:          tuxguitar3.desktop
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
%setup -q -n tuxguitar-1.3-1427

%build

cd build-scripts/tuxguitar-linux-x86_64

mvn clean package -Dnative-modules=true \
    -Dtuxguitar-alsa.jni.cflags="-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -O2 -fPIC" \
    -Dtuxguitar-jack.jni.cflags="-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -O2 -fPIC" \
    -Dtuxguitar-fluidsynth.jni.cflags="-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -O2 -fPIC" \
    -Dtuxguitar-oss.jni.cflags="-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -O2 -fPIC"

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
#%__install -m 644 misc/tuxguitar.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
%__install -m 644 misc/tuxguitar.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 misc/tuxguitar.xpm %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/
mv %{buildroot}/%{_bindir}/tuxguitar-1.3.sh %{buildroot}/%{_bindir}/%{name}

cd build-scripts/tuxguitar-linux-x86_64/target/tuxguitar-%{version}-SNAPSHOT-linux-x86_64/

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

# Under FC22, the java sound plugin make tuxguitar freezes.
%__rm share/plugins/tuxguitar-jsa.jar

%__cp -r share/help/*      %{buildroot}/%{_datadir}/%{name}/help/
%__cp -r share/lang/*      %{buildroot}/%{_datadir}/%{name}/lang/
%__cp -r share/plugins/*   %{buildroot}/%{_datadir}/%{name}/plugins/
%__cp -r share/scales/*    %{buildroot}/%{_datadir}/%{name}/scales/
%__cp -r share/skins/*     %{buildroot}/%{_datadir}/%{name}/skins/
%__cp -r share/templates/* %{buildroot}/%{_datadir}/%{name}/templates/

cd ../..

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-desktop-database &> /dev/null

%postun
if [ $1 -eq 0 ] ; then
   touch --no-create     %{_datadir}/icons/hicolor &>/dev/null
   gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
   update-mime-database  %{_datadir}/mime >& /dev/null ||:
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
