#
# spec file for package kopano
#
# Copyright (c) 2018 Mark Verlinde
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Kopano B.V.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%define release 0.4

%define with_rh_php71 1


%define apache_group apache

Name:           kopano
Version:        8.6.6
Release:        %release%{?dist}
Summary:        Groupware server suite
License:        AGPL-3.0-only
Group:          Productivity/Networking/Email/Servers
Url:            https://kopano.io/
Source:         https://github.com/Kopano-dev/kopano-core/archive/kopanocore-%{version}.tar.gz
Patch0:         jsoncpp_0.x.y_branch.patch
BuildRoot:      %{_tmppath}/kopanocore-%{version}
BuildRequires:  gettext-devel
BuildRequires:  gperftools-devel
BuildRequires:  gsoap-devel >= 2.8.49
BuildRequires:  krb5-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libcurl-devel
BuildRequires:  libical-devel >= 0.42
BuildRequires:  libicu-devel
BuildRequires:  libs3-devel >= 4.1
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libvmime-devel >= 0.9.2
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  python-devel >= 2.4
BuildRequires:  python-setuptools
BuildRequires:  libtidy-devel
BuildRequires:  swig
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(jsoncpp) >= 0.10.5
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  elinks
BuildRequires:  xapian-bindings-python
BuildRequires:  libxml2-python
BuildRequires:  mariadb-devel
%if %with_rh_php71
BuildRequires:  rh-php71-php-devel
BuildRequires:  devtoolset-7
%else
BuildRequires:  php-devel
BuildRequires:  gcc-c++ >= 4.8
%endif

%description
Kopano provides email storage on the server side and brings its own
Ajax-based mail client called WebAccess. Kopano is designed to
integrate with Kopano WebApp, Push clients and other mail services as an
alternative to Microsoft Exchange and other comparable mail servers.
Personal address book, calendar, notes and tasks, "Public Folders" and shared
calendar functionalities (inviting internal and external users,
resource management) can be handled by the software as well.

%package archiver
Summary:        Hierarchial Storage Management for the Kopano Core platform
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-lang = %version

%description archiver
The Kopano Archiver provides a Hierarchical Storage Management (HSM)
solution for Kopano Core.

To decrease the database size of your production Kopano server, the
Kopano Archiver copies or moves messages to a secondary Kopano
server. Clients will still be able to open the message from the
secondary Kopano server directly.

%package backup
Summary:        Utility to back up and restore Kopano stores
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common
Requires:       python2-kopano = %version

%description backup
kopano-backup is a MAPI-level backup/restore tool. It can sync
complete users/stores to disk using ICS to incrementally sync the
respective MAPI items, and can process stores in parallel.

%package bash-completion
Summary:        bash TAB completion for Kopano Core command-line utilities
Group:          System/Shells
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Some kopano commands offer bash completion, but it is an optional
feature.

%package client
Summary:        Kopano MAPI provider library
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common = %version
Requires:       kopano-lang = %version

%description client
Library which provides the main MAPI service to interface with a
Kopano server. This package is required by all Kopano client
programs.

%package common
Summary:        Shared files for Kopano Core services
Group:          Productivity/Networking/Email/Servers
Requires:       cronie
Requires:       logrotate
Requires(pre):  %_sbindir/groupadd
Requires(pre):  %_sbindir/useradd
%if 0%{?distro_without_intelligent_package_manager}
Obsoletes:      libkchl0
Obsoletes:      libkcservice0
Obsoletes:      libkcsoapclient0
Obsoletes:      libkcsoapserver0
%endif

%description common
Common components for services of Kopano Core.

%package contacts
Summary:        MAPI provider adding contact folders in the addressbook
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-client = %version
Requires:       kopano-common = %version

%description contacts
An additional MAPI provider which finds all contact folders of a user
and adds the contents transparently into the MAPI addrbook.

%package dagent
Summary:        E-Mail Delivery Agent for the Kopano platform
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common
Requires:       kopano-lang = %version
%if %with_rh_php71
Requires:       rh-php71
Requires:       php71-mapi
%else
Requires:       php
Requires:       php-mapi
%endif


%description dagent
Delivers incoming e-mail from your SMTP server to stores in the
Kopano server.

%package devel
Summary:        C++ development files for Kopano Core
Group:          Development/Libraries/C and C++
Requires:       kopano-common = %version
Requires:       libkcarchiver0 = %version-%release
Requires:       libkcarchivercore0 = %version-%release
Requires:       libkcfreebusy0 = %version-%release
Requires:       libkcicalmapi0 = %version-%release
Requires:       libkcinetmapi0 = %version-%release
Requires:       libkcmapi0 = %version-%release
Requires:       libkcrosie0 = %version-%release
Requires:       libkcserver0 = %version-%release
Requires:       libkcsoap0 = %version-%release
Requires:       libkcssl0 = %version-%release
Requires:       libkcsync0 = %version-%release
Requires:       libkcutil0 = %version-%release
Requires:       libmapi1 = %version-%release

%description devel
Development files to create programs for use with Kopano Core.

%package gateway
Summary:        POP3 and IMAP Gateway for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common

%description gateway
The gateway enables other e-mail clients to connect through POP3 or
IMAP to the Kopano server to read their e-mail. With IMAP, it is also
possible to view the contents of other folders and subfolders. The
gateway can be configured to listen for POP3, POP3S, IMAP and/or
IMAPS.

%package ical
Summary:        ICal and CalDAV Gateway for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common

%description ical
The iCal/CalDAV gateway enables users to retrieve their calendar
using iCalendar compliant clients. The iCal/CalDAV gateway can be
configured to listen for HTTP and HTTPS requests.

%package lang
Summary:        Translations for Kopano Core components
Group:          System/Localization

%description lang
Provides translations to various Kopano Core subpackages.

%package migration-imap
Summary:        Utility to migrate between IMAP mailboxes
Group:          Productivity/Networking/Email/Servers
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::HMAC_SHA1)
Requires:       perl(Digest::MD5)
Requires:       perl(English)
Requires:       perl(Errno)
Requires:       perl(Fcntl)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::Glob)
Requires:       perl(File::Path)
Requires:       perl(File::Spec)
Requires:       perl(File::stat)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(IO::Socket)
Requires:       perl(IO::Tee)
Requires:       perl(IPC::Open3)
Requires:       perl(MIME::Base64)
Requires:       perl(Mail::IMAPClient)
Requires:       perl(POSIX)
Requires:       perl(Readonly)
Requires:       perl(Term::ReadKey)
Requires:       perl(Test::More)
Requires:       perl(Time::HiRes)
Requires:       perl(Time::Local)
Requires:       perl(Unicode::String)
Requires:       perl(strict)
Requires:       perl(warnings)

%description migration-imap
kopano-migration-imap provides a utility based on imapsync to migrate
between IMAP mailboxes (including Kopano).

%package migration-pst
Summary:        Utility to import PST files
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common
Requires:       python2-kopano = %version


%description migration-pst
kopano-migration-pst is a utility to import PST files into Kopano. As PST
files are basically MAPI dumps, and Kopano also uses MAPI internally, there
should be practically no data loss, even including calendar data.

%package monitor
Summary:        Quota monitor for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common

%description monitor
Regularly checks stores for total usage. If a quota limit has been
exceeded, an e-mail will be internally sent to this account.

%package presence
Summary:        Kopano Core Presence Daemon
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common >= %version
Requires:       python-flask
Requires:       python-sleekxmpp
Requires:       python2-kopano = %version

%description presence
A daemon for collecting and exporting user presence information
across multiple protocols in a unified way. Supports XMPP and Spreed.
Clients can both query the daemon with presence information (for
example, the user is 'available' for XMPP and 'away' for Spreed) and
update presence information (for example, make a user 'available' on
Spreed). Queries and updates are performed with simple GET and PUT
requests, respectively, using a simple (and identical) JSON format.

%package search
Summary:        Indexed search engine for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common
Requires:       xapian-bindings-python
Requires:       python2-kopano = %version
Requires:       elinks
Requires:       xapian-core

%description search
kopano-search creates indexes for messages and attachments per user.
When this service is running, search queries on the server will use
this index to quickly find messages and contents of attached
documents, enhancing the search performance of kopano-server.

%package server
Summary:        Server component for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common = %version
# Needed for createstore scripts' functionality
Requires:       kopano-utils
# dlopened:
Requires:       libs3-4

%description server
This package provides the key component of Kopano Core, providing the
server to which Kopano clients connect. The server requires a MySQL
server to use for storage.

%package server-packages
Summary:        Metapackage to install the entire Kopano Core stack
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-backup = %version
Requires:       kopano-dagent = %version
Requires:       kopano-gateway = %version
Requires:       kopano-ical = %version
Requires:       kopano-monitor = %version
Requires:       kopano-search = %version
Requires:       kopano-server = %version
Requires:       kopano-spooler = %version
Requires:       kopano-utils = %version

%description server-packages
This package is merely meant to cause pulling in all the Kopano
server components.

%package spamd
Summary:        ICS-driven spam learning daemon for Kopano/SpamAssasin
Group:          Productivity/Networking/Email/Servers

%description spamd
A program which can teach SpamAssassin about spam based upon
the mails a user has moved to his Kopano junk folder.

%package spooler
Summary:        E-mail Spooler for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common
Requires:       kopano-lang = %version

%description spooler
The outgoing e-mail spooler. This service makes sure that e-mails
sent by clients are converted to Internet e-mail and forwarded to an
SMTP server.

%package utils
Summary:        Admin command-line utils for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-common = %version
Requires:       python2-kopano = %version

%description utils
Command-line clients to control and check the Kopano server.

%package -n libkcfreebusy0
Summary:        Implementation of Free/Busy time scheduling
Group:          System/Libraries

%description -n libkcfreebusy0
RFC 5545

%package -n libkcicalmapi0
Summary:        iCal interface for MAPI
Group:          System/Libraries

%description -n libkcicalmapi0
Provides an interface between iCal and MAPI.

%package -n libkcinetmapi0
Summary:        Internet e-mail interface for MAPI
Group:          System/Libraries

%description -n libkcinetmapi0
Provides an interface to convert between RFC 5322 Internet e-mail and
MAPI messages.

%package -n libmapi1
Summary:        Kopano's implementation of the Messaging API
Group:          System/Libraries

%description -n libmapi1
MAPI allows client programs to become (e-mail) messaging-enabled,
-aware, or -based by calling MAPI subsystem routines that interface
with certain messaging servers.

%package -n libkcarchiver0
Summary:        Library with shared Kopano archiver functionality
Group:          System/Libraries

%description -n libkcarchiver0
Library with shared archiver functionality for Kopano Core.

%package -n libkcarchivercore0
Summary:        Library with shared Kopano archiver functionality
Group:          System/Libraries

%description -n libkcarchivercore0
Library with shared archiver functionality for Kopano Core.

%package -n libkcrosie0
Summary:        Kopano HTML sanitizer interface
Group:          System/Libraries

%description -n libkcrosie0
This library contains the API to filter HTML mail using libtidy;
specifically, it contains the definitions which tags and attributes
to retain.

%package -n libkcserver0
Summary:        The Kopano Server library
Group:          System/Libraries

%description -n libkcserver0
This library contains the central server code which is responsible
for handling RPC calls from libmapi, loading/storing objects in the
database, etc.

%package -n libkcsoap0
Summary:        SOAP (de)serializer functions for Kopano's RPCs
Group:          System/Libraries

%description -n libkcsoap0
This library contains autogenerated code to (de)serialize the SOAP RPCs
that are sent between Kopano clients and server.

Remote Procedure Call more or less means that a callable function
translates its arguments (C++ objects in our case) into a
representation that can be sent over the network. On the receiving
side, this representation is translated back to objects again.

%package -n libkcsync0
Summary:        Routines for synchronization in Kopano Core
Group:          System/Libraries

%description -n libkcsync0

%package -n libkcmapi0
Summary:        MAPI-related utility functions for Kopano Core
Group:          System/Libraries

%description -n libkcmapi0

%package -n libkcssl0
Summary:        SSL-related utility functions for Kopano Core
Group:          System/Libraries

%description -n libkcssl0

%package -n libkcutil0
Summary:        Miscellaneous utility functions for Kopano Core
Group:          System/Libraries

%description -n libkcutil0

%if %with_rh_php71
%package -n php71-mapi
%else
%package -n php-mapi
%endif
Summary:        PHP bindings for MAPI
# php-ext is the one thing that can also request the "ZCONTACTS" provider
Group:          Development/Languages/PHP
Requires:       kopano-client = %version
Requires:       kopano-contacts = %version
Obsoletes:      php5-mapi
Provides:       php5-mapi

%if %with_rh_php71
%description -n php71-mapi
%else
%description-n php-mapi
%endif
Using this module, you can create PHP programs which use MAPI calls
to interact with Kopano.

%package -n python2-kopano
Summary:        High-level Python bindings for Kopano
Group:          Development/Languages/Python
Obsoletes:      python-kopano < %version-%release
Provides:       python-kopano = %version-%release
Requires:       python-dateutil
Requires:       python2-mapi

%description -n python2-kopano
Object-Oriented Python bindings for Kopano. Uses python-mapi to do
the low level work. Can be used for many common system administration
tasks.

%package -n python2-mapi
Summary:        Python bindings for MAPI
Group:          Development/Languages/Python
Requires:       kopano-client = %version
Obsoletes:      python-mapi < %version-%release
Provides:       python-mapi = %version-%release
Obsoletes:      libkcpyconv0
Obsoletes:      libkcpydirector0

%description -n python2-mapi
Low-level (SWIG-generated) Python bindings for MAPI. Using this
module, you can create Python programs which use MAPI calls to
interact with Kopano.

%package -n python2-zarafa
Summary:        Old module name support for Kopano
Group:          Development/Languages
Obsoletes:      kopano-compat
Provides:       kopano-compat = %version-%release

%description -n python2-zarafa
Provides some files under old module names.

%prep
%setup -qn kopano-core-kopanocore-%{version}
%patch0 -p1

%build

%if %with_rh_php71
  source /opt/rh/rh-php71/enable
  source /opt/rh/devtoolset-7/enable
%endif

autoreconf -fi
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z -Wl,relro"
PYTHON_CFLAGS=$(pkg-config python2 --cflags)
PYTHON_LIBS=$(pkg-config python2 --libs)

mkdir obj-python2 
pushd obj-python2 
%define _configure ../configure

%configure \
	--docdir="%_docdir/%name" \
	--with-userscript-prefix="%_sysconfdir/kopano/userscripts" \
	--with-quotatemplate-prefix="%_sysconfdir/kopano/quotamail" \
	--with-php-config="php-config" --enable-release \
	PYTHON="$(which python2)" PYTHON_CFLAGS="$PYTHON_CFLAGS" PYTHON_LIBS="$PYTHON_LIBS"

echo "%version" >version
make V=1 %{?_smp_mflags}
popd

%install
%make_install -C obj-python2/
find %{buildroot} -type f -name "*.la" -print -delete
# no headers for these two
rm -Rfv %{buildroot}/%_libdir/libkcpyconv.so %{buildroot}/%_libdir/libkcpydirector.so

# for (centos) el7 we only build python2
for i in kopano_backup kopano_cli kopano_migration_pst kopano_presence \
    kopano_search kopano_spamd kopano_utils; do
	rm -Rf %{buildroot}/%python3_sitelib/$i*
done

# distro-specifics
%if %with_rh_php71
  mkdir -p %{buildroot}/%{_unitdir}/kopano-dagent.service.d
  cat > %{buildroot}/%{_unitdir}/kopano-dagent.service.d/scl.conf <<-EOF
[Service]
Environment=X_SCLS=rh-php71
Environment=LD_LIBRARY_PATH=/opt/rh/rh-php71/root/usr/lib64
Environment=PATH=/usr/local/sbin:/usr/local/bin:/opt/rh/rh-php71/root/usr/sbin:/opt/rh/rh-php71/root/usr/bin:/usr/sbin:/usr/bin
EOF
  perl -i -pe 's{^#!/usr/bin/php}{#!/opt/rh/rh-php71/root/usr/bin/php}' \
	%{buildroot}/%_bindir/kopano-mr-accept %{buildroot}/%_bindir/kopano-mr-process
%endif

# some default dirs
mkdir -p %{buildroot}/%_defaultdocdir %{buildroot}/%{_sharedstatedir}/kopano/autorespond %{buildroot}/%{_sharedstatedir}/kopano/spamd/spam
mkdir -p %{buildroot}/%_localstatedir/log/kopano
chmod 750 %{buildroot}/%_localstatedir/log/kopano
%find_lang kopano

%triggerpostun archiver -- kopano-archiver
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/archiver.cfg" -a \
     -e "%_sysconfdir/kopano/archiver.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/archiver.cfg.rpmsave" \
		"%_sysconfdir/kopano/archiver.cfg"
fi

%post backup
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :

%triggerpostun backup -- kopano-backup
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/backup.cfg" -a \
     -e "%_sysconfdir/kopano/backup.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/backup.cfg.rpmsave" \
		"%_sysconfdir/kopano/backup.cfg"
fi

%post   client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%pre common
%_bindir/getent group kopano >/dev/null || \
	%_sbindir/groupadd -r kopano
%_bindir/getent passwd kopano >/dev/null || \
	%_sbindir/useradd -c "Kopano unprivileged account" \
	-g kopano -r kopano -s /sbin/nologin

%post common
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
chown kopano:kopano /var/lib/kopano 2>/dev/null || :
if [ -x /usr/bin/systemd-tmpfiles ]; then
	/usr/bin/systemd-tmpfiles --create kopano-tmpfiles.conf || :
fi

%triggerpostun common -- kopano-common
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/sysconfig/kopano" -a \
     -e "%_sysconfdir/sysconfig/kopano.rpmsave" ]; then
	mv -v "%_sysconfdir/sysconfig/kopano.rpmsave" \
		"%_sysconfdir/sysconfig/kopano"
fi

%post   contacts -p /sbin/ldconfig
%postun contacts -p /sbin/ldconfig

%pre dagent
# nothing to do?

%post dagent
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-dagent.service

%preun dagent
%systemd_preun kopano-dagent.service

%postun dagent
%systemd_postun_with_restart kopano-dagent.service
%triggerpostun dagent -- kopano-dagent
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/autorespond" -a \
     -e "%_sysconfdir/kopano/autorespond.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/autorespond.rpmsave" \
		"%_sysconfdir/kopano/autorespond"
fi
if [ ! -e "%_sysconfdir/kopano/dagent.cfg" -a \
     -e "%_sysconfdir/kopano/dagent.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/dagent.cfg.rpmsave" \
		"%_sysconfdir/kopano/dagent.cfg"

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%pre gateway
# nothing to do?

%post gateway
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-gateway.service

%preun gateway
%systemd_preun kopano-gateway.service

%postun gateway
%systemd_postun_with_restart kopano-gateway.service

%triggerpostun gateway -- kopano-gateway
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/gateway.cfg" -a \
     -e "%_sysconfdir/kopano/gateway.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/gateway.cfg.rpmsave" \
		"%_sysconfdir/kopano/gateway.cfg"
fi
%pre ical
# nothing to do?

%post ical
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-ical.service

%preun ical
%systemd_preun kopano-ical.service

%postun ical
%systemd_postun_with_restart kopano-ical.service
%triggerpostun ical -- kopano-ical
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/ical.cfg" -a \
     -e "%_sysconfdir/kopano/ical.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/ical.cfg.rpmsave" \
		"%_sysconfdir/kopano/ical.cfg"
fi

%post migration-pst
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :

%triggerpostun migration-pst -- kopano-migration-pst
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/migration-pst.cfg" -a \
     -e "%_sysconfdir/kopano/migration-pst.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/migration-pst.cfg.rpmsave" \
		"%_sysconfdir/kopano/migration-pst.cfg"
fi

%pre monitor
# nothing to do?

%post monitor
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-monitor.service

%preun monitor
%systemd_preun kopano-monitor.service

%postun monitor
%systemd_postun_with_restart kopano-monitor.service

%triggerpostun monitor -- kopano-monitor
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/monitor.cfg" -a \
     -e "%_sysconfdir/kopano/monitor.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/monitor.cfg.rpmsave" \
		"%_sysconfdir/kopano/monitor.cfg"
fi
%pre presence
# nothing to do?

%post presence
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-presence.service

%preun presence
%systemd_preun kopano-presence.service

%postun presence
%systemd_postun_with_restart kopano-presence.service

%triggerpostun presence -- kopano-presence
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/presence.cfg" -a \
     -e "%_sysconfdir/kopano/presence.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/presence.cfg.rpmsave" \
		"%_sysconfdir/kopano/presence.cfg"
fi
%pre search
# nothing to do?

%post search
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-search.service

%preun search
%systemd_preun kopano-search.service

%postun search
%systemd_postun_with_restart kopano-search.service

%triggerpostun search -- kopano-search
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/search.cfg" -a \
     -e "%_sysconfdir/kopano/search.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/search.cfg.rpmsave" \
		"%_sysconfdir/kopano/search.cfg"
fi
%pre server
# nothing to do?

%post server
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-server.service

%preun server
%systemd_preun kopano-server.service

%postun server
%systemd_postun_with_restart kopano-server.service

%triggerpostun server -- kopano-server
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/server.cfg" -a \
     -e "%_sysconfdir/kopano/server.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/server.cfg.rpmsave" \
		"%_sysconfdir/kopano/server.cfg"
fi
if [ ! -e "%_sysconfdir/kopano/unix.cfg" -a \
     -e "%_sysconfdir/kopano/unix.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/unix.cfg.rpmsave" \
		"%_sysconfdir/kopano/unix.cfg"
fi
if [ ! -e "%_sysconfdir/kopano/ldap.propmap.cfg" -a \
	     -e "%_sysconfdir/kopano/ldap.propmap.cfg.rpmsave" ]; \
then
		mv -v "%_sysconfdir/kopano/ldap.propmap.cfg.rpmsave" \
			"%_sysconfdir/kopano/ldap.propmap.cfg"
elif grep -q ldap.propmap.cfg "%_sysconfdir/kopano/server.cfg"; then
		# No private modifications. Make sure it exists,
		# if loosely referenced.
		ln -Tsv "%_datadir/kopano/ldap.propmap.cfg" \
			"%_sysconfdir/kopano/ldap.propmap.cfg"
fi


%pre spooler
# nothing to do?

%post spooler
chown -Rh kopano:kopano /var/log/kopano 2>/dev/null || :
%systemd_post kopano-spooler.service

%preun spooler
%systemd_preun kopano-spooler.service

%postun spooler
%systemd_postun_with_restart kopano-spooler.service

%triggerpostun spooler -- kopano-spooler
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/spooler.cfg" -a \
     -e "%_sysconfdir/kopano/spooler.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/spooler.cfg.rpmsave" \
		"%_sysconfdir/kopano/spooler.cfg"
fi
%post   -n libkcfreebusy0 -p /sbin/ldconfig
%postun -n libkcfreebusy0 -p /sbin/ldconfig
%post   -n libkcicalmapi0 -p /sbin/ldconfig
%postun -n libkcicalmapi0 -p /sbin/ldconfig
%post   -n libkcinetmapi0 -p /sbin/ldconfig
%postun -n libkcinetmapi0 -p /sbin/ldconfig
%post   -n libmapi1 -p /sbin/ldconfig
%postun -n libmapi1 -p /sbin/ldconfig
%post   -n libkcarchiver0 -p /sbin/ldconfig
%postun -n libkcarchiver0 -p /sbin/ldconfig
%post   -n libkcarchivercore0 -p /sbin/ldconfig
%postun -n libkcarchivercore0 -p /sbin/ldconfig
%post   -n libkcrosie0 -p /sbin/ldconfig
%postun -n libkcrosie0 -p /sbin/ldconfig
%post   -n libkcserver0 -p /sbin/ldconfig
%postun -n libkcserver0 -p /sbin/ldconfig
%post   -n libkcsoap0 -p /sbin/ldconfig
%postun -n libkcsoap0 -p /sbin/ldconfig
%post   -n libkcsync0 -p /sbin/ldconfig
%postun -n libkcsync0 -p /sbin/ldconfig
%post   -n libkcmapi0 -p /sbin/ldconfig
%postun -n libkcmapi0 -p /sbin/ldconfig
%post   -n libkcssl0 -p /sbin/ldconfig
%postun -n libkcssl0 -p /sbin/ldconfig
%post   -n libkcutil0 -p /sbin/ldconfig
%postun -n libkcutil0 -p /sbin/ldconfig

%post -n python2-mapi 
/sbin/ldconfig
%if 0%{?_unitdir:1}
if systemctl is-active kopano-dagent >/dev/null; then
	systemctl try-restart kopano-dagent
fi
if systemctl is-active kopano-spooler >/dev/null; then
	systemctl try-restart kopano-spooler
fi
%else
%restart_on_update kopano-dagent
%restart_on_update kopano-spooler
%endif

%postun -n python2-mapi -p /sbin/ldconfig

%files archiver
%defattr(-,root,root)
%_sbindir/kopano-archiver*
%_mandir/man*/kopano-archiver*
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/archiver.cfg

%files backup
%defattr(-,root,root)
%_sbindir/kopano-backup
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/backup.cfg
%_mandir/man*/kopano-backup.*
%python_sitelib/kopano_backup/
%python_sitelib/kopano_backup-*.egg-info

%files bash-completion
%defattr(-,root,root)
%dir %_sysconfdir/bash_completion.d
%config %_sysconfdir/bash_completion.d/kopano-bash-completion.sh

%files client -f kopano.lang
%defattr(-,root,root)
# Files live in /usr/lib
%dir %_prefix/lib/mapi.d
%_prefix/lib/mapi.d/kopano.inf
%exclude %_datadir/locale
%dir %_libdir/kopano
%_libdir/kopano/libkcclient.so

%files common
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/logrotate.d/*
%doc AGPL-3
%_sysusersdir/
%_tmpfilesdir/
%_mandir/man5/kopano-coredump.5*
%_mandir/man7/kopano.7*
%_mandir/man7/mapi.7*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/sysconfig.txt

%files contacts
%defattr(-,root,root)
# Files live in /usr/lib
%dir %_prefix/lib/mapi.d
%_prefix/lib/mapi.d/zcontacts.inf
%dir %_libdir/kopano
%_libdir/kopano/libkccontacts.so

%files dagent
%defattr(-,root,root)
%_sbindir/kopano-autorespond
%_sbindir/kopano-autorespond.py
%_sbindir/kopano-dagent
%_sbindir/kopano-mr-accept
%_sbindir/kopano-mr-process
%_sbindir/kopano-mr-accept.py
%_sbindir/kopano-mr-process.py
%_unitdir/kopano-dagent.service
%if %with_rh_php71
%_unitdir/kopano-dagent.service.d/scl.conf
%endif
%_datadir/kopano-dagent/
%_mandir/man*/kopano-autorespond.*
%_mandir/man*/kopano-mr-accept.*
%_mandir/man*/kopano-mr-process.*
%_mandir/man*/kopano-dagent.*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %_localstatedir/lib/kopano/autorespond/
%attr(0750,kopano,kopano) %_localstatedir/lib/kopano/dagent/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/autorespond
%_docdir/kopano/example-config/autorespond.cfg
%_docdir/kopano/example-config/dagent.cfg
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/usr.sbin.kopano-dagent
%python_sitelib/kopano_utils/
%python_sitelib/kopano_utils-*.egg-info

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/libkcfreebusy.so
%_libdir/libkcicalmapi.so
%_libdir/libkcinetmapi.so
%_libdir/libmapi.so
%_libdir/libkcarchivercore.so
%_libdir/libkcarchiver.so
%_libdir/libkcrosie.so
%_libdir/libkcserver.so
%_libdir/libkcsoap.so
%_libdir/libkcsync.so
%_libdir/libkcmapi.so
%_libdir/libkcssl.so
%_libdir/libkcutil.so
%_libdir/pkgconfig/*
%_datadir/gdb/

%files gateway
%defattr(-,root,root)
%_sbindir/kopano-gateway
%_unitdir/kopano-gateway.service
%_mandir/man*/kopano-gateway.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/gateway.cfg
%dir %_docdir/kopano-gateway
%_docdir/kopano-gateway/optimize-imap.*

%files ical
%defattr(-,root,root)
%_sbindir/kopano-ical
%_unitdir/kopano-ical.service
%_mandir/man*/kopano-ical.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/ical.cfg

%files lang -f kopano.lang
%defattr(-,root,root)

%files migration-imap
%defattr(-,root,root)
%_bindir/kopano-migration-imap

%files migration-pst
%defattr(-,root,root)
%_sbindir/kopano-migration-pst
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/migration-pst.cfg
%_mandir/man*/kopano-migration-pst.*
%python_sitelib/kopano_migration_pst/
%python_sitelib/kopano_migration_pst-*.egg-info

%files monitor
%defattr(-,root,root)
%dir %_sysconfdir/kopano
%config %_sysconfdir/kopano/quotamail
%_sbindir/kopano-monitor
%_unitdir/kopano-monitor.service
%_mandir/man*/kopano-monitor.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/monitor.cfg

%files presence
%defattr(-,root,root)
%_sbindir/kopano-presence
%_unitdir/kopano-presence.service
%dir %_datadir/kopano
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/presence.cfg
%python_sitelib/kopano_presence/
%python_sitelib/kopano_presence-*.egg-info

%files search
%defattr(-,root,root)
%dir %_sysconfdir/kopano
%dir %_sysconfdir/kopano/searchscripts
%config(noreplace) %attr(0640,root,kopano) %_sysconfdir/kopano/searchscripts/*.db
%config(noreplace) %attr(-,root,kopano) %_sysconfdir/kopano/searchscripts/*.xslt
%config(noreplace) %attr(-,root,kopano) %_sysconfdir/kopano/searchscripts/attachments_parser
%config(noreplace) %attr(-,root,kopano) %_sysconfdir/kopano/searchscripts/zmktemp
%_sbindir/kopano-search
%_sbindir/kopano-search-xapian-compact.py
%_unitdir/kopano-search.service
%_mandir/man*/kopano-search.*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/search/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/search.cfg
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/usr.sbin.kopano-search
%python_sitelib/kopano_search/
%python_sitelib/kopano_search-*.egg-info

%files server
%defattr(-,root,root)
%dir %_sysconfdir/kopano
%dir %_sysconfdir/kopano/userscripts
%dir %_sysconfdir/kopano/userscripts/createcompany.d
%dir %_sysconfdir/kopano/userscripts/creategroup.d
%dir %_sysconfdir/kopano/userscripts/createuser.d
%_sysconfdir/kopano/userscripts/*.sh
%_sysconfdir/kopano/userscripts/create*/*
%_sysconfdir/kopano/userscripts/createcompany
%_sysconfdir/kopano/userscripts/creategroup
%_sysconfdir/kopano/userscripts/createuser
%_sysconfdir/kopano/userscripts/deletecompany
%_sysconfdir/kopano/userscripts/deletegroup
%_sysconfdir/kopano/userscripts/deleteuser
%_sbindir/kopano-server
%dir %_libdir/kopano
%_libdir/kopano/libkcserver-[a-z]*.so
%_unitdir/kopano-server.service
%_mandir/man*/kopano-server.*
%_mandir/man*/kopano-ldap.cfg.*
%_mandir/man*/kopano-unix.cfg.*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_datadir/kopano
%_datadir/kopano/ldap.active-directory.cfg
%_datadir/kopano/ldap.openldap.cfg
%_datadir/kopano/ldap.propmap.cfg
%dir %_docdir/kopano
%_docdir/kopano/audit-parse.pl
%_docdir/kopano/createuser.dotforward
%_docdir/kopano/db-calc-storesize
%_docdir/kopano/db-convert-attachments-to-files
%_docdir/kopano/db-remove-orphaned-attachments
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/ldap.cfg
%_docdir/kopano/example-config/server.cfg
%_docdir/kopano/example-config/unix.cfg
%_docdir/kopano/ldap-switch-sendas.pl
%_docdir/kopano/ssl-certificates.sh
%_docdir/kopano/update-resource-recipients
%_docdir/kopano/kopano.ldif
%_docdir/kopano/kopano.schema
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/usr.sbin.kopano-server

%files server-packages
%defattr(-,root,root)
# We want it to be rather empty; but rpmlint does not like it empty.
%dir %_docdir/kopano

%files spamd
%defattr(-,root,root)
%_sbindir/kopano-spamd
%_unitdir/kopano-spamd.service
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/spamd/
%_mandir/man*/kopano-spamd.*
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/spamd.cfg
%python_sitelib/kopano_spamd/
%python_sitelib/kopano_spamd*.egg-info

%files spooler
%defattr(-,root,root)
%_sbindir/kopano-spooler
%_unitdir/kopano-spooler.service
%_mandir/man*/kopano-spooler.*
%_datadir/kopano-spooler
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %_localstatedir/lib/kopano/spooler/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano
%dir %_docdir/kopano/example-config
%_docdir/kopano/example-config/spooler.cfg

%files utils
%defattr(-,root,root)
%_bindir/kopano-fsck
%_bindir/kopano-oof
%_bindir/kopano-passwd
%_bindir/kopano-set-oof
%_bindir/kopano-stats
%_sbindir/kopano-admin
%_sbindir/kopano-cachestat
%_sbindir/kopano-cli
%_sbindir/kopano-dbadm
%_sbindir/kopano-fix-ipm-subtree
%_sbindir/kopano-localize-folders
%_sbindir/kopano-mailbox-permissions
%_sbindir/kopano-recreate-systemfolders
%_sbindir/kopano-rules
%_sbindir/kopano-search-upgrade-findroots.py
%_sbindir/kopano-srvadm
%_sbindir/kopano-storeadm
%_mandir/man*/kopano-admin.*
%_mandir/man*/kopano-cachestat.*
%exclude %_mandir/man*/kopano-cfgchecker.*
%_mandir/man*/kopano-cli.*
%_mandir/man*/kopano-dbadm.*
%_mandir/man*/kopano-fsck.*
%_mandir/man*/kopano-mailbox-permissions.*
%_mandir/man*/kopano-oof.*
%_mandir/man*/kopano-passwd.*
%_mandir/man*/kopano-set-oof.*
%_mandir/man*/kopano-srvadm.*
%_mandir/man*/kopano-stats.*
%_mandir/man*/kopano-storeadm.*
%dir %_libexecdir/kopano
%_libexecdir/kopano/mapitime
%_libexecdir/kopano/kscriptrun
%python_sitelib/kopano_cli/
%python_sitelib/kopano_cli*.egg-info

%files -n libkcfreebusy0
%defattr(-,root,root)
%_libdir/libkcfreebusy.so.0*

%files -n libkcicalmapi0
%defattr(-,root,root)
%_libdir/libkcicalmapi.so.0*

%files -n libkcinetmapi0
%defattr(-,root,root)
%_libdir/libkcinetmapi.so.0*

%files -n libmapi1
%defattr(-,root,root)
%_libdir/libmapi.so.1*

%files -n libkcarchiver0
%defattr(-,root,root)
%_libdir/libkcarchiver.so.0*

%files -n libkcarchivercore0
%defattr(-,root,root)
%_libdir/libkcarchivercore.so.0*

%files -n libkcrosie0
%defattr(-,root,root)
%_libdir/libkcrosie.so.0*

%files -n libkcserver0
%defattr(-,root,root)
%_libdir/libkcserver.so.0*

%files -n libkcsoap0
%defattr(-,root,root)
%_libdir/libkcsoap.so.0*

%files -n libkcsync0
%defattr(-,root,root)
%_libdir/libkcsync.so.0*

%files -n libkcmapi0
%defattr(-,root,root)
%_libdir/libkcmapi.so.0*

%files -n libkcssl0
%defattr(-,root,root)
%_libdir/libkcssl.so.0*

%files -n libkcutil0
%defattr(-,root,root)
%_libdir/libkcutil.so.0*

%if %with_rh_php71
%files -n php71-mapi
%else
%files -n php-mapi
%endif
%defattr(-,root,root)
%if %with_rh_php71
%dir /etc/opt/rh/rh-php71/php.d
%dir /opt/rh/rh-php71/root/usr/lib64/php/modules
%config(noreplace) /etc/opt/rh/rh-php71/php.d/mapi.ini
/opt/rh/rh-php71/root/usr/lib64/php/modules/mapi*
%else
%dir %_sysconfdir/php.d
%config(noreplace) %_sysconfdir/php.d/mapi.ini
%_libdir/php/modules/mapi*
%endif
%dir %_datadir/kopano/
%_datadir/kopano/php/

%files -n python2-kopano
%defattr(-,root,root)
%python_sitelib/%name/
%python_sitelib/%name-*.egg-info
%files -n python2-mapi
%defattr(-,root,root)
%_libdir/libkcpyconv-2*.so
%_libdir/libkcpydirector-2*.so
%python_sitelib/MAPI/
%python_sitelib/MAPI-*.egg-info
%python_sitelib/MAPICore.*
%python_sitelib/icalmapi.*
%python_sitelib/inetmapi.*
%python_sitelib/*libfreebusy.*
%python_sitearch/*MAPICore.*
%python_sitearch/*icalmapi.*
%python_sitearch/*inetmapi.*
%python_sitearch/*libfreebusy.*

%files -n python2-zarafa
%defattr(-,root,root)
%python_sitelib/zarafa/
%python_sitelib/zarafa-*.egg-info

%changelog
* Thu Aug 09 2018 mark.verlinde@gmail.com
- Rebuild for centos new upstream release 8.6.6
- Optional rh-php71 build
  * clean-up spec
* Mon Aug 06 2018 - jengelh@inai.de
- Update to new upstream release 8.6.6
  * ical: handle double quotes in Content-Type header
  * server: repair broken timing log messages for ldapplugin
  * php7-ext: cure stack corruption in mapi_vcftomapi
  * gateway: avoid uncaught exception when client disconnects midway
  * dagent: avoid always running into K-2383
  * server: avoid SSL crash near ERR_clear_error on shutdown
* Tue Jun 12 2018 mark.verlinde@gmail.com
- Update to new upstream release 8.6.2
  * Sanitize spec for (centos) el7 build 
    jsoncpp_0.x.y_branch.patch, epel package is build from 0.x.y branch.
  * == Fixes ==
  * installer: remove duplicate defaults from sample config
  * icalmapi: allow RRULE with DTSTART having zulu-marking [KC-414, KC-811]
  * icalmapi: do not mark timestamp as UTC when we explicitly give a
    timezone [KC-920, KC-1018]
  * icalmapi: do not write empty fields to VCF files [KW-2503]
  * scripts: follow symbolic links when running user/group/company scripts,
    and run them in lexicographic order [KC-1171,KC-1172]
  * common: force Unicode for internal string translations [KC-1140]
  * common: remove bin2hex warning [KC-1178]
  * pyko: fix Item.searchkey
  * == Enhancements ==
  * libicalmapi: allow some properties to be missing when serializing ADR
  * kopano-dbadm: default to a loglevel so all dbadm messages get shown [KC-1167]
* Mon May 28 2018 jengelh@inai.de
- Update to new upstream snapshot 8.6.1.99
  * Fixes:
  * Fix crash due to ODR violation
  * libserver: drop all remains of clientupdatestatus table
  * gateway: fix crash when new client immediately disconnects
  * mapi: avoid garbage at end of malformed RTF
  * Enhancements:
  * kopano-dbadm: new diagnostics program for offline database
    modification
  * kopano-server: allow use of --ignore-da to skip schema update
    that won't complete
  * build: support ICU 61
  * propmap: expose kopanoHidden LDAP attribute as PR_EC_AB_HIDDEN
  * Changes:
  * daemons: disable SSL renegotiation for OpenSSL 1.1+
  * server: invalid port strings are now rejected
  * client: quiesce verbose logon failure messages
  * boot: set default and UTF-8 locale for services
* Fri Apr  6 2018 jengelh@inai.de
- Update to new upstream release 8.6.1
  * Fixes:
  * backup: ignore error when server cannot find attachments
  * server: search folders were not loaded on startup
  * monitor: handle absence of config file
  * dagent: do not treat -d option like -c was given
  * server: fix a case where an old kopano-server would refuse to
    start with a newer database even if --ignore-da was used
  * server: fix server/client getting slower when named properties
    are created multiple times [KC-1108]
  * client: fix data corruption when server returns high named
    property IDs [KC-1107]
  * Changes (generally requires admin action):
  * inetmapi: stop treating empty indexed_headers as "X-*"
  * dagent: cease indexing X-Headers by default
  * dagent: turn indexed_headers from a prefix list into an
    exact-match set
  * If you need certain e-mail headers copied into named
    properties, they MUST be explicitly listed _one by one_ in
    dagent.cfg:indexed_headers now.
  * Enhancements:
  * server: reorder SQL log messages so the error is shown first,
    and do say when the message was truncated
* Fri Mar  9 2018 jengelh@inai.de
- Update to new upstream release 8.6.0
  * Enhancements:
  * spooler: rules support testing for out-of-office flag
  * kopano-spamd: new daemon for spam learning in Kopano/SpamAssasin
  * kopano-oof: new utility for Out Of Office
  * kopano-storeadm: new utility replacing the store functions
    of kopano-admin
  * daemons: added the --dump-config option
  * inetmapi: ensure all generated messages has a Message-ID
  * gateway: handle a zero-length PR_TRANSPORT_MESSAGE_HEADERS property
    as if it was absent
  * Changes:
  * gateway: generate Internet headers if missing
  * inetmapi: ensure all messages have a Message-Id
* Sat Mar  3 2018 jengelh@inai.de
- Update to new bugfix release 8.5.4
  * server: emit log entry when LDAP is missing server info objects
  * spooler: avoid deadlock due to double mutex acquisition
    within one thread
  * php: mapi_icaltomapi did not copy the iCal recipients to the
    MAPI object
  * archiver had forgotten to create its SQL tables on first use
  * php: make ParseICal able to deduce organizer addresses
  * admin: --user-count failed to print user counts
  * server: fix broken cache handling for ICS bulk restriction
    matching
  * icalmapi: handle BDAY VCF and REV VCF property
  * libserver: restore PR_EMS_AB_HOME_MDB
* Mon Feb  5 2018 jengelh@inai.de
- Update to final tag 8.5.0
  * libserver: store size for orphaned stores was reported
    incorrectly
  * client: have OpenEntry check for NULL entryids and entryids
    too short
  * dagent, client: fix nonfunctional HTML filter
  * common: switch logging to stderr when pipe dies
  * spooler: avoid printing garbage when non-worker child exits
* Sat Jan  6 2018 jengelh@inai.de
- Update to new upstream tag 8.4.91 (RC)
  * Enhancements:
  * server: new "server_listen" directive replacing "server_bind"
  * server: stronger keep-alive
  * server: further general performance improvements
  * server: update PR_LOCAL_COMMIT_MAX on hard-deletes
  * server: speed up contact and search folder querying
  * server: skip some unnecessary attachment accesses
  * spooler: introduce indexed_headers config directive
  * search: pass "limit_results" to xapian to improve performance
  * search: optionally index draft folders
  * unixplugin: support multiple non_login_shells
  * unixplugin: add /sbin/nologin as a non_login_shell (new
    installs only)
  * gateway: RFC 6154 support
  * kopano-spamd: new program
  * icalmapi: support URL, NICKNAME, PRODID in vcards
  * Fixes:
  * gateway: generate envelope using inetmapi if not present yet
  * spooler: only evaluate rules that are explicitly enabled
    using PR_RULE_STATE
  * Changes:
  * /etc/kopano is no longer prepopulated, create .cfg manually
    if you need to override anything
  * server: remove support for upgrading databases older than ZCP
    7.2
  * gateway: use threaded mode for reduced memory usage on
    many-user systems (new installs only)
  * gateway: the "imap_store_rfc822" config directive is removed
  * server: the "counter_reset" config directive is removed
  * spooler: the "always_send_utf8" config directive is removed
* Sun Dec  3 2017 jengelh@inai.de
- Add 0001-build-fix-build-error-w.r.t.-gettimeofday.patch
* Thu Nov 23 2017 rbrown@suse.com
- Replace references to /var/adm/fillup-templates with new
  %%_fillupdir macro (boo#1069468)
* Wed Nov 15 2017 jengelh@inai.de
- Update to bugfix snapshot 8.4.4
  * common: fix detection of local connections that need not use
    zlib compression
  * libserver: improve ECICS error reporting
  * dagent: reenable automated backtraces when invoked with -f
  * php5-ext: fix positive retval setting in error case
  * dagent: redirect rule led to crash
  * inetmapi: overwrite recipients instead of appending
* Thu Nov  2 2017 jengelh@inai.de
- Update to bugfix release 8.4.2
  * server: revert NO_UNSIGNED_SUBTRACTIONS edit
* Wed Nov  1 2017 jengelh@inai.de
- Update to bugfix release 8.4.1
  * inetmapi: handle empty/invalid Sender in RFC2822 mails
  * spooler: for send-later mails, check trash, not outbox
* Tue Oct 31 2017 jengelh@inai.de
- Update to new upstream release 8.4.0
  * dagent, gateway: whitelist-based HTML filter
  * provider: speed up getIDsFromNames by reducing SQL queries
  * client: speedup from-scratch MAPI session creation by
    avoiding extraneous logon-logoff cycles during provider
    initialization
  * client: add API for dump+restore of MAPI session profile data
    so libmapi users can skip provider reinitialization at
    program startup
  * mapi: disable very slow RTF compression
  * server: add entry cache for S3 backend
  * icalmapi: handle up to three email addresses in a vcard
  * icalmapi: support ADR, ORG, TITLE tags in VCF files
  * backup: save and restore store-level ACLs
  * backup: merge store-level metadata
* Tue Aug 29 2017 jengelh@inai.de
- Add Requires for kopano-migration-imap [boo#1055939]
* Tue Aug 15 2017 jengelh@inai.de
- Update to new bugfix snapshot 8.3.3~24
  * server: fix disabling of shared reminders [KC-728]
* Tue Aug  8 2017 jengelh@inai.de
- Update to new bugfix snapshot 8.3.3~22
  * gateway: trim CRLF from PR_EC_IMAP_BODY{,STRUCTURE} and
    make Apple Mail client work again [KC-668, KC-720]
  * server: disallow empty value for embedded_attachment_limit
    and depth counting error [KC-745]
  * common: fix incorrect timeout check in scheduler which had
    disabled softdeletes [KC-638]
  * server: disable reminders from shared stores [KC-758]
  * catch pointer underflows / NULL pointers [KC-694, KC-60,
    KC-177, KC-355, KC-378, KC-379, KC-669, KC-754]
  * libserver: avoid creating multi-stream gzip files
    [KC-104, KC-304, KC-597]
* Thu Jul  6 2017 jengelh@inai.de
- Update to new bugfix release 8.3.1
  * inetmapi: do not force HTML when use_tnef is set
    to minimal [KC-664]
  * spooler: avoid a use-after-free, and a deadlock after
    this failure [KC-588]
  * server: avoid unchecked return value and unsigned
    underflow [KC-656]
  * php: rework pointer value storing
  * daemons: call initgroups when switching user and
    don't fall over [KC-684,KC-690]
- Update to new bugfix release 8.3.2
  * gateway: fix an IMAP protocol error [KC-668]
    Apple Mail/Alpine did not show mails with long encoded subjects
  * common: restore ability to output crashdump [KC-630]
  * inetmapi: avoid short allocation on group
    expansion [KC-388,KC-727]
* Thu Apr 27 2017 jengelh@inai.de
- Update to new upstream release 8.3
  * Enhancements:
  * migration-pst: call SaveChanges only once [KC-534]
  * Fixes:
  * caldav: avoid a nullptr dereference [KC-236]
  * cachestat: avoid exception and unpack tuple [KC-402]
  * ldapplugin: revert "catch empty ldap_search_base" [KC-602]
  * spooler: fix crash on forwarding rules [KC-608]
* Wed Mar  8 2017 jengelh@inai.de
- Update to snapshot 8.3.0~1007
  * Enhancements:
  * gateway: optimize LIST, SELECT, STATUS [KC-490]
  * icalmapi: VCF conversion [KC-420]
  * Fixes:
  * migration-pst: skip root folder more intelligently [KC-487]
  * migration-pst: MV properties are handled better [KC-457]
  * client: add extra checks for EID sizes [KC-500]
  * gateway: enforce user and password checking on local socket [KC-396,KC-490]
  * Changes:
  * migration-pst: ignore decode errors [KC-521]
  * common: fix empty text bodies when converting U+0000 from HTML [KC-557]
  * icalmapi: reworked copying description into mail body [KC-568]
* Thu Mar  2 2017 m.kromer@kopano.com
- Build-fix include of kopano-migration-imap
* Wed Feb  1 2017 jengelh@inai.de
- Update to snapshot 8.3.0~694
  * migration-pst: skip root folder without hard-coded name check
  * client: add extra checks for EID sizes to CompareEntryIDs
  * php-ext: use /usr/share/kopano/php for mapi classes
* Sun Jan 29 2017 jengelh@inai.de
- Update to snapshot 8.3.0~667
  * Changes:
  * server: make softdelete_lifetime config setting a reloadable
    property [KC-472]
  * icalmapi: handle missing timezone for RRULE [KC-414]
  * migration-pst: filter metadata at start of subject [KC-424]
* Tue Dec 20 2016 jengelh@inai.de
- Update to snapshot 8.3.0~334
  * Enhancements:
  * gateway, server: reload SSL certificates on SIGHUP [KC-301]
  * dagent: log_raw_message option can now be used selectively on
    users [KC-370]
  * Fixes:
  * gateway: report missing attachments over IMAP better [KC-436]
  * inetmapi: avoid overzealously generating winmail.dat [KC-348]
  * common: fix spurious crash in sk_SSL_COMP_free on shutdown
    [KC-443]
  * backup: improved logging when ACL does not resolve to
    user/group [KC-431]
  * migration-pst: show usage, not traceback, for invalid options
    [KC-372]
  * inetmapi: avoid buffer overread on rejected recipients
    (showed garbage in logs) [KC-398]
  * Changes:
  * server: compressed attachments now get the same permissions
    as uncompressed ones [KC-380]
  * backup: maintain deleted folders and add --purge N option
    [KC-376]
* Wed Dec  7 2016 jengelh@inai.de
- Update to 8.3 snapshot 223
  * Enhancements:
  * mapi: drop global lock and replace singleton allocmore table by
  per-object vectors [KC-328]
  * swig: expose group and company properties in Python [KC-320]
  * xapian-compact.py: new -c option to specify config file [KC-205]
  * utils: support setting out-of-office without an until-date [KC-275]
  * Fixes:
  * pyko: do not throw backtraces on log messages [KC-340]
  * server: S3 object sizes were shown wrongly [KC-351]
  * inetmapi: do not always generate winmail.dat [KC-348]
  * icalmapi: timezone search was broken [KC-313]
  * The RTF encoder incorrectly produced paragraphs where
  it should have created linefeeds [KC-338]
  * The RTF decoder failed to see that \uXXXX could start a paragraph [KC-338]
  * The RTF decoder erroneously created a new paragraph on \pard [KC-338]
  * server: Ctrl-C now works in gdb [KC-171]
  * inetmapi: avoid an infinite recursion on SMIME handling [KC-366]
  * ics: make creation of new syncids work incrementally [KC-208]
  * libserver: change incorrect compare operator for EID_V0 [KC-365]
  * Of special mention:
  * search: python3 support (but requires new python-xapian and,
  as a result, a db migration or full reindexing)
  * Developer/packager notes:
  * KC variables and functions now live in the KC:: C++ namespace [KC-369]
* Wed Nov 23 2016 jengelh@inai.de
- Update to 8.2 snapshot 451
  * == Fixes ==
  * dagent: iCal descriptions caused wrong body parts to be displayed [KC-138]
  * dagent: mr-process failed to copy attachments to the calendar item [KC-202]
  * dagent: restore/rework forced ASCII charset upgrade [KC-294]
  * == Enhancements ==
  * kopano-stats: bind 'q' key to exit as well [KC-105]
  * presence: log authentication errors
  * Improved PHP7 support [*,KC-330]
  * == Changes ==
  * search: log to file (if set) instead of stdout [KC-204]
  * search: treat '_' as a word break [KC-290]
  * swig: resolve crash when python programs end [KC-269]
  * config: change ldap_object_search_filter for WebApp to be able to
  search by mail address [KC-337]
  * gateway/client: avoid resynchronizing RTF body content [KC-338]
* Wed Nov  9 2016 jengelh@inai.de
- Update to 8.2 snapshot 397
  * == Fixes ==
  * backup: avoid exceptions on problematic rules/ACLs/delegates [KC-213,KC-266]
  * The comment for server.cfg's "disabled_features" was wrong [KC-262]
  * php: fix crash by adding missing pointer type conversions [KC-274]
  * dagent: the "Received" debugging header had the wrong target address
  * gateway: do not emit an X-Mailer field when retrieving mail [KC-277]
  * server/ldap: report empty ldap_search_base setting
  * client: verify peer's SSL certificate name [KC-156]
  * admin: support unwrapping "default:" type URLs [KC-289]
  * backup: fix tracebacks when used with ZCP [KC-306,KC-307,KC-308]
  * server: implement missing readback of compressed attachments [KC-285]
  * search: add script for findroot upgrade [KC-300]
  * php: ICS import/export functions [KC-302]
  * server: AWS4-HMAC-SHA256 support for S3 [KC-170]
  * pyko: permit "public@company" syntax to specify stores [KC-317]
  * dagent: new AUTORESPOND_BCC option for use with OOF [KC-319]
  * == Enhancements ==
  * PST importer [KC-59]
  * Python 3 support [KC-48,KC-267]
  * search: files are now compacted, and their uid/gid checked [KC-188]
  * server: allow search folder creation outside of own store [KC-271]
  * dagent: forwarding by rule can be restricted with a whitelist [KC-109]
  * == Changes ==
  * Non-Delivery Reports now originate from "Mail Delivery System"
  (like postfix) instead of yourself [KC-309]
  * Support for building with a no-SSLv2 OpenSSL 1.1. [KC-230]
  If you run such a setup, be aware that a config setting like
  "ssl_protocol = !SSLv2" in one or more of kopano-{server,gateway,ical}.cfg
  can inhibit the process from starting.
  * Cleanup of the example LDAP configuration files. [KC-229]
  /usr/share/doc/kopano/example-configs/ now has just a ldap.cfg,
  and no more ldap{,ms}.{active-directory,ldap}.cfg.
  * The example LDAP config file now has a different proposed value for
  ldap_object_search_filter for OpenLDAP. [KC-218]
  * spooler: messages with reminder will be sent with a TNEF copy [KC-152]
  * admin: group features will no longer be shown [KC-239]
