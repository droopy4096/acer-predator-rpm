%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

%global prjname acer-predator-turbo-and-rgb-keyboard-linux-module

%global gitabbrev 8c2b628
%global gitdate 20221223
%global rel %{gitdate}git%{gitabbrev}

Name:           %{prjname}-kmod
Summary:        Kernel module (kmod) for %{prjname}
Version:        0
Release:        1%{?rel:.%{rel}}%{?dist}
License:        GPLv2+

URL:            https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
# Source0:        %{url}/archive/v%{version}/%{prjname}-%{version}%{?gitdate:-%{rel}}.tar.gz
Source0:        https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/archive/refs/heads/main.zip

BuildRequires:  gcc
BuildRequires:  elfutils-libelf-devel
BuildRequires:  kmodtool
%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool magic
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{prjname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Unofficial Acer Gaming RGB keyboard backlight and Turbo mode Linux kernel module (Acer Predator, Acer Helios, Acer Nitro)

Inspired by [faustus(for asus)](https://github.com/hackbnw/faustus), this project extends current acer-wmi linux kernel module to support Acer gaming functions.

**Warning**
Use at your own risk! Acer was not involved in developing this driver, and everything is developed by reverse engeineering official Predator Sense app. This driver interacts with low-level WMI methods which haven't been tested on all series.

Also, this package blacklists the builtin acer_wmi kernel module.


%package -n %{prjname}-kmodsrc
Summary: module sources for %{name}

%description -n %{prjname}-kmodsrc
Source tree.


%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu} --repo rpmfusion --kmodname %{prjname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c

for kernel_version  in %{?kernel_versions} ; do
  cp -a %{prjname} _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{prjname}
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{prjname}


for kernel_version in %{?kernel_versions}; do
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
  install -D -m 755 _kmod_build_${kernel_version%%___*}/src/facer.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
  chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}

%files -n %{prjname}-kmodsrc
%{_datadir}/%{prjname}


%changelog
* Fri Jan 06 2023 Andrea Santilli - 0-1.20221223git8c2b628
- Initial akmod RPM release.

