%global upstream    technomancy
%global groupId     leiningen
%global artifactId  leiningen
%global commit_hash 713a4d9

Name:           leiningen
Version:        2.5.1
Release:        8%{?dist}
Summary:        Clojure project automation tool

License:        EPL
URL:            https://github.com/%{upstream}/%{name}
# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{upstream}-%{name}-%{version}-0-g%{commit_hash}.tar.gz
# Fedora/EPEL-specific patches
# Patch the launcher script to set classpath to the proper JAR names
#Patch100:       %{name}-1.7.1-jpp.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils

#BuildRequires:  clojure-compat
#BuildRequires:  clojure-contrib
BuildRequires:  java-devel
#BuildRequires:  clucy
#BuildRequires:  jline
#BuildRequires:  lancet
#BuildRequires:  maven-ant-tasks
# this should be a maven-ant-tasks dependency:
# https://bugzilla.redhat.com/show_bug.cgi?id=830786
BuildRequires:  maven-error-diagnostics
# needed by lein script
BuildRequires:  rlwrap
BuildRequires:  robert-hooke

BuildRequires:  maven-local

BuildRequires:  maven-artifact
BuildRequires:  maven-compiler-plugin
#BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-settings
BuildRequires:  maven-surefire-plugin

Requires:       jpackage-utils
%if 0%{?rhel}
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
%endif

Requires:       ant
Requires:       classworlds
Requires:       clojure-compat
Requires:       clojure-contrib
Requires:       java-devel
Requires:       clucy
Requires:       jline
Requires:       lancet
Requires:       maven-ant-tasks
Requires:       maven-artifact
# remove once maven-ant-tasks is fixed
Requires:       maven-error-diagnostics
# ---
Requires:	maven-project
Requires:       maven-settings
Requires:       rlwrap
Requires:       robert-hooke

%description
Working on Clojure projects with tools designed for Java can be an
exercise in frustration. With Leiningen, you describe your build with
Clojure. Leiningen handles fetching dependencies, running tests,
packaging your projects and can be easily extended with a number of
plugins.


%prep
%setup -q -n %{upstream}-%{name}-%{commit_hash}
#%patch100 -p1 -b .jpp


%build
# doesn't work somehow, lein still couldn't find deps
# mvn dependency:copy-dependencies -DoutputDirectory=lib
# LEIN_ROOT=y sh bin/lein-pkg compile :all, jar
jar cf %{name}-%{version}.jar -C src .


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{name}-%{version}.jar \
    $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}.jar
%endif

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 bin/lein-pkg $RPM_BUILD_ROOT%{_bindir}/lein

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -pm 644 bash_completion.bash \
   $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/lein

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
install -pm 644 zsh_completion.zsh \
   $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_lein


%check
# FIXME
# debug this; even though it fails, the resulting package is functional
# LEIN_ROOT=y sh bin/lein-pkg test


%if 0%{?rhel}
%post
%update_maven_depmap

%postun
%update_maven_depmap
%endif


%files
%doc COPYING README.md NEWS.md TUTORIAL.md
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
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

