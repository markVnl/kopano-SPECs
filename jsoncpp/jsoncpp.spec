%global jsondir json

Name:       jsoncpp
Version:    1.7.7
Release:    1%{?dist}
Summary:    JSON library implemented in C++

License:    Public Domain or MIT
URL:        https://github.com/open-source-parsers/jsoncpp
Source0:    https://github.com/open-source-parsers/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python

%description
%{name} is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.


%package devel
Summary:    Development headers and library for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.


%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
This package contains the documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake -DBUILD_STATIC_LIBS=OFF                \
       -DJSONCPP_WITH_WARNING_AS_ERROR=OFF    \
       -DJSONCPP_WITH_PKGCONFIG_SUPPORT=ON    \
       -DJSONCPP_WITH_CMAKE_PACKAGE=ON        \
       .
make %{?_smp_mflags}
# Build the doc
python doxybuild.py --with-dot --doxygen %{_bindir}/doxygen


%install
make install DESTDIR=%{buildroot}

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/html
for f in NEWS.txt README.md ; do
    install -p -m 0644 $f $RPM_BUILD_ROOT%{_docdir}/%{name}
done
install -p -m 0644 dist/doxygen/*/*.{html,png} $RPM_BUILD_ROOT%{_docdir}/%{name}/html


%check
# Tests are run automatically in the build section
# ctest -V %{?_smp_mflags}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license AUTHORS LICENSE
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%exclude %{_docdir}/%{name}/html
%{_libdir}/lib%{name}.so.*


%files devel
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/NEWS.txt
%{_libdir}/lib%{name}.so
%{_includedir}/%{jsondir}/
%{_libdir}/cmake
%{_libdir}/pkgconfig/jsoncpp.pc


%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_docdir}/%{name}/


%changelog
* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 1.7.7-1
- Update to version 1.7.7 (#1372329)

* Sun Jul 17 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.7.4-1
- Update to version 1.7.4

* Mon Jun 20 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.7.2-3
- Revert #1336082

* Mon Jun 13 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.7.2-2
- Fix include dir path (#1336082)

* Sat Mar 26 2016 Björn Esser <fedora@besser82.io> - 1.7.2-1
- Update to version 1.7.2

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 1.7.1-1
- Update to version 1.7.1
- Use %%license and %%doc properly
- Add generated CMake-target
- Move %%check after %%install
- Remove Group-tag, needed for el <= 5, only
- Drop Patch0, not needed anymore

* Tue Feb 16 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.10.5-4
- Disabled Werror

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan  3 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.10.5-2
- Add disttag

* Sun Jan 03 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.10.5-2
- Use cmake instead of scons

* Sun Sep 13 2015 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.10.5-1
- Update to version 0.10.5

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 0.6.0-0.18.rc2
- Link libjsoncpp with -z now

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.17.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-0.16.rc2
- Rebuild for gcc 5 C++11 ABI change

* Mon Feb 16 2015 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-0.15.rc2
- Rebuild for gcc 5 C++11

* Sun Sep 21 2014 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.14.rc2
- Allow int values to be converted to string (#1143774)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.13.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.11.rc2
- https://bugzilla.redhat.com/show_bug.cgi?id=998149 : applied Michael Schwendt's
  patch to fix duplicated documentation

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.10.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.9.rc2
- Changed Summary
- Added %%doc files to the doc package
- Added python as an explicit BuildRequires

* Fri Feb 15 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.8.rc2
- Added documentation sub-package

* Sun Jan 20 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.7.rc2
- Added graphviz as a BuildRequire

* Sat Jan 19 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.6.rc2
- Install the corrected library

* Sat Dec 22 2012 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.5.rc2
- Added libjsoncpp.so.0
- Moved the shared lib build to the correct section

* Fri Dec 21 2012 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.4.rc2
- Removed doc subpackage
- Added .pc file
- Fixed shared lib

* Wed Dec 12 2012 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.3.rc2
- Removed static package
- Preserving timestamp on installed files
- Added guard grep to the sed expression
- Removed duplicated doc files
- Removed dependency on pkgconfig
- Changed base package group

* Sun Dec 02 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.2.rc2
- Changed license field to Public Domain or MIT

* Tue Nov 27 2012 Sébastien Willmann <sebastien.willmann@gmail.com> 0.6.0-0.1.rc2
- Creation of the spec file

