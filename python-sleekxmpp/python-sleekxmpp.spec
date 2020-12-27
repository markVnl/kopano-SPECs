%define tarname sleekxmpp

Summary:	SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc)
Name:		python-%tarname
Version:	1.3.3
Release:	6.1%{?dist}
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/sleekxmpp/
Source0:        https://pypi.io/packages/source/s/sleekxmpp/%{tarname}-%{version}.tar.gz
Patch0:         sleekxmpp-1.3.3-rename-async-to-asynchronous.patch
Patch1:		https://github.com/fritzy/SleekXMPP/commit/597014ba5ca258763e96ee37729ac933c5af1602.patch#/pyasn1.patch
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:  python3-sphinx

%description
SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc).

%package -n python3-%tarname
Summary:	SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc)
Group:		Development/Python
%{?python_provide:%python_provide python3-%{tarname}}

%description -n python3-%tarname
SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc).

%prep
%autosetup -p1 -n %{tarname}-%{version}

# drop bundled egg-info
rm -rf sleekxmpp.egg-info/

# cleanup
find . -name '*.pyo' -o -name '*.pyc' -delete

%build
%py3_build

export PYTHONPATH=$(pwd)
%make_build SPHINXBUILD=sphinx-build-3 -C docs html
%__rm -rf docs/_build/html/.buildinfo

%install
%py3_install

%files -n python3-%tarname
%doc docs/_build/html
%{python3_sitelib}/*


%changelog
* Sun Dec 27 2020 Mark Verlinde <mark.verlinde@gmail.com> - 1.3.3-6.1
- Adapt to / Rebuild for el7 

* Sun Feb 16 2020 umeabot <umeabot> 1.3.3-6.mga8
+ Revision: 1532475
- Mageia 8 Mass Rebuild

* Mon Sep 16 2019 daviddavid <daviddavid> 1.3.3-5.mga8
+ Revision: 1442353
- rebuild for python3.8
- drop python2 support

* Sun Aug 25 2019 wally <wally> 1.3.3-4.mga8
+ Revision: 1431841
- add upstream patch for pyasn1
- update doc build

* Thu Jan 10 2019 kekepower <kekepower> 1.3.3-4.mga7
+ Revision: 1354612
- Created a better patch (thanks daviddavid)

* Thu Jan 10 2019 kekepower <kekepower> 1.3.3-3.mga7
+ Revision: 1354557
- Add patch to build with Python 3.7
- Rebuild for Python 3.7

* Thu Sep 20 2018 umeabot <umeabot> 1.3.3-2.mga7
+ Revision: 1290032
- Mageia 7 Mass Rebuild

* Wed May 02 2018 kekepower <kekepower> 1.3.3-1.mga7
+ Revision: 1224610
- Update to version 1.3.3
- Rename python-sleekxmpp to python2-sleekxmpp
- Use python_provide

* Sat Aug 05 2017 pterjan <pterjan> 1.3.1-2.mga7
+ Revision: 1135640
- Rebuild for python 3.6

* Tue Sep 27 2016 neoclust <neoclust> 1.3.1-1.mga6
+ Revision: 1057099
- imported package python-sleekxmpp

