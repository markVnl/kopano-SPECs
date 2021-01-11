%define with_rh_php73 1

Name:       z-push
Version:    2.6.1
Release:    1
Summary:    An implementation of Microsoft's ActiveSync protocol
Group:      Applications/Productivity
License:    AGPL-3.0
BuildArch:  noarch
URL:        http://z-push.org/
Source:     https://github.com/Z-Hub/Z-Push/archive/%{version}.tar.gz
Source1:    z-push-rh-php7x-php-fpm.conf
Source2:    autodiscover-rh-php7x-php-fpm.conf
BuildRoot:  %_tmppath/%name-%{version}-build



%description
Z-push is an implementation of the ActiveSync protocol which is used 'over-the-air' for multi platform ActiveSync devices. Devices supported are including Windows Mobile, Android, iPhone, and Nokia. With Z-push any groupware can be connected and synced with these devices.

%package -n %name-common
Summary:    Z-Push core package
Group:      Applications/Productivity

%if %with_rh_php73
Requires:   rh-php73
Requires:   rh-php73-php-soap
Requires:   rh-php73-php-mbstring
Requires:   rh-php73-php-process
%else
Requires:   php >= 5.4.0
Requires:   php-soap
Requires:   php-mbstring
Requires:   php-process
%endif
Requires(pre):  %_sbindir/groupadd

%description -n %name-common
Z-push is an implementation of the ActiveSync protocol which is used 'over-the-air' for multi platform ActiveSync devices. Devices supported are including Windows Mobile, Android, iPhone, and Nokia. With Z-push any groupware can be connected and synced with these devices.

# CALDAV
%package -n %name-backend-caldav
Summary:    Z-Push caldav backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
Requires:   php-awl
%if %with_rh_php73
Requires:   rh-php73-php-common
Requires:   rh-php73-php-xml
%else
Requires:   php-xml
%endif
Provides:   %name-backend = %{version}

%description -n %name-backend-caldav
Backend for Z-Push, that adds the ability to connect to a caldav server

# CARDDAV
%package -n %name-backend-carddav
Summary:    Z-Push carddav backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
Requires:   php-xsl
Provides:   %name-backend = %{version}

%description -n %name-backend-carddav
Backend for Z-Push, that adds the ability to connect to a carddav server

# COMBINED
%package -n %name-backend-combined
Summary:    Z-Push combined backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
Provides:   %name-backend = %{version}

%description -n %name-backend-combined
Backend for Z-Push, that adds the ability to combine backends.

# IMAP
%package -n %name-backend-imap
Summary:    Z-Push imap backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
Requires:   php-awl
%if %with_rh_php73
Requires:   rh-php73-php-imap
%else
Requires:   php-imap
%endif
Provides:   %name-backend = %{version}

%description -n %name-backend-imap
Backend for Z-Push, that adds the ability to connect to a imap server

# LDAP
%package -n %name-backend-ldap
Summary:    Z-Push ldap backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-ldap
%else
Requires:   php-ldap
%endif
Provides:   %name-backend = %{version}

%description -n %name-backend-ldap
Backend for Z-Push, that adds the ability to connect to a ldap server

# KOPANO
%package -n %name-backend-kopano
Summary:    Z-Push Kopano backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   php73-mapi
%else
Requires:   php-mapi
%endif
Provides:   %name-backend = %{version}

%description -n %name-backend-kopano
Backend for Z-Push, that adds the ability to connect to a Kopano server

%package -n %name-kopano
Summary:    Z-Push for Kopano
Group:      Applications/Productivity
Requires:   %name-common = %{version}
Requires:   %name-backend-kopano = %{version}
Requires:   %name-ipc-sharedmemory = %{version}

%description -n %name-kopano
Z-Push for Kopano meta package

%package -n %name-kopano-gabsync
Summary:    GAB sync for Kopano
Group:      Applications/Productivity
%if %with_rh_php73
Requires:   php73-mapi
%else
Requires:   php-mapi
%endif

%description -n %name-kopano-gabsync
Synchronizes a Kopano global address book

%package -n %name-kopano-gab2contacts
Summary:    GAB sync into a contacts folder for Kopano
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   php73-mapi
%else
Requires:   php-mapi
%endif

%description -n %name-kopano-gab2contacts
Synchronizes a Kopano global address book into a contacts folder

# IPC SHARED MEMORY
%package -n %name-ipc-sharedmemory
Summary:    Z-Push ipc shared memory provider
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-process
%else
Requires:   php-sysvshm
Requires:   php-sysvsem
Requires:   php-pcntl
%endif

%description -n %name-ipc-sharedmemory
Provider for Z-Push, that adds the ability to use ipc shared memory

# IPC MEMCACHED
%package -n %name-ipc-memcached
Summary:    Z-Push ipc memcached provider
Group:      Applications/Productivity
Requires:   %name-common = %{version}
Requires:   memcached
%if %with_rh_php73
Requires:   sclo-php73-php-pecl-memcached
%else
Requires:   php-pecl-memcached
%endif

%description -n %name-ipc-memcached
Provider for Z-Push, that adds the ability to use ipc memcached

# GALSEARCH LDAP
%package -n %name-galsearch-ldap
Summary:    Z-Push ldap search backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-ldap
%else
Requires:   php-ldap
%endif
Provides:   %name-backend = %{version}

%description -n %name-galsearch-ldap
Backend for Z-Push, that adds the ability to search a ldap server

# STATE SQL
%package -n %name-state-sql
Summary:    Z-Push mysql state backend
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-mysqlnd
Requires:   rh-php73-php-pdo
%else
Requires:   php-mysql
Requires:   php-pdo
%endif

%description -n %name-state-sql
Backend for Z-Push, that adds the ability to save states in a mysql database

# AUTODISCOVER
# check for rh-php73
%package -n %name-autodiscover
Summary:    Z-Push autodiscover
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-xml
%else
Requires:   php-xml
%endif
Requires:   %name-backend

%description -n %name-autodiscover
Autodiscover for Z-Push backends

# CONFIG
%package -n %name-config-apache
Summary:    Z-Push apache configuration
Group:      Applications/Productivity
Requires:   %name-common = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-fpm
%endif
Requires:   httpd



%description -n %name-config-apache
Z-push apache configuration files

%package -n %name-config-apache-autodiscover
Summary:    Z-Push autodiscover apache configuration
Group:      Applications/Productivity
Requires:   %name-autodiscover = %{version}
%if %with_rh_php73
Requires:   rh-php73-php-fpm
%endif
Requires:   httpd


%description -n %name-config-apache-autodiscover
Z-push autodiscover apache configuration files

# CONFIG NGINX
%package -n %name-config-nginx
Summary:    Z-Push nginx configuration
Group:      Applications/Productivity
Requires:   nginx

%description -n %name-config-nginx
Z-push nginx configuration files

%prep
%setup -q -n Z-Push-%{version}

%build

%install

mkdir -p %{buildroot}%{_datadir}/z-push
cp -a src/* %{buildroot}/%{_datadir}/z-push/
rm -f %{buildroot}/%{_datadir}/z-push/{INSTALL,LICENSE}

# COMMON
# set version number
sed -s "s/ZPUSHVERSION/%{version}/" build/version.php.in > %{buildroot}%{_datadir}/z-push/version.php

mkdir -p %{buildroot}%_sysconfdir/z-push

mv %{buildroot}%{_datadir}/z-push/config.php %{buildroot}%{_sysconfdir}/z-push/z-push.conf.php
ln -s %{_sysconfdir}/z-push/z-push.conf.php %{buildroot}%{_datadir}/z-push/config.php

mv %{buildroot}%{_datadir}/z-push/policies.ini %{buildroot}%{_sysconfdir}/z-push/policies.ini
ln -s %{_sysconfdir}/z-push/policies.ini %{buildroot}%{_datadir}/z-push/policies.ini

mkdir -p %{buildroot}%_bindir
ln -s %{_datadir}/z-push/z-push-admin.php %{buildroot}%_bindir/z-push-admin
ln -s %{_datadir}/z-push/z-push-top.php %{buildroot}%_bindir/z-push-top

mkdir -p %{buildroot}%_localstatedir/lib/z-push
mkdir -p %{buildroot}%_localstatedir/log/z-push
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -Dpm 644 config/z-push-rhel.lr \
    %{buildroot}%{_sysconfdir}/logrotate.d/z-push.lr

# CALDAV
mv %{buildroot}%{_datadir}/z-push/backend/caldav/config.php %{buildroot}%{_sysconfdir}/z-push/caldav.conf.php
ln -s %{_sysconfdir}/z-push/caldav.conf.php %{buildroot}%{_datadir}/z-push/backend/caldav/config.php

# CARDDAV
mv %{buildroot}%{_datadir}/z-push/backend/carddav/config.php %{buildroot}%{_sysconfdir}/z-push/carddav.conf.php
ln -s %{_sysconfdir}/z-push/carddav.conf.php %{buildroot}%{_datadir}/z-push/backend/carddav/config.php

# COMBINED
mv %{buildroot}%{_datadir}/z-push/backend/combined/config.php %{buildroot}%{_sysconfdir}/z-push/combined.conf.php
ln -s %{_sysconfdir}/z-push/combined.conf.php %{buildroot}%{_datadir}/z-push/backend/combined/config.php

# IMAP
mv %{buildroot}%{_datadir}/z-push/backend/imap/config.php %{buildroot}%{_sysconfdir}/z-push/imap.conf.php
ln -s %{_sysconfdir}/z-push/imap.conf.php %{buildroot}%{_datadir}/z-push/backend/imap/config.php

# LDAP
mv %{buildroot}%{_datadir}/z-push/backend/ldap/config.php %{buildroot}%{_sysconfdir}/z-push/ldap.conf.php
ln -s %{_sysconfdir}/z-push/ldap.conf.php %{buildroot}%{_datadir}/z-push/backend/ldap/config.php

# KOPANO
mv %{buildroot}%{_datadir}/z-push/backend/kopano/config.php %{buildroot}%{_sysconfdir}/z-push/kopano.conf.php
ln -s %{_sysconfdir}/z-push/kopano.conf.php %{buildroot}%{_datadir}/z-push/backend/kopano/config.php

# GAB-SYNC
mkdir -p %{buildroot}%{_datadir}/z-push/tools
cp -a tools/gab-sync %{buildroot}%{_datadir}/z-push/tools/
mv %{buildroot}%{_datadir}/z-push/tools/gab-sync/config.php %{buildroot}%{_sysconfdir}/z-push/gabsync.conf.php
ln -s %{_sysconfdir}/z-push/gabsync.conf.php %{buildroot}%{_datadir}/z-push/tools/gab-sync/config.php
mkdir -p %{buildroot}%_bindir
ln -s %{_datadir}/z-push/tools/gab-sync/gab-sync.php %{buildroot}%_bindir/z-push-gabsync

# GAB2CONTACTS
mkdir -p %{buildroot}%{_datadir}/z-push/tools
cp -a tools/gab2contacts %{buildroot}%{_datadir}/z-push/tools/
mv %{buildroot}%{_datadir}/z-push/tools/gab2contacts/config.php %{buildroot}%{_sysconfdir}/z-push/gab2contacts.conf.php
ln -s %{_sysconfdir}/z-push/gab2contacts.conf.php %{buildroot}%{_datadir}/z-push/tools/gab2contacts/config.php
sed -i -s "s/PATH_TO_ZPUSH', '\.\.\/\.\.\/src\/')/PATH_TO_ZPUSH', '\/usr\/share\/z-push\/')/" %{buildroot}%{_datadir}/z-push/tools/gab2contacts/gab2contacts.php
mkdir -p %{buildroot}%_bindir
ln -s %{_datadir}/z-push/tools/gab2contacts/gab2contacts.php %{buildroot}%_bindir/z-push-gab2contacts

# MEMCACHED
mv %{buildroot}%{_datadir}/z-push/backend/ipcmemcached/config.php %{buildroot}%{_sysconfdir}/z-push/memcached.conf.php
ln -s %{_sysconfdir}/z-push/memcached.conf.php %{buildroot}%{_datadir}/z-push/backend/ipcmemcached/config.php

# GALSEARCH LDAP
mv %{buildroot}%{_datadir}/z-push/backend/searchldap/config.php %{buildroot}%{_sysconfdir}/z-push/galsearch-ldap.conf.php
ln -s %{_sysconfdir}/z-push/galsearch-ldap.conf.php %{buildroot}%{_datadir}/z-push/backend/searchldap/config.php

# STATE SQL
mv %{buildroot}%{_datadir}/z-push/backend/sqlstatemachine/config.php %{buildroot}%{_sysconfdir}/z-push/state-sql.conf.php
ln -s %{_sysconfdir}/z-push/state-sql.conf.php %{buildroot}%{_datadir}/z-push/backend/sqlstatemachine/config.php

cp -a tools/migrate-filestates-to-db.php %{buildroot}%{_datadir}/z-push/tools/

# AUTODISCOVER
mv %{buildroot}%{_datadir}/z-push/autodiscover/config.php %{buildroot}%{_sysconfdir}/z-push/autodiscover.conf.php
ln -s %{_sysconfdir}/z-push/autodiscover.conf.php %{buildroot}%{_datadir}/z-push/autodiscover/config.php

# APACHE
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
%if %with_rh_php73
install -m 0664 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/z-push.conf
install -m 0664 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/z-push-autodiscover.conf
%else
install -Dpm 644 config/apache2/z-push.conf \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/z-push.conf
install -Dpm 644 config/apache2/z-push-autodiscover.conf \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/z-push-autodiscover.conf
%endif

# NGINX
# not packaged
# mkdir -p %{buildroot}%{_sysconfdir}/nginx/sites-available/
# install -Dpm 644 config/nginx/z-push.conf %{buildroot}%{_sysconfdir}/nginx/sites-available/z-push.conf

# MANPAGES
mkdir -p %{buildroot}%_mandir/man1
cp man/*.8 %{buildroot}%_mandir/man1


%post -n %name-config-apache
service httpd reload || true


%post -n %name-config-apache-autodiscover
service httpd reload || true

# NGNIX is not packaged
#%post -n %name-config-nginx
#echo -e "\033[0;33mEdit %{_sysconfdir}/nginx/sites-available/z-push.conf, enable it and reload nginx.\n\033[0m"

%post -n %name-ipc-memcached
# check
%if %with_rh_php73
echo -e "\033[0;33mMake sure you have scl repositories enabled.\n\033[0m"
%endif

%postun -n %name-config-apache
service httpd reload || true


%postun -n %name-config-apache-autodiscover
service httpd reload || true


%postun -n %name-config-nginx
service nginx reload || true

# COMMON
%files -n %name-common
%doc src/LICENSE
%defattr(-, root, root)
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/policies.ini
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/z-push.conf.php
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/logrotate.d/z-push.lr
%exclude %_datadir/z-push/backend
%exclude %_datadir/z-push/autodiscover
%exclude %_datadir/z-push/tools/migrate-filestates-to-db.php
%exclude %_datadir/z-push/tools/gab-sync
%exclude %_datadir/z-push/tools/gab2contacts
%_datadir/z-push/
%attr(770,root,apache) %dir %_localstatedir/lib/z-push
%attr(770,root,apache) %dir %_localstatedir/log/z-push
%_bindir/z-push-admin
%_bindir/z-push-top
%_mandir/man1/z-push-admin.8*
%_mandir/man1/z-push-top.8*

# CALDAV
%files -n %name-backend-caldav
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/caldav
%_datadir/z-push/backend/caldav/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/caldav.conf.php

# CARDDAV
%files -n %name-backend-carddav
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/carddav
%_datadir/z-push/backend/carddav/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/carddav.conf.php

# COMBINED
%files -n %name-backend-combined
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/combined
%_datadir/z-push/backend/combined/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/combined.conf.php

# IMAP
%files -n %name-backend-imap
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/imap
%_datadir/z-push/backend/imap/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/imap.conf.php

# LDAP
%files -n %name-backend-ldap
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/ldap
%_datadir/z-push/backend/ldap/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/ldap.conf.php

# KOPANO
%files -n %name-backend-kopano
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/kopano
%_datadir/z-push/backend/kopano/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/kopano.conf.php

%files -n %name-kopano-gabsync
%defattr(-, root, root)
%dir %_datadir/z-push/tools
%dir %_datadir/z-push/tools/gab-sync
%_datadir/z-push/tools/gab-sync/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/gabsync.conf.php
%_bindir/z-push-gabsync
%_mandir/man1/z-push-gabsync.8*

%files -n %name-kopano-gab2contacts
%defattr(-, root, root)
%dir %_datadir/z-push/tools
%dir %_datadir/z-push/tools/gab2contacts
%_datadir/z-push/tools/gab2contacts/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/gab2contacts.conf.php
%_bindir/z-push-gab2contacts
%_mandir/man1/z-push-gab2contacts.8*

%files -n %name-kopano

# IPC-SHAREDMEMORY
%files -n %name-ipc-sharedmemory
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/ipcsharedmemory/
%_datadir/z-push/backend/ipcsharedmemory

# IPC-MEMCACHED
%files -n %name-ipc-memcached
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/ipcmemcached
%_datadir/z-push/backend/ipcmemcached/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/memcached.conf.php

# GALSEARCH-LDAP
%files -n %name-galsearch-ldap
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/searchldap
%_datadir/z-push/backend/searchldap/
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/galsearch-ldap.conf.php

# STATE-SQL
%files -n %name-state-sql
%defattr(-, root, root)
%dir %_datadir/z-push/backend
%dir %_datadir/z-push/backend/sqlstatemachine
%_datadir/z-push/backend/sqlstatemachine/
%_datadir/z-push/tools/migrate-filestates-to-db.php
%dir %_sysconfdir/z-push
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/state-sql.conf.php

# AUTODISCOVER
%files -n %name-autodiscover
%defattr(-, root, root)
%dir %_datadir/z-push/autodiscover
%_datadir/z-push/autodiscover/
%dir %_sysconfdir/z-push
    %config(noreplace) %attr(0640,root,apache) %_sysconfdir/z-push/autodiscover.conf.php

# CONFIG
%files -n %name-config-apache
%dir %_sysconfdir/httpd
%dir %_sysconfdir/httpd/conf.d
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/httpd/conf.d/z-push.conf

%files -n %name-config-apache-autodiscover
%dir %_sysconfdir/httpd
%dir %_sysconfdir/httpd/conf.d
%config(noreplace) %attr(0640,root,apache) %_sysconfdir/httpd/conf.d/z-push-autodiscover.conf

# NGINX CONFIG
# not packaged
#%%files -n %name-config-nginx
#%%dir %_sysconfdir/nginx
#%%dir %_sysconfdir/nginx/sites-available
#%%config(noreplace) %attr(0640,nginx,z-push) %_sysconfdir/nginx/sites-available/z-push.conf

%changelog

* Mon Dec 28 2020 Mark Verlinde <mark.verlinde@gmail.com> - 2.6.1-1
- update to 2.6.1
- require rh-php73

* Wed Oct 2 2019 Verlinde <mark.verlinde@gmail.com> - 2.5.1
- intial build
- require rh-php72