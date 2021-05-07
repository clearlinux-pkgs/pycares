#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycares
Version  : 3.1.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/4e/09/f49ef1c4b6a5ad50fc08a8acd015f1938594dd7a6b4a6a96d049d9bbec7d/pycares-3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/09/f49ef1c4b6a5ad50fc08a8acd015f1938594dd7a6b4a6a96d049d9bbec7d/pycares-3.1.1.tar.gz
Summary  : Python interface for c-ares
Group    : Development/Tools
License  : MIT
Requires: pycares-license = %{version}-%{release}
Requires: pycares-python = %{version}-%{release}
Requires: pycares-python3 = %{version}-%{release}
Requires: cffi
Requires: idna
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : idna
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
====================================

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
%setup -q -n pycares-3.1.1
cd %{_builddir}/pycares-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602521705
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
cp %{_builddir}/pycares-3.1.1/LICENSE %{buildroot}/usr/share/package-licenses/pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
