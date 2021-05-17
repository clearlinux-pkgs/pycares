#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycares
Version  : 4.0.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/25/5a/ed8cc3340b7e83a5e572b5d27387a968a7e52b1e3c269442076ca902b7ba/pycares-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/25/5a/ed8cc3340b7e83a5e572b5d27387a968a7e52b1e3c269442076ca902b7ba/pycares-4.0.0.tar.gz
Summary  : Python interface for c-ares
Group    : Development/Tools
License  : MIT
Requires: pycares-license = %{version}-%{release}
Requires: pycares-python = %{version}-%{release}
Requires: pycares-python3 = %{version}-%{release}
Requires: cffi
Requires: idna
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : idna
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===========================

%package license
Summary: license components for the pycares package.
Group: Default

%description license
license components for the pycares package.


%package python
Summary: python components for the pycares package.
Group: Default
Requires: pycares-python3 = %{version}-%{release}

%description python
python components for the pycares package.


%package python3
Summary: python3 components for the pycares package.
Group: Default
Requires: python3-core
Provides: pypi(pycares)
Requires: pypi(cffi)

%description python3
python3 components for the pycares package.


%prep
%setup -q -n pycares-4.0.0
cd %{_builddir}/pycares-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621260263
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycares
cp %{_builddir}/pycares-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b
cp %{_builddir}/pycares-4.0.0/deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/pycares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b
/usr/share/package-licenses/pycares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
