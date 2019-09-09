#
# spec file for package z-push
#
# Copyright (c) 2019 Mark Verlinde
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           z-push
Version:        2.4.5
Release:        0.1%{?dist}
Summary:        An implementation of Microsoft's ActiveSync protocol
License:        AGPL-3.0-only
Group:          Applications/Communications
Url:            https://stash.z-hub.io/projects/ZP/repos/z-push
Source:         https://github.com/Z-Hub/Z-Push/archive/2.4.5.tar.gz
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
Requires:       php-imap
Requires:       php-curl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Z-push is an implementation of the ActiveSync protocol which is used
'over-the-air' for multi platform ActiveSync devices.
Devices supported are including Windows Mobile, Android,
iPhone, and Nokia. With Z-push any groupware can
be connected and synced with these devices.

%prep
%setup -q -n Z-Push-%{version}
# fix shebang
sed -i 's|^#!/usr/bin/env |#!%{_bindir}/|' src/backend/kopano/listfolders.php \
 src/z-push-admin.php src/z-push-top.php

%build
#Prepare Licence and trademarks
mv  src/{LICENSE,TRADEMARKS} .


%install
mkdir -p %{buildroot}/%{_datarootdir}/z-push
cp -a src/* %{buildroot}/%{_datarootdir}/z-push/
rm -f %{buildroot}/%{_datarootdir}/z-push/INSTALL

mkdir -p %{buildroot}/%{_sysconfdir}/z-push
mkdir -p %{buildroot}/%{_sysconfdir}/z-push/backend
# Global config
mv %{buildroot}/%{_datarootdir}/z-push/config.php %{buildroot}/%{_sysconfdir}/z-push/config.php
ln -s %{_sysconfdir}/z-push/config.php %{buildroot}/%{_datarootdir}/z-push/config.php
# Kopano backend config
mv %{buildroot}/%{_datarootdir}/z-push/backend/kopano/config.php %{buildroot}/%{_sysconfdir}/z-push/backend/kopano.config.php
ln -s %{_sysconfdir}/z-push/backend/kopano.config.php %{buildroot}/%{_datarootdir}/z-push/backend/kopano/config.php
# Combined backend config
mv %{buildroot}/%{_datarootdir}/z-push/backend/combined/config.php %{buildroot}/%{_sysconfdir}/z-push/backend/combined.config.php
ln -s %{_sysconfdir}/z-push/backend/combined.config.php %{buildroot}/%{_datarootdir}/z-push/backend/combined/config.php
# IMAP backend config
mv %{buildroot}/%{_datarootdir}/z-push/backend/imap/config.php %{buildroot}/%{_sysconfdir}/z-push/backend/imap.config.php
ln -s %{_sysconfdir}/z-push/backend/imap.config.php %{buildroot}/%{_datarootdir}/z-push/backend/imap/config.php
# Caldav backend config
mv %{buildroot}/%{_datarootdir}/z-push/backend/caldav/config.php %{buildroot}/%{_sysconfdir}/z-push/backend/caldav.config.php
ln -s %{_sysconfdir}/z-push/backend/caldav.config.php %{buildroot}/%{_datarootdir}/z-push/backend/caldav/config.php
# Carddav backend config
mv %{buildroot}/%{_datarootdir}/z-push/backend/carddav/config.php %{buildroot}/%{_sysconfdir}/z-push/backend/carddav.config.php
ln -s %{_sysconfdir}/z-push/backend/carddav.config.php %{buildroot}/%{_datarootdir}/z-push/backend/carddav/config.php

mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
install -Dpm 644 %{SOURCE1} \
  %{buildroot}/%{_sysconfdir}/httpd/conf.d/z-push.conf
install -Dpm 644 %{SOURCE2} \
  %{buildroot}/%{_sysconfdir}/httpd/conf.d/z-push-autodiscover.conf
mkdir -p %{buildroot}/%{_localstatedir}/lib/z-push
mkdir -p %{buildroot}/%{_localstatedir}/log/z-push

%files
%doc LICENSE TRADEMARKS
%dir %{_sysconfdir}/z-push
%dir %{_sysconfdir}/z-push/backend
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/z-push/config.php
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/z-push/backend/kopano.config.php
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/z-push/backend/combined.config.php
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/z-push/backend/imap.config.php
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/z-push/backend/caldav.config.php
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/z-push/backend/carddav.config.php
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/httpd/conf.d/z-push.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/httpd/conf.d/z-push-autodiscover.conf
%{_datarootdir}/z-push/
%attr(750,apache,apache) %dir %{_localstatedir}/lib/z-push
%attr(750,apache,apache) %dir %{_localstatedir}/log/z-push


%changelog
* Mon Sep 09 2019 Mark Verlinde <mark.verlinde@gmail.com> - 2.4.5-0.1
- refactor spec for (centos) el7 build
* Sat Jan 19 2019 Luigi Baldoni <aloisio@gmx.com>
- Update to version 2.4.5 from new source repository
  Bug:
  * [ZP-1225] - GAL search returns username as email address
  * [ZP-1447] - php-mbstring is needed on Debian 9 as well
  * [ZP-1449] - Private items stripped in own calendar when
    calendar folder is also configured as share
  * [ZP-1452] - Fix logrotate for RHEL6
  * [ZP-1455] - nginx: change location from regex match to
    prefix match
  * [ZP-1456] - Categories are lost when marking email
    read/unread on shared account
  * [ZP-1457] - FirstDayOfWeek missing for recurring tasks
  Improvement:
  * [ZP-1438] - RHEL 7 packages are incompatible with Remi PHP
    7.x packages
  version 2.4.4:
  Bug
  * [ZP-454] - Error deleting an occurrence on a mobile device
  * [ZP-1014] - z-push/include/z_caldav.php:585 Undefined index:
    urn:ietf:params:xml:ns:caldav:calendar-home-set
    (8)
  * [ZP-1437] - Send range in ItemOperations response
  * [ZP-1440] - Outlook EAS break meeting request
  * [ZP-1444] - KOE webservices calls fail for impersonated
    stores
  * [ZP-1445] - MAPI_E_STORE_FULL handling in SendMail()
  New Feature
  * [ZP-1442] - Retry loop when writing file state machine data
    to disk
  version 2.4.3:
  Epic
  * [ZP-1402] - PHP 7.2 compatibility
  Research
  * [ZP-1407] - $errcontext argument of error handlers has been
    deprecated
  Bug
  * [ZP-1330] - PHP 7.2, warnings in logs about implementing
    Countable
  * [ZP-1405] - create_function() has been deprecated
  * [ZP-1406] - each() has been deprecated
  * [ZP-1418] - IMAP Backend: imap_fetch_overview might return
    an empty array
  * [ZP-1419] - Structurally dead code (UNREACHABLE)
  * [ZP-1420] - Typo in identifier (IDENTIFIER_TYPO)
  * [ZP-1421] - Expression with no effect (NO_EFFECT)
  * [ZP-1422] - Expression with no effect (NO_EFFECT)
  * [ZP-1423] - Nesting level does not match indentation
    (NESTING_INDENT_MISMATCH)
  * [ZP-1424] - Typo in identifier (IDENTIFIER_TYPO)
  * [ZP-1425] - Expression with no effect (NO_EFFECT)
  * [ZP-1426] - Logically dead code (DEADCODE)
  * [ZP-1427] - Undefined index in mapiprovider
  * [ZP-1429] - IMAP backend, send emailaddress to
    reply_meeting_calendar
  * [ZP-1430] - Wrong IpcWincacheProvider path in
    InterProcessData
  * [ZP-1431] - Z-Push logrotate cron su file permissions
  * [ZP-1434] - X-Forwarded-For header might contain multiple IPs
  * [ZP-1436] - Z-Push log files not writable after logrotate
  Improvement
  * [ZP-1416] - List opened shares in z-push-admin
  version 2.4.2:
  Bug
  * [ZP-1369] - Impersonation: ReplyBack notification mail can
    not get folder name
  * [ZP-1386] - include/mimeDecode.php:541 Uninitialized string
    offset: 0 (8)
  * [ZP-1391] - IMAP Backend: Users cannot authenticate against
    IMAP servers with GSSAPI support
  * [ZP-1396] - CalDAV Attendee but no meeting
  * [ZP-1399] - Wrong state and log folder permissions for RHEL
    based systems
  * [ZP-1400] - Picture not saved for a contact created on mobile
  * [ZP-1408] - Warning Undefined index: subject
  * [ZP-1410] - IMAP backend to provide user details for caldav
  * [ZP-1411] - Unset undefined properties for tasks
  * [ZP-1412] - Add ignore_missing_attachments option to
    mapi_inetmapi_imtoinet
  New Feature
  * [ZP-1372] - Folder re-sync is triggered on deletions ratio
    threshold
  Improvement
  * [ZP-1398] - z-push-admin do not call
    $device->GetHierarchyCache() in loop
  * [ZP-1401] - In gab2contacts also sync Kopano contacts
  * [ZP-1413] - deb: Turn php dependencies around
  version 2.4.1:
  Bug
  * [ZP-1291] - Cli tools should exit with 0 if called with
  - -help
  * [ZP-1373] - USE_CUSTOM_REMOTE_IP_HEADER not working with
    Apache
  * [ZP-1374] - Include path in imap backend lacks pear folders
  * [ZP-1375] - z-push-config-nginx has wrong permissions in RPM
  * [ZP-1376] - Out-of-memory check when memory_limit = -1
  * [ZP-1377] - Undefined index warnings in imap backend
  * [ZP-1379] - Undefined offset warnings when impersonating
  * [ZP-1383] - CARDDAV: Last character of note trimmed
  * [ZP-1392] - Default backend, Warning about non existing
    $userinformation
  Improvement
  * [ZP-1382] - CALDAV: Out of office / Tentative /
    Workingelsewhere status
  version 2.4.0:
  Epic
  * [ZP-596] - ActiveSync 14.1 related issues and tasks
    Research
  * [ZP-1233] - Meeting requests default to GMT timezone
  * [ZP-1313] - Remove TNEF class
    Story
  * [ZP-1205] - Set custom sync period per store
  Bug
  * [ZP-295] - AS 14.1: Implement FirstDayOfWeek for recurring
    items
  * [ZP-836] - Recurring tasks duplicate in OL 2016
  * [ZP-1051] - z-push/include/mimeDecode.php:902 mb_strlen():
    Unknown encoding "windows-1250"
  * [ZP-1162] - Create a nginx config package
  * [ZP-1267] - Change summed mapi tags
  * [ZP-1270] - Unknown origin and warnings when listing
    configured shared folders via API
  * [ZP-1276] - Error in logging when sending email with imap
    backend: Only variables should be assigned by
    reference
  * [ZP-1287] - Editing appointment by owner creates new
    appointment
  * [ZP-1294] - FixFileOwner requires posix_getuid which fails
    on Windows
  * [ZP-1307] - Unable to accept Meeting Request on iOS 11
  * [ZP-1308] - Incompatible PHP 5.4 code in FileStateMachine
  * [ZP-1315] - Carddav backend, EMAIL should only contain email
    address
  * [ZP-1318] - Caldav only set ORGANIZER if ATTENDEE
  * [ZP-1319] - Caldav only save DESCRIPTION if it's not empty
  * [ZP-1320] - Caldav X-MICROSOFT-CDO-ALLDAYEVENT support
  * [ZP-1321] - Carddav support rare phone types
  * [ZP-1322] - All-day event created in Outlook stretches over
    2 days in Webapp
  * [ZP-1324] - Carddav, $message->asbody->data can be NULL
  * [ZP-1326] - AirWatch Boxer not working on iOS
  * [ZP-1329] - Refactor impersonation feature
  * [ZP-1339] - Replace removed PHP-MAPI functions
  * [ZP-1344] - Reply back exporter doesn't honor private flag
  * [ZP-1345] - Own private items stripped when folder is in
    $additionalFolders
  * [ZP-1347] - [imap] Creating folder on mobile fails
  * [ZP-1348] - Use of undefined constants in email with
    attachments
  * [ZP-1350] - Erroneous mapi_last_hresult value when source
    message is not found while moving
  * [ZP-1352] - Impersonation: check read permissions on all
    folders on FolderSync
  * [ZP-1353] - Check user vs authUser case-insensitive for log
  * [ZP-1354] - Basedate in GlobalObjectId must be GMT
  * [ZP-1355] - Auth username when impersonating is always
    lowercase
  * [ZP-1356] - Log output without impersonated user
  * [ZP-1361] - Folder created in impersonated store is not
    FLD_ORIGIN_IMPERSONATED
  * [ZP-1370] - Impersonation: public folder can't be opened
  New Feature
  * [ZP-742] - Implement OnlineMeeting*Link
  * [ZP-743] - Implement Picture for ResolveRecipients
  * [ZP-744] - Implement Picture for Search
  * [ZP-745] - Implement BodyPart and BodyPartPreference
  * [ZP-746] - Implement PrimarySmtpAddress in Settings
  * [ZP-747] - Implement Accounts in Settings
  * [ZP-748] - Implement RightsManagementInformation
  * [ZP-758] - Implement MeetingMessageType
  * [ZP-1104] - Have a device specific log file
  * [ZP-1121] - Output opaque data
  * [ZP-1165] - Tools: z-push-admin could have an option to
    delete profiles older than X days
  * [ZP-1192] - Expose shared folder API to z-push-admin
  * [ZP-1271] - Impersonate shared folders with own credentials
  * [ZP-1305] - Show KOE last connection time in z-push-admin
  * [ZP-1332] - Add wincache IPC provider
  Task
  * [ZP-753] - Add ASV 14.1 constant to zpush.php
  * [ZP-1303] - [nginx] write documentation about configuration
  Improvement
  * [ZP-1122] - Sync loop failsafe - check for out-of-memory
    condition
  * [ZP-1145] - Support fpm in webserver config packages
  * [ZP-1153] - Debian packaging: run tools als webserver user
  * [ZP-1161] - Update Nginx config
  * [ZP-1183] - Use custom header for remote IP (e.g.
    HTTP_X_REAL_IP)
  * [ZP-1206] - Statically configured folders can not have flags
  * [ZP-1209] - AutoDiscover: config parameter to get a valid
    username
  * [ZP-1214] - AutoDiscover should check for credentials even
    in GET requests
  * [ZP-1235] - Improve guessTZNameFromPHPName
  * [ZP-1242] - Check for cpid directly instead of getting
    charset
  * [ZP-1258] - Use PR_EC_IMAP_EMAIL to get RFC822 data
  * [ZP-1260] - Improve isset in ASDevice->GetFolderSyncStatus()
  * [ZP-1261] - Reduce amount of repeated glob calls
  * [ZP-1283] - Build rh-php56-php-memcached for RHEL 6+7 with
    SCL
  * [ZP-1284] - Add Note Backend operating against Postgres
    database
  * [ZP-1295] - Merge MAPI classes from webapp
  * [ZP-1304] - Refactoring in MAPI classes
  * [ZP-1327] - Add KOE Impersonate feature flag
  * [ZP-1331] - Create z-push group for rpm packages
  * [ZP-1340] - Review stream writes
  * [ZP-1357] - Private items aren't stripped of data when
    impersonating
  * [ZP-1360] - Remove ICalParser class
  * [ZP-1367] - Tools: gab-sync shows weird behavior when
    php-mapi includes are wrong
- Added _service
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
