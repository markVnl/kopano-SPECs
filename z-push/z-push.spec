#
# spec file for package z-push
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


%define wwwroot %{_prefix}/share
%define zpush_dir %{wwwroot}/z-push
Name:           z-push
Version:        2.3.9
Release:        2.2
Summary:        An implementation of Microsoft's ActiveSync protocol
License:        AGPL-3.0
Group:          Productivity/Networking/Email/Utilities
Url:            http://z-push.sourceforge.net/
Source:         http://download.z-push.org/final/2.3/z-push-%{version}.tar.gz
Source1:        z-push.conf
Source2:        z-push-autodiscover.conf
Requires:       php >= 5.4
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-pcntl
Requires:       php-posix
Requires:       php-soap
Requires:       php-sysvmsg
Requires:       php-sysvsem
Requires:       php-sysvshm
Recommends:     php-imap
Recommends:     php-curl
Suggests:       apache2
Suggests:       mod_php_any
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Z-push is an implementation of the ActiveSync protocol which is used
'over-the-air' for multi platform ActiveSync devices.
Devices supported are including Windows Mobile, Android,
iPhone, and Nokia. With Z-push any groupware can
be connected and synced with these devices.

%prep
%setup -q

%build

%install
mkdir -p "%{buildroot}/%{zpush_dir}"
cp -a * "%{buildroot}/%{zpush_dir}/"
rm -f "%{buildroot}/%{zpush_dir}/"{INSTALL,LICENSE}

mkdir -p "%{buildroot}/%{_sysconfdir}/z-push";
mkdir -p "%{buildroot}/%{_sysconfdir}/z-push/backend";
# Global config
mv "%{buildroot}/%{zpush_dir}/config.php" "%{buildroot}/%{_sysconfdir}/z-push/config.php";
ln -s "%{_sysconfdir}/z-push/config.php" "%{buildroot}/%{zpush_dir}/config.php";
# Kopano backend config
mv "%{buildroot}/%{zpush_dir}/backend/kopano/config.php" "%{buildroot}/%{_sysconfdir}/z-push/backend/kopano.config.php";
ln -s "%{_sysconfdir}/z-push/backend/kopano.config.php" "%{buildroot}/%{zpush_dir}/backend/kopano/config.php";
# Combined backend config
mv "%{buildroot}/%{zpush_dir}/backend/combined/config.php" "%{buildroot}/%{_sysconfdir}/z-push/backend/combined.config.php";
ln -s "%{_sysconfdir}/z-push/backend/combined.config.php" "%{buildroot}/%{zpush_dir}/backend/combined/config.php";
# IMAP
mv "%{buildroot}/%{zpush_dir}/backend/imap/config.php" "%{buildroot}/%{_sysconfdir}/z-push/backend/imap.config.php";
ln -s "%{_sysconfdir}/z-push/backend/imap.config.php" "%{buildroot}/%{zpush_dir}/backend/imap/config.php";
# Caldav
mv "%{buildroot}/%{zpush_dir}/backend/caldav/config.php" "%{buildroot}/%{_sysconfdir}/z-push/backend/caldav.config.php";
ln -s "%{_sysconfdir}/z-push/backend/caldav.config.php" "%{buildroot}/%{zpush_dir}/backend/caldav/config.php";
# Carddav
mv "%{buildroot}/%{zpush_dir}/backend/carddav/config.php" "%{buildroot}/%{_sysconfdir}/z-push/backend/carddav.config.php";
ln -s "%{_sysconfdir}/z-push/backend/carddav.config.php" "%{buildroot}/%{zpush_dir}/backend/carddav/config.php";

mkdir -p "%{buildroot}/%{_sysconfdir}/apache2/conf.d";
install -Dpm 644 %{SOURCE1} \
	"%{buildroot}/%{_sysconfdir}/apache2/conf.d/z-push.conf";
install -Dpm 644 %{SOURCE2} \
	"%{buildroot}/%{_sysconfdir}/apache2/conf.d/z-push-autodiscover.conf";
mkdir -p "%{buildroot}/%{_localstatedir}/lib/z-push";
mkdir -p "%{buildroot}/%{_localstatedir}/log/z-push";

%files
%defattr(-, root, root)
%dir %{_sysconfdir}/z-push
%dir %{_sysconfdir}/z-push/backend/
%config(noreplace) %attr(0640,root,www) %{_sysconfdir}/z-push/config.php
%config(noreplace) %attr(0640,root,www) %{_sysconfdir}/z-push/backend/kopano.config.php
%config(noreplace) %attr(0640,root,www) %{_sysconfdir}/z-push/backend/combined.config.php
%config(noreplace) %attr(0640,root,www) %{_sysconfdir}/z-push/backend/imap.config.php
%config(noreplace) %attr(0640,root,www) %{_sysconfdir}/z-push/backend/caldav.config.php
%config(noreplace) %attr(0640,root,www) %{_sysconfdir}/z-push/backend/carddav.config.php
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/apache2/conf.d/z-push.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/apache2/conf.d/z-push-autodiscover.conf
%{zpush_dir}/
%attr(750,wwwrun,www) %dir %{_localstatedir}/lib/z-push
%attr(750,wwwrun,www) %dir %{_localstatedir}/log/z-push
%doc LICENSE TRADEMARKS

%changelog
* Thu Feb  8 2018 bosim@opensuse.org
- Updated to 2.3.9
  * [ZP-1339] Replace removed PHP-MAPI functions
  * [ZP-1344] Reply back exporter doesn't honor private flag
  * [ZP-1345] Own private items stripped when folder is in
    $additionalFolders
* Sun Jan 21 2018 bosim@opensuse.org
- Added missing "php-pcntl" for z-push-top to work
* Mon Oct  2 2017 bosim@opensuse.org
- Updated to 2.3.8
  * [ZP-1248] Include WindowsMail in the list of long timeout
    clients
  * [ZP-1259] Check if sm->data is empty for SendMail
  * [ZP-1164] Upgrading z-push-common could take a very long time
  * [ZP-1211] php-memcached not available on CentOS
  * [ZP-1223] running z-push-top as root destroy /dev/null
  * [ZP-1224] [caldav] Pass PHP supported timezone to DateTimeZone
  * [ZP-1230] Windows Phone 8.1 - Data can not be retrieved via
    ItemOperations
  * [ZP-1238] Resources booked in Outlook are saved as "required"
    attendees
  * [ZP-1239] WP 8.1 sends client changes and fetch in one request
  * [ZP-1240] HTML bodies should not be truncated within HTML tags
  * [ZP-1241] Don't perform heartbeat in empty sync requests
  * [ZP-1244] Caldav never matches personal/main calendars/tasks if
    defined CALDAV_PERSONAL has uppercase characters
  * [ZP-1247] Unexpected synckey (StateInvalidException) for backends
    without FolderStats support
  * [ZP-1249] WP 8.1: Empty sync + empty response trigger loop
  * [ZP-1250] Send-As is detected erroneously
  * [ZP-1251] z-push-top: too much output from Ping response
  * [ZP-1254] Wastebasket not available when removing an item in
    public folder
  * [ZP-1255] Send-as not working for other companies
  * [ZP-1256] z-push-admin -a resync -t FOLDERID -u USER does not
    work
  * [ZP-1257] Removing a folder added in $additionalFolders from
    config.php fails with KOE
  * [ZP-1262] Synchronization progress of z-push-admin shows Folder:
    unknown
  * [ZP-1268] Undefined variable: name in z-push-admin
  * [ZP-1269] Carddav backend, newlines result in an invalid vcard
  * [ZP-1273] Missing warnings for autodiscover
  * [ZP-1274] Carddav backend, wrong url in debug logging
  * [ZP-1275] GAL does not work with DAViCal backend
  * [ZP-1277] Fatal error in Ping
  * [ZP-1278] Caldav Backend does not pick up user and domain;
    results in non-editable events on Exchange device (E.g. phones)
  * [ZP-1279] Imap backend delete
  * [ZP-1280] Email from a deleted user doesn't show from
  * [ZP-1281] ":" not escaped when creating icalendar
  * [ZP-1282] Store deleted occurrences as EXDATE in caldav
  * [ZP-1285] Caldav time zone incorrectly converted
  * [ZP-1286] Unable to delete an appointment on mobile phone
* Sun Jun 25 2017 bosim@opensuse.org
- Updated to 2.3.7
  * [ZP-1177] KOE: private appointments in shared folders are not
    visible after making them public
  * [ZP-1197] Add a flag to WebserviceDevice->GetDeviceDetails() to
    (not) include hierarchy cache
  * [ZP-1200] IPv6 address not logged correctly (Contributed by
    Chris Pitchford - Thanks!)
  * [ZP-1204] Process delivery request from KOE
  * [ZP-1227] Prioritize KOE GAB sync
  * [ZP-1243] Always send X-Push-Capabilities header in Settings
    response (hotfix to 2.3.7beta1)
  * [ZP-1196] Warning in gab-sync with hidden groups
  * [ZP-1198] WebserviceDevice->GetDeviceDetails() should not
    return hierarchy cache
  * [ZP-1199] Truncating emails can result in invalid strings
  * [ZP-1201] Settings command triggered by KOE always
    overwrites device data
  * [ZP-1208] Meeting shows up twice in Outlook calendar
  * [ZP-1210] Not possible to install z-push-kopano-gabsync on
    CentOS/RHEL/Fedora
  * [ZP-1212] Folder stat data expiration time should be randomized
  * [ZP-1215] Error on generating first sync state if
    GlobalWindowSize is full
  * [ZP-1219] Introduce hidden debugging flag for WBXML decoder
  * [ZP-1220] Outlook is "disconnected" after adding a Contact
    folder
  * [ZP-1221] Unable to create OL2013 profile when password
    contains special chars
  * [ZP-1228] Accept folders with type "OTHER" as shared folders
  * [ZP-1229] Strict type checking in SyncObject.equals() may break
    other backends (Contributed by Vincent Sherwood aka.
    liverpoolfcfan - Thanks!)
* Sat May  6 2017 bosim@opensuse.org
- Updated to 2.3.6
  * ZP-1155 REVERT: [IMAP] iOS mail with z-push preview show
    raw html
  * ZP-1179 folderid not mapped when deleting
  * ZP-1191 Z-Push 2.3.5 breaks CentOS updates / libawl invalid
    dependency
  * ZP-1135 Update licenses of forked PEAR classes to be compatible
    with Debian (includes ZP-1152, ZP-1187, ZP-1189, ZP-1193)
    (thanks to Roel for achieving this!)
  * ZP-1168 Log wait time in INFO level
  * ZP-1178 Use PR_SEARCH_KEY in cases the GAB entry of a
    recipient is not available
  * ZP-1190 Missing manpages for installed binaries
    (thanks to Roel for contributing)
  * ZP-1195 Expose WebserviceDevice->GetDeviceDetails() for a
    single device
  * ZP-1163 Warning when install z-push-common on a new system
  * ZP-1167 [IMAP] Some new messages are outdated and lost when sync
  * ZP-1169 Kopano MAPI_E_UNCONFIGURED (0x8004011C) causes a folder
    resync
  * ZP-1172 [IMAP] Some mails bodies or headers in Japanese may be
    decoded in wrong encoding
  * ZP-1180 Implement plain streams for CalDav and CardDav backends
  * ZP-1182 WARN messages doesn't log into z-push-error.log
  * ZP-1185 Messages in error log are duplicated
  * ZP-1186 Folder created under root in Outlook is not synced
  * ZP-1188 Check if OOF expired and disabled it if needed
* Tue Mar 28 2017 bosim@opensuse.org
- changed config prefix from /etc/kopano/ to /etc/z-push/
- added combined, imap, caldav, carddav config files to
  /etc/z-push/backend
- removed %%{buildroot} alias ($b)
- ran spec-cleaner on z-push.spec
* Wed Mar 15 2017 bosim@opensuse.org
- Updated to 2.3.5
* Fri Mar 10 2017 bosim@opensuse.org
- Added autodiscover configuration
* Thu Jan 26 2017 bosim@opensuse.org
- Updated to 2.3.4
