#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liberasurecode
Version  : 1.5.0
Release  : 15
URL      : https://github.com/openstack/liberasurecode/archive/1.5.0.tar.gz
Source0  : https://github.com/openstack/liberasurecode/archive/1.5.0.tar.gz
Summary  : Naive Reed-Soloman Vandermonde Backend built-in to liberasurecode
Group    : Development/Tools
License  : BSD-2-Clause
Requires: liberasurecode-lib
Requires: liberasurecode-license

%description
liberasurecode
==============
liberasurecode is an Erasure Code API library written in C with pluggable Erasure Code backends.

%package dev
Summary: dev components for the liberasurecode package.
Group: Development
Requires: liberasurecode-lib
Provides: liberasurecode-devel

%description dev
dev components for the liberasurecode package.


%package lib
Summary: lib components for the liberasurecode package.
Group: Libraries
Requires: liberasurecode-license

%description lib
lib components for the liberasurecode package.


%package license
Summary: license components for the liberasurecode package.
Group: Default

%description license
license components for the liberasurecode package.


%prep
%setup -q -n liberasurecode-1.5.0
pushd ..
cp -a liberasurecode-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533876341
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell "
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell "
export LDFLAGS="$LDFLAGS -m64 -march=haswell "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1533876341
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/liberasurecode
cp COPYING %{buildroot}/usr/share/doc/liberasurecode/COPYING
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/liberasurecode/alg_sig.h
/usr/include/liberasurecode/config_liberasurecode.h
/usr/include/liberasurecode/erasurecode.h
/usr/include/liberasurecode/erasurecode_backend.h
/usr/include/liberasurecode/erasurecode_helpers.h
/usr/include/liberasurecode/erasurecode_helpers_ext.h
/usr/include/liberasurecode/erasurecode_log.h
/usr/include/liberasurecode/erasurecode_postprocessing.h
/usr/include/liberasurecode/erasurecode_preprocessing.h
/usr/include/liberasurecode/erasurecode_stdinc.h
/usr/include/liberasurecode/erasurecode_version.h
/usr/include/liberasurecode/liberasurecode_rs_vand.h
/usr/include/liberasurecode/list.h
/usr/include/liberasurecode/rs_galois.h
/usr/include/liberasurecode/xor_code.h
/usr/include/liberasurecode/xor_hd_code_defs.h
/usr/lib64/haswell/libXorcode.so
/usr/lib64/haswell/liberasurecode.so
/usr/lib64/haswell/liberasurecode_rs_vand.so
/usr/lib64/libXorcode.so
/usr/lib64/liberasurecode.so
/usr/lib64/liberasurecode_rs_vand.so
/usr/lib64/libnullcode.so
/usr/lib64/pkgconfig/erasurecode-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libXorcode.so.1
/usr/lib64/haswell/libXorcode.so.1.0.1
/usr/lib64/haswell/liberasurecode.so.1
/usr/lib64/haswell/liberasurecode.so.1.5.0
/usr/lib64/haswell/liberasurecode_rs_vand.so.1
/usr/lib64/haswell/liberasurecode_rs_vand.so.1.0.1
/usr/lib64/libXorcode.so.1
/usr/lib64/libXorcode.so.1.0.1
/usr/lib64/liberasurecode.so.1
/usr/lib64/liberasurecode.so.1.5.0
/usr/lib64/liberasurecode_rs_vand.so.1
/usr/lib64/liberasurecode_rs_vand.so.1.0.1
/usr/lib64/libnullcode.so.1
/usr/lib64/libnullcode.so.1.0.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/liberasurecode/COPYING
