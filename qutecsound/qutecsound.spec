Name:         qutecsound
Version:      0.9.0
Release:      1%{?dist}
Summary:      A csound file editor
URL:          http://qutecsound.sourceforge.net/
Group:        Applications/Multimedia

License:      GPLv2+

Source0:      %{name}-%{version}.tar.gz
Source1:      qutecsound.desktop
Source2:      qutecsound.xml

BuildRequires: qt4-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: csound-devel
BuildRequires: csound-manual

%description
CsoundQt is a frontend for Csound featuring a highlighting editor with autocomplete, interactive widgets and integrated help. It is a cross-platform and aims to be a simple yet powerful and complete development environment for Csound. It can open files created by MacCsound. Csound is a musical programming language with a very long history, with roots in the origins of computer music. It is still being maintained by an active community and despite its age, is still one of the most powerful tools for sound processing and synthesis. CsoundQt hopes to bring the power of Csound to a larger group of people, by reducing Csound''s intial learning curve, and by giving users more immediate control of their sound. It hopes to be both a simple tool for the beginner, as well as a powerful tool for experienced users.

%prep
%setup0 -q

%build

# BUILD OPTIONS:
# CONFIG+=build32    To build floats version
# CONFIG+=pythonqt   To build with PythonQt support
# CONFIG+=rtmidi     To build with RtMidi support
# CONFIG+=record_support
# CONFIG+=debugger
# CONFIG+=html5      To support HTML5 via the <CsHtml5> element in the csd file.
# CSOUND_INCLUDE_DIR
# CSOUND_LIBRARY_DIR

qmake-qt4 CSOUND_LIBRARY_DIR=/usr/%{_lib} qcs.pro
make VERBOSE=1 %{?_smp_mflags}
cd ..

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 bin/CsoundQt-d-cs6 %{buildroot}%{_bindir}/%{name}

%__install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
%__install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/templates
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples

%__install -m 644 templates/* %{buildroot}%{_datadir}/%{name}/templates/
%__install -m 644 doc/*       %{buildroot}%{_datadir}/%{name}/doc/
%__cp      -r     examples/*  %{buildroot}%{_datadir}/%{name}/examples/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 images/qtcs.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install qutecsound.desktop properly.
desktop-file-install --vendor '' \
        --add-category X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi


%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files
%doc ChangeLog BUILDING COPYING
%{_bindir}/qutecsound
%{_datadir}/applications/qutecsound.desktop
%{_datadir}/mime/packages/qutecsound.xml
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/*


%changelog
* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- Initial spec file 1.6.0
