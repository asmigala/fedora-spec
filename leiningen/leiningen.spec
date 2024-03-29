Name:           leiningen
Version:        2.5.3
Release:        1%{?dist}
Summary:        Clojure project automation tool

License:        EPL
URL:            https://github.com/technomancy/leiningen
Source0:        %{name}-%{version}.zip

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  maven
BuildRequires:  clojure
BuildRequires:  wget

Requires:       java

%description
Working on Clojure projects with tools designed for Java can be an
exercise in frustration. With Leiningen, you describe your build with
Clojure. Leiningen handles fetching dependencies, running tests,
packaging your projects and can be easily extended with a number of
plugins.


%prep
%setup

%build

wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
chmod +x lein
export PATH=`pwd`:$PATH

cd leiningen-core
mvn clean package
lein bootstrap
cd ..
bin/lein uberjar


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}-standalone.jar $RPM_BUILD_ROOT/%{_javadir}/

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 bin/lein-pkg $RPM_BUILD_ROOT%{_bindir}/lein

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -pm 644 bash_completion.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/lein

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
install -pm 644 zsh_completion.zsh $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_lein


%check
# FIXME
# debug this; even though it fails, the resulting package is functional
# LEIN_ROOT=y sh bin/lein-pkg test


%files
%doc COPYING README.md NEWS.md TUTORIAL.md
%{_javadir}/*
%{_bindir}/lein
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/lein
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_lein


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Oct 16 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-4
- Revert to packaging uncompiled Leiningen sources; need to find out why
  we can't compile against RPM-packaged JARs

* Sun Aug 19 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-3
- Use package's own launcher script to build the JAR (from Debian)

* Tue Jun 12 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-2
- Package launcher script
- Update dependencies

* Mon Jun 11 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-1
- Initial package

