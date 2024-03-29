# Disable production of debug package. Problem with fedora 23
#%global debug_package %{nil}

# Global variables for github repository
%global commit0 c02ef34407fb35b080de14f433dac90eefa018e9
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           picoloop
Version:        0.67
Release:        1%{?dist}
Summary:        An audio sequencer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/yoyz/audio
Source0:        https://github.com/yoyz/audio/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: pulseaudio-libs-devel

%description
Picoloop is a synth Stepsequencer (a nanoloop clone).
A pattern of 16 notes is played repeatedly while these notes can be edited in various respects like volume, pitch, filter, lfo etc.
All parameters are set step-wise, so you can make huge variation of sound on the same pattern.
There are four channels, playing simultaneously.

%prep
%setup -qn audio-%{commit0}


%build

cd picoloop

%make_build -f Makefile.RtMidi_debian clean
%make_build -f Makefile.RtAudio_debian clean
%make_build -f Makefile.PatternPlayer_debian_RtAudio clean

%make_build -f Makefile.RtMidi_debian  CFLAGS="-std=c++11 -O3 -Wall -I.. -DHAVE_GETTIMEOFDAY -D__LINUX_ALSA__ -D__LINUX_JACK__ -D__LINUX_PULSE__"
%make_build -f Makefile.RtAudio_debian CFLAGS="-std=c++11 -O3 -Wall -I.. -DHAVE_GETTIMEOFDAY -D__LINUX_ALSA__ -D__LINUX_JACK__ -D__LINUX_PULSE__"
%make_build -f Makefile.PatternPlayer_debian_RtAudio DIRTOCREATE
%make_build -f Makefile.PatternPlayer_debian_RtAudio CFLAGS="-c -std=c++11 -O3 -D__LINUX__ -DLINUX -I. -LSDL/lib -D__RTAUDIO__ -D __RTMIDI__ -DLINUX_DESKTOP -fpermissive" LDFLAGS="-lasound -lSDL -lSDL_ttf -lpthread -lpulse -lpulse-simple"

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=picoloop
Comment=Audio tracker
Exec=picoloop
Icon=picoloop
Terminal=false
Type=Application
Categories=Audio;
EOF

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 picoloop/PatternPlayer_debian_Rtaudio %{buildroot}%{_bindir}/%{name}

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/
%__install -m 644 picoloop/patch/MDADrum/create_patchlist.sh %{buildroot}%{_datadir}/%{name}/patch/MDADrum/
%__install -m 644 picoloop/patch/MDADrum/patchlist.cfg %{buildroot}%{_datadir}/%{name}/patch/MDADrum/

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_claps/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_synth/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_electro/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_fx/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_bass/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_perc/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/misc_hats/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Acoustic/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Electro/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Latin/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/tr808/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/cr78/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Farfisa/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Linn/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/tr909/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/cr8000/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Ferraro/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/magnetboy/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/R_B/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/instrmnt/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/tr606/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/Effects/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/JergenSohn/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/patch/MDADrum/tr77/

%__install -m 644 picoloop/patch/MDADrum/Acoustic/*     %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Acoustic/
%__install -m 644 picoloop/patch/MDADrum/Electro/*      %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Electro/
%__install -m 644 picoloop/patch/MDADrum/Latin/*        %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Latin/
%__install -m 644 picoloop/patch/MDADrum/misc_claps/*   %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_claps/
%__install -m 644 picoloop/patch/MDADrum/misc_synth/*   %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_synth/
%__install -m 644 picoloop/patch/MDADrum/tr808/*        %{buildroot}%{_datadir}/%{name}/patch/MDADrum/tr808/
%__install -m 644 picoloop/patch/MDADrum/cr78/*         %{buildroot}%{_datadir}/%{name}/patch/MDADrum/cr78/
%__install -m 644 picoloop/patch/MDADrum/Farfisa/*      %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Farfisa/
%__install -m 644 picoloop/patch/MDADrum/Linn/*         %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Linn/
%__install -m 644 picoloop/patch/MDADrum/misc_electro/* %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_electro/
%__install -m 644 picoloop/patch/MDADrum/tr909/*        %{buildroot}%{_datadir}/%{name}/patch/MDADrum/tr909/
%__install -m 644 picoloop/patch/MDADrum/cr8000/*       %{buildroot}%{_datadir}/%{name}/patch/MDADrum/cr8000/
%__install -m 644 picoloop/patch/MDADrum/Ferraro/*      %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Ferraro/
%__install -m 644 picoloop/patch/MDADrum/magnetboy/*    %{buildroot}%{_datadir}/%{name}/patch/MDADrum/magnetboy/
%__install -m 644 picoloop/patch/MDADrum/misc_fx/*      %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_fx/
%__install -m 644 picoloop/patch/MDADrum/R_B/*          %{buildroot}%{_datadir}/%{name}/patch/MDADrum/R_B/
%__install -m 644 picoloop/patch/MDADrum/instrmnt/*     %{buildroot}%{_datadir}/%{name}/patch/MDADrum/instrmnt/
%__install -m 644 picoloop/patch/MDADrum/misc/*         %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc/
%__install -m 644 picoloop/patch/MDADrum/misc_hats/*    %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_hats/
%__install -m 644 picoloop/patch/MDADrum/tr606/*        %{buildroot}%{_datadir}/%{name}/patch/MDADrum/tr606/
%__install -m 644 picoloop/patch/MDADrum/Effects/*      %{buildroot}%{_datadir}/%{name}/patch/MDADrum/Effects/
%__install -m 644 picoloop/patch/MDADrum/JergenSohn/*   %{buildroot}%{_datadir}/%{name}/patch/MDADrum/JergenSohn/
%__install -m 644 picoloop/patch/MDADrum/misc_bass/*    %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_bass/
%__install -m 644 picoloop/patch/MDADrum/misc_perc/*    %{buildroot}%{_datadir}/%{name}/patch/MDADrum/misc_perc/
%__install -m 644 picoloop/patch/MDADrum/tr77/*         %{buildroot}%{_datadir}/%{name}/patch/MDADrum/tr77/

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/documentation/filter/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/documentation/gp2x/

%__install -m 644 picoloop/documentation/filter/* %{buildroot}%{_datadir}/%{name}/documentation/filter/
%__install -m 644 picoloop/documentation/gp2x/*   %{buildroot}%{_datadir}/%{name}/documentation/gp2x/

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.67
- Initial build
