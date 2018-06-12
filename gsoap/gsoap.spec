Summary: Generator Tools for Coding SOAP/XML Web Services in C and C++
Name: gsoap
Version: 2.8.60
Release: 3%{?dist}

# gsoap is licensed both under the gSOAP public license and under GPL version
# 2 or later with an OpenSSL linking exception.
#
# The gSOAP public license is a modified version of the Mozilla Public License.
# Due to the modifications, the gSOAP public license is non-free. You can not
# use gsoap under this license for software that you intend to contribute to
# fedora. If you use gsoap in fedora you must use it under the GPL license,
# possibly using the OpenSSL linking exception. The specific modification that
# makes the license non-free is in section 3.2:
#
# 3.2. Availability of Source Code.
# Any Modification created by You will be provided to the Initial Developer in
# Source Code form and are subject to the terms of the License.
License: GPLv2+ with exceptions
URL: http://gsoap2.sourceforge.net/
Source0: http://downloads.sourceforge.net/gsoap2/%{name}_%{version}.zip
Source1: soapcpp2.1
Source2: wsdl2h.1
# Create shared libraries
Patch0: %{name}-libtool.patch
# Missing include of <signal.h> in gsoap/samples/testmsgr/testmsgr.cpp
# https://sourceforge.net/p/gsoap2/bugs/1183/
Patch1: %{name}-header.patch
# Restore broken -c and -s modes in wsdl2h
# https://sourceforge.net/p/gsoap2/bugs/1191/
Patch2: %{name}-size-aname.patch

BuildRequires: flex
BuildRequires: bison
BuildRequires: dos2unix
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

Requires: openssl
Obsoletes: %{name}-examples < 2.8.3

%description
The gSOAP Web services development toolkit offers an XML to C/C++
language binding to ease the development of SOAP/XML Web services in C
and C/C++.

%package devel
Summary: Devel libraries and headers for linking with gSOAP generated stubs
Requires: %name = %version-%release

%description devel
gSOAP libraries, headers and generators for linking with and creating
gSOAP generated stubs.

%package doc
Summary: Documentation for gSOAP
BuildArch: noarch

%description doc
gSOAP documentation in html.

%prep
%setup -q -n gsoap-2.8
%patch0 -p1
%patch1 -p1
%patch2 -p1

# XML files non-executable
find gsoap/samples/autotest/databinding/examples -name '*.xml' \
    -exec chmod a-x {} ';'

# Documentation fonts non-executable
chmod a-x gsoap/doc/fonts/*

# we want all txt files to have unix end-of-line encoding
dos2unix -k README.txt LICENSE.txt NOTES.txt GPLv2_license.txt

# remove stuff with gsoap license only - not GPL
rm -rf gsoap/extras gsoap/mod_gsoap gsoap/Symbian
sed 's!$(top_srcdir)/gsoap/extras/\*!!' -i gsoap/Makefile.am

# remove pre-compiled binaries
rm -rf gsoap/bin
rm gsoap/samples/calc_vs2005/calc_vs2005/soapcpp2.exe
rm gsoap/samples/rest/person
rm gsoap/VisualStudio2005/wsdl2h/wsdl2h/soapcpp2.exe
( cd gsoap/samples/link++ ; make distclean )
( cd gsoap/samples/wcf/Basic/TransportSecurity ; make distclean )

%build
# patches change autoconf and automake files, so we must reconfigure
autoreconf --install --force

# the libraries deliberately leave some symbols undefined
LDFLAGS=$(sed 's!-Wl,-z,defs!!' <<< "%{__global_ldflags}")
%configure --disable-static --prefix=/usr --enable-ipv6 --enable-samples

# dependencies are not declared properly
#make %{?_smp_mflags}
make

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%_libdir/*.la

mkdir -p %{buildroot}/%_mandir/man1
install -m 644 -p %{SOURCE1} %{SOURCE2} %{buildroot}/%_mandir/man1

%check
make check

%files
%doc README.txt NOTES.txt
%license LICENSE.txt GPLv2_license.txt
%_libdir/libgsoap-*.so
%_libdir/libgsoap++-*.so
%_libdir/libgsoapck-*.so
%_libdir/libgsoapck++-*.so
%_libdir/libgsoapssl-*.so
%_libdir/libgsoapssl++-*.so

%files devel
%_bindir/soapcpp2
%_bindir/wsdl2h
%_mandir/man1/soapcpp2.1*
%_mandir/man1/wsdl2h.1*
%_libdir/libgsoap.so
%_libdir/libgsoap++.so
%_libdir/libgsoapck.so
%_libdir/libgsoapck++.so
%_libdir/libgsoapssl.so
%_libdir/libgsoapssl++.so
%_includedir/stdsoap2.h
%dir %_datadir/gsoap
%dir %_datadir/gsoap/import
%_datadir/gsoap/import/c14n.h
%_datadir/gsoap/import/dom.h
%_datadir/gsoap/import/ds2.h
%_datadir/gsoap/import/ds.h
%_datadir/gsoap/import/README.txt
%_datadir/gsoap/import/soap12.h
%_datadir/gsoap/import/stldeque.h
%_datadir/gsoap/import/stl.h
%_datadir/gsoap/import/stllist.h
%_datadir/gsoap/import/stlset.h
%_datadir/gsoap/import/stlvector.h
%_datadir/gsoap/import/wsa3.h
%_datadir/gsoap/import/wsa4.h
%_datadir/gsoap/import/wsa5.h
%_datadir/gsoap/import/wsa.h
%_datadir/gsoap/import/WS-example.c
%_datadir/gsoap/import/WS-example.h
%_datadir/gsoap/import/WS-Header.h
%_datadir/gsoap/import/wsp.h
%_datadir/gsoap/import/wsrp.h
%_datadir/gsoap/import/wsse2.h
%_datadir/gsoap/import/wsse.h
%_datadir/gsoap/import/wsu.h
%_datadir/gsoap/import/xlink.h
%_datadir/gsoap/import/xmime4.h
%_datadir/gsoap/import/xmime5.h
%_datadir/gsoap/import/xmime.h
%_datadir/gsoap/import/xml.h
%_datadir/gsoap/import/xmlmime5.h
%_datadir/gsoap/import/xmlmime.h
%_datadir/gsoap/import/xop.h
%dir %_datadir/gsoap/WS
%_datadir/gsoap/WS/README.txt
%_datadir/gsoap/WS/WS-Addressing.xsd
%_datadir/gsoap/WS/WS-Addressing03.xsd
%_datadir/gsoap/WS/WS-Addressing04.xsd
%_datadir/gsoap/WS/WS-Addressing05.xsd
%_datadir/gsoap/WS/WS-Discovery.wsdl
%_datadir/gsoap/WS/WS-Enumeration.wsdl
%_datadir/gsoap/WS/WS-Policy.xsd
%_datadir/gsoap/WS/WS-Routing.xsd
%_datadir/gsoap/WS/WS-typemap.dat
%_datadir/gsoap/WS/discovery.xsd
%_datadir/gsoap/WS/ds.xsd
%_datadir/gsoap/WS/enumeration.xsd
%_datadir/gsoap/WS/typemap.dat
%_datadir/gsoap/WS/wsse.xsd
%_datadir/gsoap/WS/wsu.xsd
%dir %_datadir/gsoap/custom
%_datadir/gsoap/custom/README.txt
%_datadir/gsoap/custom/long_double.c
%_datadir/gsoap/custom/long_double.h
%_datadir/gsoap/custom/struct_timeval.c
%_datadir/gsoap/custom/struct_timeval.h
%_datadir/gsoap/custom/struct_tm.c
%_datadir/gsoap/custom/struct_tm.h
%dir %_datadir/gsoap/plugin
%_datadir/gsoap/plugin/README.txt
%_datadir/gsoap/plugin/cacerts.c
%_datadir/gsoap/plugin/cacerts.h
%_datadir/gsoap/plugin/httpda.c
%_datadir/gsoap/plugin/httpda.h
%_datadir/gsoap/plugin/httpdatest.c
%_datadir/gsoap/plugin/httpdatest.h
%_datadir/gsoap/plugin/httpform.c
%_datadir/gsoap/plugin/httpform.h
%_datadir/gsoap/plugin/httpget.c
%_datadir/gsoap/plugin/httpget.h
%_datadir/gsoap/plugin/httpgettest.c
%_datadir/gsoap/plugin/httpgettest.h
%_datadir/gsoap/plugin/httpmd5.c
%_datadir/gsoap/plugin/httpmd5.h
%_datadir/gsoap/plugin/httpmd5test.c
%_datadir/gsoap/plugin/httpmd5test.h
%_datadir/gsoap/plugin/httppost.c
%_datadir/gsoap/plugin/httppost.h
%_datadir/gsoap/plugin/logging.c
%_datadir/gsoap/plugin/logging.h
%_datadir/gsoap/plugin/md5evp.c
%_datadir/gsoap/plugin/md5evp.h
%_datadir/gsoap/plugin/plugin.c
%_datadir/gsoap/plugin/plugin.h
%_datadir/gsoap/plugin/smdevp.c
%_datadir/gsoap/plugin/smdevp.h
%_datadir/gsoap/plugin/threads.c
%_datadir/gsoap/plugin/threads.h
%_datadir/gsoap/plugin/wsaapi.c
%_datadir/gsoap/plugin/wsaapi.h
%_datadir/gsoap/plugin/wsse2api.c
%_datadir/gsoap/plugin/wsse2api.h
%_datadir/gsoap/plugin/wsseapi.c
%_datadir/gsoap/plugin/wsseapi.h
%_libdir/pkgconfig/gsoapck.pc
%_libdir/pkgconfig/gsoapck++.pc
%_libdir/pkgconfig/gsoap.pc
%_libdir/pkgconfig/gsoap++.pc
%_libdir/pkgconfig/gsoapssl.pc
%_libdir/pkgconfig/gsoapssl++.pc
# Additions in 2.7.12-1
%_datadir/gsoap/WS/WS-ReliableMessaging.wsdl
%_datadir/gsoap/WS/WS-ReliableMessaging.xsd
%_datadir/gsoap/WS/reference-1.1.xsd
%_datadir/gsoap/WS/ws-reliability-1.1.xsd
%_datadir/gsoap/import/ref.h
%_datadir/gsoap/import/wsrm.h
%_datadir/gsoap/import/wsrm4.h
%_datadir/gsoap/import/wsrx.h
# Additions in 2.7.13-1
%_datadir/gsoap/import/stdstring.h
%_datadir/gsoap/import/xsd.h
%_datadir/gsoap/plugin/wsseapi.cpp
# Additions in 2.7.16-1
%_datadir/gsoap/custom/duration.c
%_datadir/gsoap/custom/duration.h
%_datadir/gsoap/plugin/httpposttest.c
%_datadir/gsoap/plugin/httpposttest.h
%_datadir/gsoap/plugin/wsrmapi.c
%_datadir/gsoap/plugin/wsrmapi.h
# Additions in 2.7.17-1
%_datadir/gsoap/WS/WS-Policy12.xsd
%_datadir/gsoap/WS/WS-SecurityPolicy.xsd
%_datadir/gsoap/import/wsse11.h
# Additions in 2.8.3-1
%_datadir/gsoap/WS/xenc.xsd
%_datadir/gsoap/import/xenc.h
%_datadir/gsoap/plugin/mecevp.c
%_datadir/gsoap/plugin/mecevp.h
# Additions in 2.8.4-1
%_datadir/gsoap/import/wsdd.h
%_datadir/gsoap/import/wsdx.h
%_datadir/gsoap/plugin/wsddapi.c
%_datadir/gsoap/plugin/wsddapi.h
# Additions in 2.8.7-1
%_datadir/gsoap/import/wsdd10.h
# Additions in 2.8.12-1
%_datadir/gsoap/WS/WS-SecureConversation.xsd
%_datadir/gsoap/WS/WS-Trust.wsdl
%_datadir/gsoap/WS/WS-Trust.xsd
%_datadir/gsoap/import/ser.h
%_datadir/gsoap/import/wsc.h
%_datadir/gsoap/import/wsrm5.h
%_datadir/gsoap/import/wsrx5.h
%_datadir/gsoap/import/wst.h
%_datadir/gsoap/import/wstx.h
# Additions in 2.8.16-1
%_datadir/gsoap/import/wsc2.h
%_datadir/gsoap/plugin/calcrest.h
# Additions in 2.8.17-1
%_datadir/gsoap/plugin/mq.c
%_datadir/gsoap/plugin/mq.h
# Additions in 2.8.21-1
%_datadir/gsoap/WS/LEGAL.txt
%_datadir/gsoap/WS/ws-bpel_abstract_common_base.xsd
%_datadir/gsoap/WS/ws-bpel_executable.xsd
%_datadir/gsoap/WS/ws-bpel_plnktype.xsd
%_datadir/gsoap/WS/ws-bpel_serviceref.xsd
%_datadir/gsoap/WS/ws-bpel_varprop.xsd
%_datadir/gsoap/import/plnk.h
%_datadir/gsoap/import/vprop.h
# Additions in 2.8.22-1
%_datadir/gsoap/import/wsdd5.h
%_datadir/gsoap/plugin/wsseapi-lite.c
%_datadir/gsoap/plugin/wsseapi-lite.h
# Additions in 2.8.28-1
%_datadir/gsoap/WS/oasis-sstc-saml-schema-assertion-1.1.xsd
%_datadir/gsoap/WS/saml-schema-assertion-2.0.xsd
%_datadir/gsoap/custom/chrono_duration.cpp
%_datadir/gsoap/custom/chrono_duration.h
%_datadir/gsoap/custom/chrono_time_point.cpp
%_datadir/gsoap/custom/chrono_time_point.h
%_datadir/gsoap/custom/float128.c
%_datadir/gsoap/custom/float128.h
%_datadir/gsoap/custom/int128.c
%_datadir/gsoap/custom/int128.h
%_datadir/gsoap/custom/long_time.c
%_datadir/gsoap/custom/long_time.h
%_datadir/gsoap/custom/struct_tm_date.c
%_datadir/gsoap/custom/struct_tm_date.h
%_datadir/gsoap/import/saml1.h
%_datadir/gsoap/import/saml2.h
# Additions in 2.8.35-1
%_datadir/gsoap/custom/qbytearray_base64.cpp
%_datadir/gsoap/custom/qbytearray_base64.h
%_datadir/gsoap/custom/qbytearray_hex.cpp
%_datadir/gsoap/custom/qbytearray_hex.h
%_datadir/gsoap/custom/qdate.cpp
%_datadir/gsoap/custom/qdate.h
%_datadir/gsoap/custom/qdatetime.cpp
%_datadir/gsoap/custom/qdatetime.h
%_datadir/gsoap/custom/qstring.cpp
%_datadir/gsoap/custom/qstring.h
%_datadir/gsoap/custom/qtime.cpp
%_datadir/gsoap/custom/qtime.h
%_datadir/gsoap/import/wsp_appliesto.h
%_datadir/gsoap/import/xenc2.h
%_datadir/gsoap/plugin/sessions.c
%_datadir/gsoap/plugin/sessions.h
%_datadir/gsoap/plugin/wstapi.c
%_datadir/gsoap/plugin/wstapi.h
# Additions in 2.8.48-1
%_datadir/gsoap/plugin/curlapi.c
%_datadir/gsoap/plugin/curlapi.h

%files doc
%doc README.txt NOTES.txt gsoap/doc/[^R]*
%license LICENSE.txt GPLv2_license.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.60-2
- Restore broken -c and -s modes in wsdl2h

* Wed Jan 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.60-1
- Update to gsoap 2.8.60

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.49-1
- Update to gsoap 2.8.49
- Drop patch gsoap-xlocale.patch (accepted upstream)

* Fri Jul 07 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.48-3
- Update patch based on upstream's feedback

* Mon Jul 03 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.48-2
- Don't include xlocale.h

* Tue Jun 20 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.48-1
- Update to gsoap 2.8.48
- Use -release instead of -version-info to set soname of shared libraries

* Mon Feb 06 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.43-1
- Update to gsoap 2.8.43
- Drop patches gsoap-backport.patch and gsoap-openssl110.patch

* Sat Oct 15 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.35-3
- Rebuild for openssl 1.1.0 (Fedora 26)

* Mon Sep 26 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.35-2
- Backport fix from upstream

* Mon Sep 19 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8.35-1
- Update to gsoap 2.8.35
- Add fixes for OpenSSL 1.1.0

* Mon Apr 18 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.30-1
- Update to gsoap 2.8.30
- Drop patch fixed upstream: gsoap-aliasing.patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.28-1
- Update to gsoap 2.8.28
- Drop patch fixed upstream: gsoap-missing-terminating-quote.patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.22-1
- Update to gsoap 2.8.22

* Tue Jan 06 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.21-1
- Update to gsoap 2.8.21
- Drop patches fixed upstream: gsoap-private-lm.patch, -pad.patch, -ipv6.patch,
  -default-paths.patch, -cleanfiles.patch, -ai-next.patch, -einprogress.patch
- Adapt to updated license packaging guidelines

* Thu Sep 11 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.17-5
- Try next interface also in case of EINPROGRESS

* Mon Aug 25 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.17-4
- Try next interface on connect failure (backport)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.17-2
- Bump soname

* Fri Jul 11 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.17-1
- Update to gsoap 2.8.17

* Fri Jul 11 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.16-5
- Fix default import paths for soapcpp2 and wsdl2h

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.16-3
- Fix for IPv4 only hosts

* Thu Oct 31 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.16-2
- Move -lm to Libs.private in pkg-config files

* Wed Oct 16 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.16-1
- Update to gsoap 2.8.16
- Bump soname (struct soap has changed)

* Wed Oct 16 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.12-4
- Pad non-ipv6 struct gsoap to match ipv6 version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.12-1
- Update to gsoap 2.8.12
- Bump soname

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.7-2
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.7-1
- Update to gsoap 2.8.7
- Bump soname due to changes in struct soap w.r.t. previous Fedora version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.4-3
- Bump soname

* Tue Nov 01 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.4-2
- Move openssl libraries to Libs.private in pkg-config files

* Mon Oct 31 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.4-1
- Update to gsoap 2.8.4
- Drop gsoap-ipv6.patch implemented upstream
- Link gsoap SSL shared libraries with libssl

* Fri Oct 21 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.3-2
- Fix an issue with IPv4 only sockets when IPv6 support is enabled

* Tue Aug 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8.3-1
- Update to gsoap 2.8.3
- Drop the examples sub-package - the examples are written to be built
  in the source tree, installing them does not make sense without a
  major rewrite
- Add manpages from Debian

* Sat Feb 12 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7.17-3
- Enable IPv6 support

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 28 2010 Ivan Romanov <drizt@land.ru> - 2.7.17-1
- Update to gsoap 2.7.17
- Removed openssl patch, it fixed by upstream
- Added gsoap-2.7-iostream.patch to fix using iostream oldstyle in examples
- Added examples sources and binaries
- Added documentation

* Sat Apr 24 2010  <matt@redhat> - 2.7.16-1
- Update to gsoap 2.7.16
- Thanks to matt@mattjamison.com for update patches
- Removed unused_args patch (upstream)

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.7.13-2
- Fix build

* Mon May 11 2009  <matt@redhat> - 2.7.13-1
- Updated to gsoap 2.7.13

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.7.12-2
- rebuild with new openssl

* Wed Dec 24 2008  <matt@redhat> - 2.7.12-1
- Updated to gsoap 2.7.12:
-  Numerous bug fixes - xml:lang, maxOccurs="unbounded", SSL, xmlns="", ...
-  New features, maintaining backward compatibility - MinGW, wsseapi, multi-endpoint connect, ...
- Patches removed (incorporated upstream):
-  datadir_importpath-2.7.10.patch
-  install_soapcpp2_wsdl2h_aux-2.7.10.patch
-  no_locale.patch as default off, enable by defining WITH_C_LOCALE
- Patches added (sent upstream):
-  unused_args.patch - eliminate many unused param warnings

* Thu Feb 21 2008  <mfarrellee@redhat> - 2.7.10-4
- Applied upd patch from upstream. It fixes glibc C locale issues,
  hp-ux h_errno definition, and xsd:dateTime timezone processing for
  WS-I
- Removed tru64_hp_ux patches, they are present in upstream's upd
  patch
- Added no_locale.patch to stop configure from checking for locale
  version of functions

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.7.10-3
- Autorebuild for GCC 4.3

* Mon Feb 18 2008  <mfarrellee@redhat> - 2.7.10-2
- Removed --disable-namespaces from configure, result is code compiled
  against gsoap does not need to call set_soap_namespaces

* Sun Jan 27 2008  <mfarrellee@redhat> - 2.7.10-1
- Upgraded to 2.7.10 release
- Stopped hosting patches on grid.et.redhat.com
- Removed import_dom_h patch, it was integrated
- Removed large autotools patch, replaced with patch
  (use_libtool-2.7.10.patch) changing configure.in, gsoap/Makefile.am
  and gsoap/wsdl/Makefile.am, which enable libtool use, and a
  call to autoreconf
- Changed soapcpp2 references to gsoap as per new layout of source
  distribution
- Updated tru64_hp_up_c/pp patches to handle new source layout
- Install of soapcpp2/import with cp removed in favor of a patch to
  gsoap/Makefile.am (install_soapcpp2_wsdl2h_aux-2.7.10.patch)
- No pre-generated Makefiles are distributed, no longer removing them
- stdsoap2_cpp.cpp not in distribution, no longer removing it
- Added datadir_importpath-2.7.10.patch to set SOAPCPP2_IMPORT_PATH
  and WSDL2H_IMPORT_PATH, useful defaults, using ${datadir} instead of
  `pwd`
- Added autoconf, automake and libtool to BuildRequires, because
  configure.in and gsoap/Makefile.am are patched
- Added ?dist to Release

* Fri Nov 30 2007  <mfarrellee@redhat> - 2.7.9-0.4.l
- Added OpenSSL requirement

* Tue Nov 27 2007  <mfarrellee@redhat> - 2.7.9-0.3.l
- Decided soapcpp2/import/ files should be in /usr/share instead of
  /usr/include because they are not really headers gcc can
  process. Also, this is likely the location new versions of gsoap
  will install the import headers. People should use -I
  /usr/share/gsoap/import

* Mon Nov 26 2007  <mfarrellee@redhat> - 2.7.9-0.2.l
- Changed license tag to GPLv2+, which is more accurate
- Resolved bz399761 by adding soapcpp2/import/*.h to the -devel
  package as /usr/include/gsoap, users will need to add -I
  /usr/include/gsoap to their soapcpp2 line

* Sun Sep 30 2007  <mfarrellee@redhat> - 2.7.9-0.1.l
- Updated to 2.7.9l (2.7.9k patches still apply)
- Added patch for import/dom.h missing xsd__anyAttribute definitions
- Removed removal of .deps directories and autom4te.cache

* Mon Sep 24 2007  <mfarrellee@redhat> - 2.7.9-0.2.k
- Moved pkgconfig requirement to -devel package

* Tue Sep 11 2007  <mfarrellee@redhat> - 2.7.9-0.1.k
- Initial release

