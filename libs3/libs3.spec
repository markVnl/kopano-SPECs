#
# spec file for package libs3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define version_unconverted 4.1.git257

Name:           libs3
%define lname	libs3-4
Version:        4.1.git257
Release:        9.13
Summary:        C Library and tools for Amazon S3 access
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://aws.amazon.com/developertools/Amazon-S3/1648

Source:         %name-%version.tar.xz
Patch2:         s3-am.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)

%description
The libs3 project implements a C library API for Amazon S3.

%package -n %lname
Summary:        Shared library from libs3
Group:          System/Libraries

%description -n %lname
This package includes the libs3 shared object library, needed to run
applications compiled against libs3, and additionally contains the s3
utility for accessing Amazon S3.

%package devel
Summary:        Headers and documentation for libs3
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
This library provides an API for using Amazon's S3 service.
- access to all of S3's functionality
- no requirement to know HTTP, XML or SSL
- supports single-thread and multi-threaded operation in
  synchronous and asynchronous fashion

%package tools
Summary:        Utilities for Amazon S3 service
Group:          System/Management

%description tools
A command-line frontend for Amazon S3 access.

%prep
%setup -q
%patch -P 2 -p1

%build
mkdir -p m4
autoreconf -fi
%configure
make %{?_smp_flags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libs3.so.4*
%doc COPYING LICENSE

%files devel
%defattr(-,root,root)
%_includedir/libs3.h
%_libdir/libs3.so

%files tools
%defattr(-,root,root)
%_bindir/s3

%changelog
* Thu Jul 20 2017 jengelh@inai.de
- Update to new snapshot 4.1.git257
  * Adapted v4 signature construction for Linux.
  * Add auth. region to relevant API calls.
  * Support the generate_query_string operation with the new
    authorization/signature logic.
  * Fix query parameter handling in canonicalization.
  * Remove obsolete hash functions, update library major version
    due to API change.
  * Fix expected output for ACL with new identifier format.
  * Increase length of auth. header to account for requests with
    many amz headers.
  * Fix the logic that determines the hostname to use in HTTP
    headers.
  * fix S3_destroy_request_context() to correctly abort
    curl_multi context.
  * Request timeout for _create_bucket and _put_object.
  * Request timeout for _get_object and _head_object.
  * timeout: report timeout error if request timed out.
  * Fix signature error when requesting with sub resource.
  * Fix urlencode error according to AWS S3 documents.
- Removed s3-aws4.diff (merged)
* Fri Nov  4 2016 b.simonsen@kopano.com
- Updated s3-aws4.diff to new submission
- Added s3-revert-pr51.diff, needed for s3-aws4.diff to work
- Correct version to be 3.0~gitN, since the 2.0 release is already
  way past.
* Wed Aug 17 2016 jengelh@inai.de
- Update to new snapshot 2.0~git195
  * Add multipart copy API and support inside s3 executable
- Add s3-aws4.diff to support AWS4-HMAC-SHA256
* Thu Mar 31 2016 jengelh@inai.de
- Initial package (version 2.0~git193) for build.opensuse.org
