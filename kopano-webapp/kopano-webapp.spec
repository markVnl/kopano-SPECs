#
# spec file for package kopano-webapp
#
# Copyright (c) 2017 Mark Verlinde
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

%define release 0.3

%define langdir %{_datadir}/%{name}/server/language
%define plugindir %{_datadir}/%{name}/plugins

Name:           kopano-webapp
Version:        3.4.19
Release:        %release%{?dist}
Summary:        Improved WebApp for Kopano

License:        AGPL-3.0
Url:            https://kopano.io
Source:         https://github.com/Kopano-dev/kopano-webapp/archive/v%{version}.tar.gz

BuildRequires:  ant
BuildRequires:  xz
BuildRequires:  libxml2

Requires:       %{name}-lang = %{version}
Requires:       rh-php71
Requires:       rh-php71-php-common
Requires:       php71-mapi

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provides a web-client written in PHP that makes use of Jason and ExtJS
to allow users to make full use of the Kopano platform
through a modern web browser.

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Languages for package %{name}
Group:          System Environment/Base

%description lang
Provides translations to the package %{name}.

%package contactfax
Summary:        Contact fax plugin for kopano-webapp
Group:          Applications/Communications

%description contactfax
Opens a new "create mail" dialog with contact's fax number in the To:
field of the email.

%package folderwidgets
Summary:        Folder widgets plugin for kopano-webapp
Group:          Applications/Communications

%description folderwidgets
A collection of widgets which can show the contents of some of the
default folders for a user.

%package gmaps
Summary:        Google Maps plugin for kopano-webapp
Group:          Applications/Communications

%description gmaps
Shows contact address on Google Maps.

%package pimfolder
Summary:        Plugin for kopano-webapp to quickly move mail into another folder
Group:          Applications/Communications

%description pimfolder
Kopano PIM plugin, allows you to set-up a folder quickly moving your mail to another folder; like "Archive" in GTD

%package quickitems
Summary:        Quick Items plugin for kopano-webapp
Group:          Applications/Communications

%description quickitems
Special widgets for easily creating new Mails, Appointments, Contacts,
Tasks and Notes.

%package titlecounter
Summary:        Title counter plugin for kopano-webapp
Group:          Applications/Communications

%description titlecounter
Plugin to show number of unread messages in the window title.

%package webappmanual
Summary:        Manual plugin for kopano-webapp
Group:          Applications/Communications

%description webappmanual
Plugin with manual for Kopano WebApp

%package zdeveloper
Summary:        Developer plugin for kopano-webapp
Group:          Development/Tools

%description zdeveloper
Shows all available insertion points on the screen.

%prep
%setup -q
find . -type f "(" -name "*.js" -o -name "*.php" ")" \
  -exec chmod a-x "{}" "+";
echo "%{version}" > version

%build
ant deploy deploy-plugins;

%install

mkdir -p "%{buildroot}/%{_datadir}";
cp -a deploy "%{buildroot}/%{_datadir}/%{name}";
mkdir -p "%{buildroot}/%{_sysconfdir}/httpd/conf.d"
mv "%{buildroot}/%{_datadir}/%{name}/kopano-webapp.conf" "%{buildroot}/%{_sysconfdir}/httpd/conf.d"
mkdir -p "%{buildroot}/%{_sysconfdir}/kopano/webapp"
mv "%{buildroot}/%{_datadir}/%{name}/config.php.dist" "%{buildroot}/%{_sysconfdir}/kopano/webapp/config.php"
ln -s "%{_sysconfdir}/kopano/webapp/config.php" \
  "%{buildroot}/%{_datadir}/%{name}/config.php"
rm "%{buildroot}/%{_datadir}/%{name}/debug.php.dist"
mkdir -p "%{buildroot}%{_localstatedir}/lib/%{name}/tmp"

%files
%defattr(-,root,root)
%{_datadir}/%{name}
%exclude %{plugindir}/*
%exclude %{langdir}
%dir %{_sysconfdir}/kopano
%dir %{_sysconfdir}/kopano/webapp
%config(noreplace) %{_sysconfdir}/kopano/webapp/config.php
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%config(noreplace) %{_sysconfdir}/httpd/conf.d/kopano-webapp.conf
%dir %{_localstatedir}/lib/kopano-webapp
%dir %attr(0775, apache, apache) %{_localstatedir}/lib/kopano-webapp/tmp

%files lang
%defattr(-,root,root)
%dir %{langdir}
#lang(bg_BG) %%langdir/bg_BG.UTF-8
%lang(ca_ES) %{langdir}/ca_ES.UTF-8
%lang(cs_CZ) %{langdir}/cs_CZ.UTF-8
%lang(da_DK) %{langdir}/da_DK.UTF-8
%lang(de_DE) %{langdir}/de_DE.UTF-8
%lang(el_GR) %{langdir}/el_GR.UTF-8
%lang(en_US) %{langdir}/en_US.UTF-8
%lang(es_CA) %{langdir}/es_CA.UTF-8
%lang(es_ES) %{langdir}/es_ES.UTF-8
%lang(et_EE) %{langdir}/et_EE.UTF-8
%lang(fa_IR) %{langdir}/fa_IR.UTF-8
%lang(fi_FI) %{langdir}/fi_FI.UTF-8
%lang(fr_FR) %{langdir}/fr_FR.UTF-8
%lang(gl_ES) %{langdir}/gl_ES.UTF-8
%lang(he_IL) %{langdir}/he_IL.UTF-8
%lang(hr_HR) %{langdir}/hr_HR.UTF-8
%lang(hu_HU) %{langdir}/hu_HU.UTF-8
%lang(it_IT) %{langdir}/it_IT.UTF-8
%lang(ja_JP) %{langdir}/ja_JP.UTF-8
%lang(ko_KR) %{langdir}/ko_KR.UTF-8
%lang(lt_LT) %{langdir}/lt_LT.UTF-8
%lang(nb_NO) %{langdir}/nb_NO.UTF-8
%lang(nl_NL) %{langdir}/nl_NL.UTF-8
%lang(pl_PL) %{langdir}/pl_PL.UTF-8
%lang(pt_BR) %{langdir}/pt_BR.UTF-8
%lang(pt_PT) %{langdir}/pt_PT.UTF-8
%lang(ru_RU) %{langdir}/ru_RU.UTF-8
%lang(sl_SI) %{langdir}/sl_SI.UTF-8
%lang(sv_SE) %{langdir}/sv_SE.UTF-8
%lang(tr_TR) %{langdir}/tr_TR.UTF-8
%lang(uk_UA) %{langdir}/uk_UA.UTF-8
%lang(zh_CN) %{langdir}/zh_CN.UTF-8
%lang(zh_TW) %{langdir}/zh_TW.UTF-8

%files contactfax
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/contactfax

%files folderwidgets
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/folderwidgets

%files gmaps
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/gmaps

%files pimfolder
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/pimfolder

%files quickitems
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/quickitems

%files titlecounter
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/titlecounter

%files webappmanual
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/webappmanual

%files zdeveloper
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/zdeveloper

%changelog
* Thu Aug 09 2018 mark.verlinde@gmail.com
- Update to 3.4.19
  * == Fixes ==	 
  - KW-1958 Country code jumps to the wrong field
  - KW-2528 Basic shortcuts are not enabled by default when kopano-files is not installed
  - KW-2705 Broken members of distributionlist break the whole list
  - KW-1728 Xss injection via description and image urls in what’s new dialog
  - KW-2237	Removing attachment and send meeting request still have the attachment
  - KW-2575	Canceled attachments are still uploaded
  - KW-2685	Xss via components names
  - KW-2688	Deleting a gab user which is part of a distribution list breaks the list
  - KW-2689	Accepting meeting request in shared store throws error
  - KW-1277	Task request data not visible when previewing in small window
  - KW-1890	German spellchecker marks some common abbreviation as incorrect
  - KW-2384	Deleting a kopano-contact removes mailaddress in existing mails
  - KW-2509	Unable to download attachment from popout and preview pane
  - KW-2539	Large folder structures get scrambled after copying a folder
  - KW-2632	Opening task / todo folder in embedded window throws error
  - KW-2661	Undefined offset errors when opening a task request
  - KW-428 	Clicking outside of the copy/move dialog selects a folder
  - KW-872 	Error occurs when editing local contact via address book
  - KW-1194	“add new...” e-mail address dialog has too much height by default
  - KW-1362	Webapp should handle ‘broken’ freebusy entryid
  - KW-2317	Mail sent as attachment can’t be imported
  - KW-2360	Html ampersand code visible in link
  - KW-2383	Organizer should be updated when selected “create in calendar” is changed
  - KW-2436	Losing category when receiving update for meeting request
  - KW-2452	Send as email when selecting contact, distribution list and email freezes the to send email
  - KW-2526	Unable to delete assigned tasks from public folder
  - KW-2546	Infinite scroll loading information is not reset when switching folders
  - KW-2584	Unable to delete search folder when it contains messages
  - KW-2625	Unable to upload certificates
  - KW-2626	Hover card is missing send new mail icon
  - KW-2651	Invalid html in notifier message
  * == Enhancements == 	 
  - KW-1969	Add to favorites dialog remove ‘folder name’
  - KW-2267	Refactor reminder dialog iconclass code
  - KW-2604	Build webapp for ucs 4.3
  - KW-2612	Ucs 4.3 spellchecker plugin support
  - KW-2613	Ucs 4.3 support for plugin mattermost
  - KW-2614	Ucs 4.3 support for desktop notification plugin
  - KW-1127	Notes: remove unused functions
  - KW-2127	Add category as an optional filter in search tools
  - KW-2212	Open reminder dialog from reminder button in menu bar
  - KW-2564	Add support for simple json themes
  - KW-2606	Use mapi_deferred_errors flag when opening a table
  - KW-2654	Refactor common code
  - KW-463 	Reloading pop-out should not clear unsaved content
  - KW-2322	Reposition pagination panel of the mail grid
  - KW-2335	Introduce possibility to show more information about ‘message could not be saved’
  - KW-2556	Improve loading of recurrences
  - KW-2588	Add delay to hover card pop-up
  - KW-2598 Implement dark tooltips
* Mon Jun 11 2018 mark.verlinde@gmail.com
- Sanitize spec for (centos) el7 build
- Update to 3.4.15final
  * == Full changelog ==
  * https://documentation.kopano.io/kopano_changelog/webapp.html
* Wed May 16 2018 bosim@opensuse.org
- Update to 3.4.13
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Fri Apr  6 2018 bosim@opensuse.org
- Update to 3.4.10
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Fri Feb  9 2018 bosim@opensuse.org
- Update to 3.4.5 final, improvements:
  * KW-420 Improve “sorting not possible” text in search
  * KW-612 Import e-mail (eml) from attachment
  * KW-1535 Set a flag on a task item
  * KW-2100 Detect closing or adding newly opened calendar in a mr
- Bugfixes:
  * KW-1604 Error thrown when opening previously favorited shared
    search folder of re-opened shared store
  * KW-1948 [ie11] [edge] saving attachment with umlauts results in
    a scrambled file name
  * KW-2028 Attachment not send when address book is open while
    auto-saving
- Full changelog:
https://documentation.kopano.io/kopano_changelog/webapp.html
* Mon Jan 22 2018 bosim@opensuse.org
- Suggesting php-opcache (speeds up WebApp quite some)
* Sat Jan 20 2018 bosim@opensuse.org
- Update to 3.4.4 final, improvements:
  * KW-1098 Indicate in which calendar an appointment will be
    created
  * KW-2060 Make setdefaultsignature python 3 compatible
  * KW-2204 Webapp opens the public store on every request
  * KW-2205 Webapp lazy load settings
  * KW-2218 Reduce timeout delay for showing suggestions
  * KW-2222 Add jenkinsfile for running tests in webapp repository
  * KW-2230 Ship basic apparmor profiles
- Bugfixes:
  * KW-2091 Distribution list not shown as suggested recipient
  * KW-2257 Uncaught type error after upgrade to webapp 3.4.3
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Tue Jan  9 2018 bosim@opensuse.org
- Updated to 3.4.3 final, improvements:
  * KW-664 Resolve multiple email addresses correctly when pasting
    from other applications
  * KW-1908 Mark incomplete icon is not aligned
  * KW-1999 Change context menu location of export e-mail as eml or
    zip
  * KW-2051 Mark for follow-up flag menu in tasks can not be opened
    by left click
  * KW-2171 Update code using php-ext function aliases
  * KW-2209 Integrate js unit tests in webapp repository
  * KW-2221 Rename ‘send as attachment’ to ‘send to...’
- Bugfixes:
  * KW-1713 Setting a phonenumber extension will create a x as
    seperator
  * KW-1740 Checkbox is not checked in multi select hierarchy
  * KW-1945 Text is gone when typing text in the calendar while its
    being refreshed
  * KW-2046 Clicking a flagged e-mail in reminder pop up does not
    show e-mail
  * KW-2096 Flagged mail icon not shown in reminder dialog
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Wed Dec 13 2017 bosim@opensuse.org
- Updated to 3.4.2 final, improvements:
  * KW-1465 Use profile save/restore from php-mapi to speed up login
  * KW-1473 Restyle reminder column
  * KW-2061 Remove dead and unused code
  * KW-2062 Reduce maximum allowed nesting level in webapp
- Bugfixes:
  * KW-1588 Mail address does not appear in suggestion list
  * KW-1642 Custom flagged e-mails without reminder with due_by date
  in the past are not red colored
  * KW-1787 Initial gab sort order ascending (a-z)
  * KW-1803 3 dotted ‘more’ menu can not be opened
  * KW-1838 Blue color shown twice in color panel
  * KW-1852 Calendar item can not be saved when public calendar is
  opened from favorites
  * KW-1858 To-do list is written wrong
  * KW-2032 Ff - calendar canvas breaks in month view
  * KW-2159 No-date flag can not have reminder when set through
  ‘custom’ dialog
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Fri Dec  1 2017 bosim@opensuse.org
- Updated to 3.4.1 final, improvements:
  * Short time and date in list view
  * Visualize active calendar
- Bugfixes:
  * KW-1840 Category should not be sent with task- and meeting
    requests
  * KW-1874 Recurrence window is blank while pasting recurrence
    series
  * KW-1876 Pasting single occurrence will open recurrence window
    sometimes
  * KW-1940 Webapp forgets that it accepted a meeting request
  * KW-2119 Hierarchy breaks when todo search folder is removed
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Thu Nov 16 2017 bosim@opensuse.org
- Updated to 3.4.0 final, improvements:
  * Flag handling
  * To-do list
  * Improved categories
  * Search folders
  * Performance improvements
  * Smaller improvements and bugfixes
- Full changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
* Tue Jul 18 2017 bosim@opensuse.org
- Updated to 3.3.1 final, changelog:
  * Bugs:
  * KW-924 - Improve webapp presence cache by making it hash-based
  * KW-1162 - No ‘save’ notification when applying settings while
    having a mail pop-out window open
  * KW-1170 - Php error when adding recurrence to existing calendar
    item
  * KW-1198 - Empty body in webapp when parser breaks on minified
    javascript
  * KW-1216 - Business card filter can not be applied again when
    switching back and forth between contact folders
  * KW-1246 - Mail scroll bar resets when switching tabs
  * KW-1291 - Php 7.1 fatal error when opening signed or encrypted
    email
  * KW-1303 - Suggested contacts folder of shared store not closed
    even if the entire store is closed
  * KW-1407 - Rtl direction attribute is removed from html mail
  * KW-1419 - Original html message removed entirely when pressing
    enter
  * KW-1443 - Layout of task request breaks
  * KW-1469 - [sles12] invalid dirname and filename for italian
    spellchecker language pack
  * Improvement:
  * KW-1241 - “what’s new” dialog in webapp
  * KW-1319 - Put the unit behind the value for the reload interval
    when configuring a widget
  * KW-1342 - Combo list should be the same styling as sub menu
  * KW-1399 - Improve task request message code so one sentence
    does not appear as two separate strings for translators
  * KW-1456 - [intranet plugin] disable the plugin by default
  * KW-1459 - Php 7.1 throws error when adding a non-numeric value
    to a string
* Tue Jul 18 2017 bosim@opensuse.org
- %%prep will modify "version" file so webapp will show actual
  version instead of "devel".
* Tue May 30 2017 bosim@opensuse.org
- Updated to 3.3 final, changelog:
  https://documentation.kopano.io/kopano_changelog/webapp.html
  [#]kopano-webapp-3-3-0-final
- Ran spec-cleaner
* Thu Jan 26 2017 bosim@opensuse.org
- Updated to 3.2 snapshot 149
* Mon Jul 18 2016 bosim@opensuse.org
- Created package based on zarafa-webapp. Used 3.0.1 sources from
  bitbucket
- Added patch to support apache 2.4 config directives
