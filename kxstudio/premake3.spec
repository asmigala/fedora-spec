Summary:       Tool for describing builds
Name:          premake
Version:       3.7
Release:       1%{?dist}
License:       GPLv3+
Group:         Developpment
URL:           http://sourceforge.net/projects/premake/
Source0:       http://downloads.sourceforge.net/premake/premake-src-3.7.zip

%description
Describe your software project with a full-featured scripting language and let Premake write the build scripts for you. With one file your project can support both IDE-addicted Windows coders and Linux command-line junkies!

%prep
%setup -qn Premake-3.7

%build
make %{?_smp_mflags}

%install
%__install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/premake %{buildroot}/%{_bindir}/premake3

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES.txt LICENSE.txt README.txt
%{_bindir}/*

%changelog
* Fri Jun 19 2015 Yann Collette <ycollette.nospam@free.fr> - 3.7-1
- initial release
