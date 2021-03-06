#
# spec file for package kopano-webapp
#
# Copyright (c) 2019 Mark Verlinde
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define langdir %{_datadir}/%{name}/server/language
%define plugindir %{_datadir}/%{name}/plugins

Name:           kopano-webapp
Version:        4.6.2
Release:        1%{?dist}
Summary:        Improved WebApp for Kopano
License:        AGPL-3.0-only
Url:            https://kopano.io
Source:         https://github.com/Kopano-dev/kopano-webapp/archive/v%{version}.tar.gz

# Configure apache to use rh-php7x fpm by default
Patch1:         rh-php7x-php-fpm-httpd-conf.patch

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ant
BuildRequires:  xz
BuildRequires:  libxml2
BuildRequires:  gettext
BuildRequires:  rh-php73

Requires:       %{name}-lang = %{version}

Requires:       php73-mapi
Requires:       rh-php73
Requires:       rh-php73-php-fpm

# On el7 (centos) these 3 are provided by (rh-php7x-)php-common; a dependency of (rh-php7x-)php
#Requires:       rh-php73-php-gettext
#Requires:       rh-php73-php-openssl
#Requires:       rh-php73-php-zlib

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
%autosetup -p1
find . -type f "(" -name "*.js" -o -name "*.php" ")" \
  -exec chmod a-x "{}" "+";
echo "%{version}" > version

%build
source /opt/rh/rh-php73/enable
%{make_build}

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

%changelog
* Sun Dec 27 2020 mark Verlinde <mark.verlinde@gmail.com> 4.6.3-1
- rh-php73-php-fpm is a default requirment now
- Update to 4.6.3

* Tue Oct 01 2019 mark Verlinde <mark.verlinde@gmail.com>
- rh-php72-php-fpm is a default requirment now
- Update to 3.5.10
  - Bug   
  * KW-3016 Arrow keys does not work as expected with Firefox on Ubuntu
  * KW-3110 Default folder is not selected in rules select folder dialog
  * KW-3111 After adding a flag plain text is visible in search preview
  * KW-3196 Umlauts missing for certain emails when reply/forward in plain text editor
  * KW-3100 Webapp with oidc runs in quirks mode
  * KW-3184 Remove dependency on php-gettext
  * KW-3189 Category button is not shown while hovering row
  * KW-3154 Sort by flag does not function
  * KW-189  Subject column takes too much width in task list print
  * KW-2907 [json themes] action colors are not updated
  * KW-3129 German umlauts disappear until webserver is restarted
  * KW-3096 Item without a pr_record_key has an “untitled” attachment name
  * KW-346  Remove icons from “show details” dialog in scheduling
  * KW-515  Shared inbox folder jumps position in favorites when marking mail read/unread
  * KW-2228 Shared contact folder is not translated to german
  * KW-3105 Add font-size to .x-fieldset for files account creation
  - Improvement   
  * KW-313  Ability to select other users mailbox when settings Out of Office
  * KW-3041 Copy all email addresses from to/cc/bcc field
  * KW-731  Concatenate extjs stylesheets
  * KW-2311 Change fallback timezone to europe/amsterdam
  * KW-3039 Add option to always cc specific address
  * KW-254  Create a rule for items with an at least or at most size
  * KW-1405 Refactor calendar canvas implementation
  * KW-2822 Support for rules exceptions
  * KW-3173 Avoid to show “show all folders” panel in navigation panel forcefully
  * KW-840  Create rule for “name in bcc box”
  * KW-2507 Update link to powerpaste configuration
  * KW-2818 Calendar: add day of week next to date
  * KW-3122 Allow plugins can set the notifiers
  * KW-3123 Use custom shadow store to record component plugin
  * KW-3147 Create print overview for calendar grid (list view)
  * KW-3148 Allow plugins to add ipf notification module name
  * KW-3157 Add colored border to indicate unread items
  * KW-571  Add “create folder” option in rules’ select folder dialogue
  * KW-1265 Create a rule-action for “mark mail as read”
  * KW-2836 Add support for rule: “includes these words in the recipient address”
  * KW-2982 Redesign x-window dialogs
  * KW-2025 Add ‘remove from to-do list’ button to context menu
  * KW-2388 Add padding above buttons in rule creation dialog
  * KW-2422 Don’t show the “update rules for” feature when the list contains one user
  * KW-2877 Add oidc support to webapp
  * KW-2941 Send icon missing in send later dialog
  * KW-3081 Context menu handler changes in zarafa.js
  * KW-3083 Create insertion point in rules settings
  * KW-3085 Unpin favorites from top in “create new folder” dialog

* Sat Apr 13 2019 bosim@opensuse.org
- Update to 3.5.4
  * KW-18 Download all as zip skips files with same name
  * KW-1756 Sent field displays the received date
  * KW-2770 [mail widget] to input field too small
  * KW-3057 Create appointment from email on nearest ‘start of
    block’
  * KW-3062 Deskapp: downloads from intranet plugin do not work
  * KW-3064 [safari] attachments with umlaut can’t be uploaded
  * KW-3078 Uncaught arithmeticerror: bit shift by negative number
  * KW-769 Increase message options dialogue size
  * KW-1160 Improve text in delegate settings tab
  * KW-3008 Show entryids in message options
  * KW-3055 Exclude outbox folders from pre-fetching
  * KW-1332 Multiple appointments in the same time slot will not
    use the entire width of the row
  * KW-2670 [json themes] not all main colors get correct hover
    color
  * KW-2922 Webapp wrongly tries sso login when request containts
    empty remote_user
  * KW-3003 [json themes] extra-info text color is always adjusted
  * KW-3007 Default language set by admin not shown on login page
  * KW-3015 Download buttons do not work in mattermost plugin
  * KW-619 Pop-out window uses uncompressed tinymce scripts
  * KW-733 Kopano stylesheet should be minimized
  * KW-787 After login load body of first x items
  * KW-1543 Use english for message headers on replies and forwards
    while language is set to non-english
  * KW-2841 Additional_categories should always extend current
    categories
  * KW-2951 Don’t search for hidden attachments
  * KW-2979 Modify font-size css selector for quill
  * KW-2986 Update set default signature script
  * KW-3004 Shorter the “message saved at” text
  * KW-3005 Update email spelling of new mail tab
  * KW-3006 Mailflagscontentpanel and mailflagspanel not used
  * KW-3022 Update closure-compiler
  * KW-3025 Quill editor specific change in webapp
  * KW-1610 Hiting del-key very fast ends up in error
  * KW-2365 Menu of preview pane wont open after searching
  * KW-2781 Wa leaves an unnamed rule action after actions are deleted
  * KW-2782 [quick task widget] due date via widget is one day earlier
  * KW-2918 Icon missing for recurring meeting request mail
  * KW-2959 [kql] tokenizr.min.js not found
  * KW-2966 Time values in scheduling tab doesn’t overwrite time in appointment
    tab for recurruring items
  * KW-2973 Recurring information does not fit in calendar tooltip
  * KW-2975 Dots shown in column icons
  * KW-2977 Calendar: icon of time indicator line is missing (not visible)
  * KW-442 Implement printing of calendar month overview
  * KW-2680 Add info pop-up when moving a meeting as attendee
  * KW-2917 Resolve php 7.3 warnings
  * KW-2944 [kql] implement character operators
  * KW-2948 [kql] the license of the tokenizr library should be added to
    the webapp
  * KW-2949 [kql] update tokenizr library
  * KW-2950 [kql] improve build with regard to tokenizr library
  * KW-2958 Include time in monthly printing overview
  * KW-2952 [kql] parenthesis around the complete query are seen as free
    text search
  * KW-2953 [!chrome] search tab broken
  * KW-2054 Addition line in plugin config.php prevents webapp from loading
  * KW-2470 Update list bar of tasks doesn’t end
  * KW-2640 Support ”.-” in local part of a mail address
  * KW-2868 Filter icon missing; unread icon incorrect
  * KW-2905 Json themes: small logo is not displayed
  * KW-2913 Php 7.3 issue: jsonexception already defined
  * KW-2920 What’s new dialog double encodes strings
  * KW-2927 Reminderlistmodule requests stops when kc-server restarts
  * KW-2931 Inline image breaks when mail is forwarded or replied to
  * KW-1685 Order calendars alphabetically in calendar hierarchy
  * KW-2330 Improve extra info box
  * KW-2562 Consistently use email spelling
  * KW-2890 Create calendar event from an email
  * KW-2896 Copy email address in scheduling tab
  * KW-2899 Reduce php memory usage when loading the gab
  * KW-2906 Implement kql for search
  * KW-2908 Remove not current button
  * KW-2915 Themes should be able to change the colors of icons
  * KW-2928 Disable “what’s new’ with central configuration option
  * KW-2929 Populate insertion points in general widget
  * KW-2900 Escaped html shown in print preview
  * KW-2902 Print preview is empty
  * KW-2904 Updated meeting requests do not have an icon
  * KW-2909 Improve print code
  * KW-805 Increase height of edit sender, edit recipient dialog
  * KW-1155 Edge - tool tips unnecessarily use an extra line
  * KW-1320 Month picker in suggested times not visible
  * KW-2411 Block middle-click in folder hierarchy
  * KW-2730 [minimal tinymce] font size wrong when inserting browser
    spell checker suggestion
  * KW-2757 Html signatures are not prepended with an empty line in
    pop-outs
  * KW-2758 Html signatures are prepended with one empty line
  * KW-2769 Inline images not loaded for printout
  * KW-2787 Deleted inline images is sent as unknown_content_type.jpg
  * KW-2819 Day view printing dates should be translatable strings
  * KW-2855 “php notice: use of undefined constant loglevel_off” when
    deploying webapp
  * KW-2857 Title counter: open about link in new window
  * KW-2865 Regression: widget collapse/expand icon does not change
  * KW-169 Allow a user to disable their favorites
  * KW-617 Export calendar items as ics
  * KW-1008 Only show scrollbar while hovering element
  * KW-2245 Favorites folders should always be visible
  * KW-2487 Pluggable icon packs
  * KW-2493 What’s new: icon pack
  * KW-2666 Import ics / vcs from upload
  * KW-2743 Add option to delete items directly to soft delete for
    shared folders
  * KW-2813 Include location in print overview
  * KW-2843 [task widget] hide email followups when marked as done
  * KW-2850 Make the new icon pack default
  * KW-2853 Remove panel collapse / expand animation
  * KW-2860 [minimal tinymce] empty lines are removed when viewing
    from outlook
  * KW-2875 Npm files should be ignored or added to the repository
  * KW-2882 Update package.json dependencies to non-vulnerable one
  * KW-2887 Remove bracket from mail counter
* Sat Apr 13 2019 bosim@opensuse.org
- Update to 3.4.24
  * KW-2017 [desktop notification plugin] disable autohide does not
    work
  * KW-2581 Images not shown in body
  * KW-2676 Log message string when user is deleted is split over
    multiple lines
  * KW-2768 Missing tooltips for widget buttons
  * KW-2797 Removed users meeting request opening throws javascript
    errors
  * KW-2815 [desktop notifications plugin] reminder does not appear
    as desktop notification
  * KW-2835 Print within the main webapp window
  * KW-2849 [folder widgets] height not re-applied
  * KW-1311 [desktop notifications plugin] don’t mention ‘chrome and
    firefox’
  * KW-2162 Insufficient privileges message popups while moving
    appointment in public calendar
  * KW-2278 Link to a file on a network share would be rewritten
  * KW-2657 Direct booking method broken
  * KW-2694 [appointment widget] items cannot be unselected
  * KW-2697 While attachment is being uploaded saving is possible
  * KW-2760 Wa fails to handle flatentrylist structure for multi
    reply-to
  * KW-2798 Ambiguous recipient when receiving meeting request
  * KW-2799 Mapi_e_unknown_entryid when importing an malformed
    pr_reply_recipient_entries
  * KW-2801 Configure widget dialog should be slightly bigger
  * KW-2806 Error shows in debug.txt when add resource in recurring
    exception
  * KW-2826 Text color in category blocks in the calendar tooltip
    is always white
  * KW-613 Import calendar items (ics & vcs) from attachment
  * KW-1718 Let webapp show client & server versions
  * KW-2013 Delete all items from folder
  * KW-2525 Replace the current widget plugin with the advanced
    widget plugin
  * KW-2535 Advanced task/appointments widget: show categories as we
    do it now
  * KW-2537 [appointment widget] do not show appointments in the past
  * KW-2735 Move html editor plugin to webapp core
  * KW-2802 Rename task widget to task / todo
  * KW-2804 Make booking resources not look like an error
  * KW-648 Out of office dependent rules
  * KW-2793 Revert: kw-2214
  * KW-1841 Date from signed and encrypted mails are not shown in
    search results
  * KW-2189 Calendar title not cut off properly in create in
    drop-down menu
  * KW-2547 Ampersand html code visible full name
  * KW-2579 Address book dysfunctional after removing shared folder
    permission
  * KW-2761 Webapp tries to access a subfolder inside a restricted
    parent folder
  * KW-361 Get notifications about new mail in other users’
    inboxes *
  * KW-1470 Configuration window of a widget should be modal
  * KW-2193 Use kopanoenabledfeatures to enable/disable
    webapp/deskapp
  * KW-2339 Per-user logging in webapp
  * KW-2658 Support to open eml files with deskapp
  * KW-2752 Reduce code duplication in quickitems
  * KW-2771 Change widget labels to place holder text
  * KW-2784 Increase size of “add widget” dialog
  * KW-2785 Change widget panel name from “kopano” to “widgets”
  * KW-315 Webapp rpm lacks a dependency on mbstring
  * KW-2443 Inline image declared as content-type: image/plain
  * KW-2701 Reminder dialog and in-browser notification appear in
    pop-out window
  * KW-2741 Unable to copy calendar / meeting with shortcuts
  * KW-2742 Space missing in copied appointment text
  * KW-2745 Unable to login when quick appointment widget is enabled
  * KW-1373 Hierarchy list request is slow
  * KW-1989 Add group criteria sender to the mail grid
  * KW-2031 Improve text in ‘accepting task’ dialog
  * KW-2550 Improve tool tips text
  * KW-2647 Improve performance of loading the hiearchy with
    shared stores
  * KW-2027 Print dialog does not open
  * KW-2214 ‘send as attachment’ should not add forward indicator
    to the message (fw:)
  * KW-2460 Appointment saved into the wrong calendar with read
    only permissions
  * KW-2628 Strip sgml comments in style attribute
  * KW-2700 Today’s appointment widget shows escaped html
  * KW-2715 Escaped html shown when no signatures are configured
  * KW-185 Filter to show unread e-mails only
  * KW-1191 Show email address when printing an email
  * KW-1675 Hide the number of unread e-mails as part of the search
    folder favorite name
  * KW-2650 Remove not required hashing from reminderlistmodule
  * KW-2674 [json themes] support x-menu-item-selected
  * KW-2709 Update default columns of the contact folder
  * KW-2712 Ooo text input field should be larger
  * KW-1958 Country code jumps to the wrong field
  * KW-2528 Basic shortcuts are not enabled by default when
    kopano-files is not installed
  * KW-2705 Broken members of distributionlist break the whole list
  * KW-1728 Xss injection via description and image urls in what’s
    new dialog
  * KW-2237 Removing attachment and send meeting request still have
    the attachment
  * KW-2575 Canceled attachments are still uploaded
  * KW-2685 Xss via components names
  * KW-2688 Deleting a gab user which is part of a distribution
    list breaks the list
  * KW-2689 Accepting meeting request in shared store throws error
  * KW-1969 Add to favorites dialog remove ‘folder name’
  * KW-2267 Refactor reminder dialog iconclass code
  * KW-2604 Build webapp for ucs 4.3
  * KW-2612 Ucs 4.3 spellchecker plugin support
  * KW-2613 Ucs 4.3 support for plugin mattermost
  * KW-2614 Ucs 4.3 support for desktop notification plugin
  * KW-1277 Task request data not visible when previewing in small
    window
  * KW-1890 German spellchecker marks some common abbreviation as
    incorrect
  * KW-2384 Deleting a kopano-contact removes mailaddress in
    existing mails
  * KW-2509 Unable to download attachment from popout and preview
    pane
  * KW-2539 Large folder structures get scrambled after copying a
    folder
  * KW-2632 Opening task / todo folder in embedded window throws
    error
  * KW-2661 Undefined offset errors when opening a task request
  * KW-1127 Notes: remove unused functions
  * KW-2127 Add category as an optional filter in search tools
  * KW-2212 Open reminder dialog from reminder button in menu bar
  * KW-2564 Add support for simple json themes
  * KW-2606 Use mapi_deferred_errors flag when opening a table
  * KW-2654 Refactor common code
  * KW-428 Clicking outside of the copy/move dialog selects a
    folder
  * KW-872 Error occurs when editing local contact via address book
  * KW-1194 “add new...” e-mail address dialog has too much height
    by default
  * KW-1362 Webapp should handle ‘broken’ freebusy entryid
  * KW-2317 Mail sent as attachment can’t be imported
  * KW-2360 Html ampersand code visible in link
  * KW-2383 Organizer should be updated when selected
    “create in calendar” is changed
  * KW-2436 Losing category when receiving update for meeting
    request
  * KW-2452 Send as email when selecting contact, distribution list
    and email freezes the to send email
  * KW-2526 Unable to delete assigned tasks from public folder
  * KW-2546 Infinite scroll loading information is not reset when
    switching folders
  * KW-2584 Unable to delete search folder when it contains
    messages
  * KW-2625 Unable to upload certificates
  * KW-2626 Hover card is missing send new mail icon
  * KW-2651 Invalid html in notifier message
  * KW-463 Reloading pop-out should not clear unsaved content
  * KW-2322 Reposition pagination panel of the mail grid
  * KW-2335 Introduce possibility to show more information about
    ‘message could not be saved’
  * KW-2556 Improve loading of recurrences
  * KW-2588 Add delay to hover card pop-up
  * KW-2598 Implement dark tooltips
  * KW-2363 Classlist.foreach does not work in ie/edge
  * KW-2446 Categorie management can not opened in ie11
  * KW-2497 Send mail to distribution list broken in ie
  * KW-2498 Right click on a contact and “send mail” do not work
    with ie11
  * KW-2520 Fpm support presently broken
  * KW-1076 When session already exists allow user to destroy
    existing sessions
  * KW-2018 Create a “share folder” button in folder context menu
  * KW-2090 Open item in new tab when opened from the reminders
    dialog
  * KW-2114 Change whatsapp favicon in the tab to official whatsapp
    favicon
  * KW-2326 Import eml via upload
  * KW-2385 Implement hoover card: show name, emailadres and
    warning info
  * KW-2458 Hightlight active filter in contact business card view
  * KW-2461 Allow disabling publishing of free/busy information
  * KW-354 Delete button shows tool tip as string in overflow menu
  * KW-1869 Missing space in ‘from’ auto generated reply quote text
    header
  * KW-2243 Removed inline images are sent as bin attachments
  * KW-2495 Attachment broken when opened from a mail which should
    be forwarded
  * KW-2587 Disable cancellation of uploaded attachments
  * KW-620 Remove version info from login page
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
