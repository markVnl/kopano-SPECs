%global srcname sleekxmpp

Name:           python-%{srcname}
Version:        1.3.2
Release:        4.1%{?dist}
Summary:        Flexible XMPP client/component/server library for Python

License:        MIT
URL:            https://github.com/fritzy/SleekXMPP
Source0:        https://github.com/fritzy/SleekXMPP/archive/sleek-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python2-devel
BuildRequires:	python3-devel
# Required for some tests in %%check.
BuildRequires:  gnupg

%description
SleekXMPP is a flexible XMPP library for python that allows you to
create clients, components or servers for the XMPP protocol. Plug-ins
can be create to cover every current or future XEP.

%package -n python2-%{srcname}
Summary:        %{summary}
Requires:	python2-dns
Requires:       python2-pyasn1
Requires:       python2-pyasn1-modules
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
SleekXMPP is a flexible XMPP library for python that allows you to
create clients, components or servers for the XMPP protocol. Plug-ins
can be create to cover every current or future XEP.

%package -n python3-%{srcname}
Summary:        %{sum}
%if 0%{?rhel} == 7
Requires:	python36-dns
%else 
Requires:	python3-dns
%endif
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
SleekXMPP is a flexible XMPP library for python that allows you to
create clients, components or servers for the XMPP protocol. Plug-ins
can be create to cover every current or future XEP.

%prep
%setup -q -n SleekXMPP-sleek-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} testall.py
%{__python3} testall.py

%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{srcname}/
%{python_sitelib}/sleekxmpp-*.egg-info

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/sleekxmpp-*.egg-info

%changelog
* Fri Sep 06 2019 Mark Verlinde <mark.verlinde@gmail.com> - 1.3.2-4.1
- adapt to el7 (centos) build: python36-dns lives in epel

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Update to latest upstream release 1.3.2 to fix CVE-2017-5591 (rhbz#1421077)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuild for Python 3.6

* Mon Nov 21 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Update spec file
- Update to latest upstream release 1.3.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.11.git08a0fd5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.10.git08a0fd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.9.git08a0fd5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.8.git08a0fd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.7.git08a0fd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-0.6.git08a0fd5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Oct 27 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 1.2.0-0.5.git08a0fd5
- Update to latest revision

* Tue Aug 06 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 1.2.0-0.4.git6401c9a
- Update to latest revision

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.3.gitcedc9dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 01 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 1.2.0-0.2.gitcedc9dd
- Update to latest revision

* Wed Jun 05 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 1.2.0-0.1.gitda6b549
- Remove obsolete Group tag in spec file
- Remove obsolete BuildRoot tag in spec file
- Remove obsolete cleanup command at the beginning of %%install section in spec file
- Remove obsolete %%clean section in spec file
- Remove obsolete %%defattr line in %%files sections
- Use latest commit of upstream git in Source
- Update %%setup command in spec file

* Sun Mar 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.11-2
- add python-pyasn1 and python-pyasn1-modules to Requires

* Sat Feb 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.11-1
- update to upstream release 1.1.11
- add python3-dns to BuildRequires for python3-sleekxmpp subpackage

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.0-0.11.beta2
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 8 2011 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.7.beta2
- We do not need the link

* Sat Jan 8 2011 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.6.beta2
- Fixe source0 again

* Mon Nov 15 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.5.beta2
- Fixe source0

* Thu Nov 11 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.4.beta2
- Fixed some issues reported in review (rhbz 651227)

* Wed Nov 10 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.3.beta2
- Added the execution of tests
- Use a better way to build the python3 subpackage

* Tue Oct 26 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.2.beta2
- Update sources to beta2

* Fri Oct 22 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-0.1.beta1
- Create .spec file from scratch
