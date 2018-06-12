#
# spec file for package libvmime
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libvmime
%define lname	libvmime1
Summary:        Library for working with RFC 2822, MIME messages and IMAP/POP/SMTP
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        0.9.2
Release:        20.22
Url:            http://vmime.org/

Source:         https://github.com/kisli/vmime/archive/v%version.tar.gz
Patch1:         libvmime-nodatetime.diff
Patch2:         no-override-cflags.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ImageMagick
%if 0%{?suse_version} < 1310
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake >= 2.8.3
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  inkscape
BuildRequires:  libgnutls-devel
%if !0%{?sle_version}
BuildRequires:  libgsasl-devel
%endif
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1130
%define with_pdf 1
%if 0%{?suse_version} < 1300
BuildRequires:  texlive-bin-latex
%endif
BuildRequires:  texlive-latex
%if 0%{?suse_version} >= 1230
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(fancyheadings.sty)
BuildRequires:  tex(pcrr7t.tfm)
BuildRequires:  tex(ucs.sty)
%endif
%endif
BuildRequires:  xz

%description
VMime is a C++ class library for working with RFC2822 and
MIME-conforming messages (RFC2045–2049), as well as Internet
messaging services like IMAP, POP or SMTP.

VMime can parse, generate and modify messages, and also connect to
store and transport services to receive or send messages over the
Internet. The library offers features to build a mail client.

%package -n %lname
Summary:        Library for working with MIME messages and IMAP/POP/SMTP
Group:          System/Libraries

%description -n %lname
VMime is a C++ class library for working with RFC2822 and
MIME-conforming messages (RFC2045–2049), as well as Internet
messaging services like IMAP, POP or SMTP.

VMime can parse, generate and modify messages, and also connect to
store and transport services to receive or send messages over the
Internet. The library offers features to build a mail client.

%package devel
Summary:        Development files for vmime, an e-mail message library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
VMime is a C++ class library for working with RFC2822 and
MIME-conforming messages (RFC2045–2049), as well as Internet
messaging services like IMAP, POP or SMTP.

This subpackage contains the headers for the library's API.

%prep
%setup -qn vmime-%version
%patch -P 1 -P 2 -p1

%build
%if 0%{?with_pdf}
pushd doc/book/
make book_pdf
popd
%endif

cf="%optflags -DVMIME_ALWAYS_GENERATE_7BIT_PARAMETER=1"
cmake . \
	-DVMIME_SENDMAIL_PATH:STRING="%_sbindir/sendmail" \
	-DVMIME_BUILD_SAMPLES:BOOL=OFF \
%if 0%{?sle_version}
	-DVMIME_HAVE_SASL_SUPPORT:BOOL=OFF \
%endif
	-DVMIME_HAVE_TLS_SUPPORT:BOOL=ON \
	-DVMIME_BUILD_STATIC_LIBRARY:BOOL=OFF \
	-DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
	-DCMAKE_INSTALL_PREFIX:PATH="%_prefix" \
%if 0%{?suse_version} >= 1310
	-DCMAKE_CXX_FLAGS:STRING="$cf -std=gnu++11" \
%else
	-DCMAKE_CXX_FLAGS:STRING="$cf -std=gnu++0x" \
%endif
	-DCMAKE_C_FLAGS:STRING="$cf"
make %{?_smp_mflags} VERBOSE=1

%install
b="%buildroot"
%if 0%{?with_pdf}
mkdir -p "$b/%_docdir/%name"
cp -a doc/book/book.pdf "$b/%_docdir/%name/"
%endif
make install DESTDIR="$b"
find "$b" -type f -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc COPYING
%_libdir/%name.so.1*

%files devel
%defattr(-,root,root)
%_includedir/vmime
%_libdir/libvmime.so
%_libdir/pkgconfig/*.pc
%if 0%{?with_pdf}
%_docdir/%name
%endif

%changelog
* Mon Apr 23 2018 jengelh@inai.de
- Add no-override-cflags.diff so that vmime becomes externally
  buildable with other -O/-g levels.
* Thu Jul 13 2017 jengelh@inai.de
- Update description
* Thu Jul 13 2017 olaf@aepfle.de
- Remove openssl because gnutls is preferd already
* Wed Mar  8 2017 bosim@opensuse.org
- Don't stop the build due to SLES missing GSASL.
* Mon Jan 23 2017 jengelh@inai.de
- Resolve wrong name of cmake variable:
  CMAKE_RELEASE_TYPE -> CMAKE_BUILD_TYPE
* Tue Jan  3 2017 jengelh@inai.de
- Update to final release 0.9.2
  * Always ignore newlines between words.
- Drop dont-fixup.diff (issue fixed upstream),
  drop libvmime-sotag.diff (no longer needed).
* Sun Oct 30 2016 jengelh@inai.de
- Update to new git snapshot
  047cacb1dba516ca902b36a290f2b81555658c1e [0.9.2~g500]
  * Skip multiple (bogus) colons after header field name
- Add dont-fixup.diff
* Wed Jun 22 2016 jengelh@inai.de
- Update to new git snapshot
  4d1a6ad2f267e3b83f7c04122af8d8e7ee9a2113 [0.9.2~g490]
  * handle "x-uuencode" type
  * Skip word on unexpected error when fixing broken words.
  * XOAUTH2 auth mechanism support
* Wed May 13 2015 jengelh@inai.de
- Ship COPYING file
* Mon Aug 25 2014 dap@open.by, jengelh@inai.de
- Update to new git snapshot
  30ea54f269efa673a1eb5bc07e71715b67607dbc
  * No upstream changelog was provided
- Turn on SASL, TLS support
- Remove vmime-0.9.2-header-value-on-next-line.diff
  (no longer applies)
* Thu Dec 19 2013 jengelh@inai.de
- Use existing postscript fonts as BuildRequires
  (suggestion by user WernerFink)
* Mon Aug  5 2013 ro@suse.de
- BuildRequire texlive-bin-latex only for <= 12.3
* Wed Mar 27 2013 jengelh@inai.de
- Update to new git snapshot (54b5fe13f7e7cb6c4f63884e91ff472b42b63147)
- Removed because merged: vmime-0.8.1-charset-catch.diff,
  vmime-mixed-qp-in-parameter.diff, vmime-0.9.2-qp-in-buffers.diff
- Removed because they no longer apply: vmime-automake1_13.diff,
  vmime-noansiflag.patch
* Sun Mar  3 2013 jengelh@inai.de
- Add vmime-automake1_13.diff to fix up ancient autotools constructs
* Sat Aug 11 2012 jengelh@inai.de
- Make the package build on RHEL6
* Thu Jul 12 2012 jengelh@inai.de
- Enable always generating 7-bit parameters
  (https://jira.zarafa.com/browse/ZCP-9475)
* Thu May 10 2012 crrodriguez@opensuse.org
- Use RPM_OPT_FLAGS
- Do not use -ansi gcc flag.
* Fri Mar 16 2012 jengelh@medozas.de
- Update to new SVN snapshot rev 603 (ZCP 7.0.6 dependency)
  * Set Diffie-Hellman prime size (bug SF#3434852)
* Thu Jun 30 2011 jengelh@medozas.de
- Initial package for build.opensuse.org
