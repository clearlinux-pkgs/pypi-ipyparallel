#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipyparallel
Version  : 8.3.0
Release  : 12
URL      : https://files.pythonhosted.org/packages/2a/c9/6e1bef0aef78b3db6e2070d2c9a25d3184e74fad76a919ff6b82de8a1970/ipyparallel-8.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/c9/6e1bef0aef78b3db6e2070d2c9a25d3184e74fad76a919ff6b82de8a1970/ipyparallel-8.3.0.tar.gz
Summary  : Interactive Parallel Computing with IPython
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ipyparallel-bin = %{version}-%{release}
Requires: pypi-ipyparallel-data = %{version}-%{release}
Requires: pypi-ipyparallel-license = %{version}-%{release}
Requires: pypi-ipyparallel-python = %{version}-%{release}
Requires: pypi-ipyparallel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(jupyterlab)

%description
# Interactive Parallel Computing with IPython
IPython Parallel (`ipyparallel`) is a Python package and collection of CLI scripts for controlling clusters of IPython processes, built on the Jupyter protocol.

%package bin
Summary: bin components for the pypi-ipyparallel package.
Group: Binaries
Requires: pypi-ipyparallel-data = %{version}-%{release}
Requires: pypi-ipyparallel-license = %{version}-%{release}

%description bin
bin components for the pypi-ipyparallel package.


%package data
Summary: data components for the pypi-ipyparallel package.
Group: Data

%description data
data components for the pypi-ipyparallel package.


%package license
Summary: license components for the pypi-ipyparallel package.
Group: Default

%description license
license components for the pypi-ipyparallel package.


%package python
Summary: python components for the pypi-ipyparallel package.
Group: Default
Requires: pypi-ipyparallel-python3 = %{version}-%{release}

%description python
python components for the pypi-ipyparallel package.


%package python3
Summary: python3 components for the pypi-ipyparallel package.
Group: Default
Requires: python3-core
Provides: pypi(ipyparallel)
Requires: pypi(decorator)
Requires: pypi(entrypoints)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(psutil)
Requires: pypi(python_dateutil)
Requires: pypi(pyzmq)
Requires: pypi(tornado)
Requires: pypi(tqdm)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-ipyparallel package.


%prep
%setup -q -n ipyparallel-8.3.0
cd %{_builddir}/ipyparallel-8.3.0
pushd ..
cp -a ipyparallel-8.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656526743
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipyparallel
cp %{_builddir}/ipyparallel-8.3.0/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-ipyparallel/2c15eff35efcbd62ef860412b46613a6a194fbc3
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_notebook_config.d/ipyparallel.json
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_server_config.d/ipyparallel.json
rm -f %{buildroot}*/usr/etc/jupyter/nbconfig/tree.d/ipyparallel.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipcluster
/usr/bin/ipcontroller
/usr/bin/ipengine

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/ipyparallel-labextension/package.json
/usr/share/jupyter/labextensions/ipyparallel-labextension/schemas/ipyparallel-labextension/package.json.orig
/usr/share/jupyter/labextensions/ipyparallel-labextension/schemas/ipyparallel-labextension/plugin.json
/usr/share/jupyter/labextensions/ipyparallel-labextension/static/114.66e59b086d0542d83a0b.js
/usr/share/jupyter/labextensions/ipyparallel-labextension/static/592.a995f9fa3b86006d200a.js
/usr/share/jupyter/labextensions/ipyparallel-labextension/static/remoteEntry.7f82cb668ab24ab4675c.js
/usr/share/jupyter/labextensions/ipyparallel-labextension/static/style.js
/usr/share/jupyter/labextensions/ipyparallel-labextension/static/third-party-licenses.json
/usr/share/jupyter/nbextensions/ipyparallel/clusterlist.css
/usr/share/jupyter/nbextensions/ipyparallel/clusterlist.js
/usr/share/jupyter/nbextensions/ipyparallel/main.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipyparallel/2c15eff35efcbd62ef860412b46613a6a194fbc3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
