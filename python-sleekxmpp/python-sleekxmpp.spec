%global commit 08a0fd5420c25108d3bff4096a2378fd2f288a50
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# we do not build python3 for (centos) el7
%define with_py3 0

Name:		python-sleekxmpp
Version:	1.2.0
Release:	0.11.git%{shortcommit}%{?dist}
Summary:	Flexible XMPP client/component/server library for Python

License:	MIT
URL:		https://github.com/fritzy/SleekXMPP
Source0:    https://github.com/fritzy/SleekXMPP/archive/%{commit}/SleekXMPP-%{version}-%{shortcommit}.tar.gz
# Seems to have been fixed upstream in
#  https://github.com/fritzy/SleekXMPP/commit/a2423b849963887415b5b86e556ccda5f9ac2913#diff-446dd43bb3cb47383b2629c457abf504
Patch0:     python-sleekxmpp-fix-mixed-tabs-and-spaces.patch

BuildArch:	    noarch
BuildRequires:	python2-devel
%if %with_py3
BuildRequires:	python3-devel
%endif
# Required for some tests in %%check.
BuildRequires:  gnupg

Requires:	    python-dns
Requires:       python-pyasn1
Requires:       python-pyasn1-modules

%description
SleekXMPP is a flexible XMPP library for python that allows
you to create clients, components or servers for the XMPP protocol.
Plug-ins can be create to cover every current or future XEP.

%if %with_py3
%package -n python3-sleekxmpp
Summary:	Flexible XMPP client/component/server library for Python
Requires:	python3-dns

%description -n python3-sleekxmpp
SleekXMPP is a flexible XMPP library for python that allows
you to create clients, components or servers for the XMPP protocol.
Plug-ins can be create to cover every current or future XEP.
%endif

%prep
%setup -q -n SleekXMPP-%{commit}
%patch0 -p0
%if %with_py3
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build
%if %with_py3
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%if %with_py3
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%check
%{__python} testall.py
%if %with_py3
pushd %{py3dir}
%{__python3} testall.py
popd
%endif

%files
%doc LICENSE README.rst
%{python_sitelib}/sleekxmpp/
%{python_sitelib}/sleekxmpp-*.egg-info

%if %with_py3
%doc LICENSE README.rst
%files -n python3-sleekxmpp
%{python3_sitelib}/sleekxmpp/
%{python3_sitelib}/sleekxmpp-*.egg-info
%endif

%changelog
* Mon Jan 1 2018 mark.verlinde@gmail.com
- build only python2 for (centos) el7

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
