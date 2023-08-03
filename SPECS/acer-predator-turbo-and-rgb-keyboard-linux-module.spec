%global gitabbrev 8c2b628
%global gitdate 20221223
%global rel %{gitdate}git%{gitabbrev}


Name:           acer-predator-turbo-and-rgb-keyboard-linux-module
Summary:        Kernel module (kmod) for %{name}
Version:        0
Release:        1%{?rel:.%{rel}}%{?dist}
License:        GPLv2
URL:            https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
%if 0%{?fedora} || 0%{?rhel} > 7
%global        _dracutopts          rd.driver.blacklist=acer_wmi modprobe.blacklist=acer_wmi
%else
%global        _dracutopts          rd.driver.blacklist=acer_wmi
%endif

%global        debug_package %{nil}

ExclusiveArch:  i686 x86_64
BuildRequires:  %{name}-kmodsrc >= %{version}
Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}
Requires:       grubby
Requires:       python3


%description
%{name} common files.

%prep
#setup -q -c
tar zxvf %{_datadir}/%{name}/%{name}-%{version}-%{rel}.tar.gz


%build
#Nothing to build
cat > %{name}.conf << EOF
wmi
sparse-keymap
video
facer
EOF


%install
install -m755 -d $RPM_BUILD_ROOT%{_sysconfdir}/modules-load.d/
install -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/modules-load.d/%{name}.conf

tar zxvf %{_datadir}/%{name}/%{name}-%{version}-%{rel}.tar.gz
install -m755 -d $RPM_BUILD_ROOT%{_bindir}
install -m755 %{name}/facer_rgb.py $RPM_BUILD_ROOT%{_bindir}

%post
_acerwmitest=$(lsmod | awk '{print $1}' | grep ^acer_wmi$)
if [ ! "x${_acerwmitest}" = "x" ]; then
  rmmod acer_wmi
fi

if [ "$1" -eq "1" ]; then
  sed -i -e 's/GRUB_CMDLINE_LINUX="/GRUB_CMDLINE_LINUX="%{_dracutopts} /g' /etc/default/grub
fi || :

if [ -f %{_sysconfdir}/default/grub ] ; then
  . %{_sysconfdir}/default/grub
  if [ -z "${GRUB_CMDLINE_LINUX+x}" ]; then
    echo -e GRUB_CMDLINE_LINUX=\"%{_dracutopts}\" >> %{_sysconfdir}/default/grub
  else
    for i in %{_dracutopts} ; do
      _has_string=$(echo ${GRUB_CMDLINE_LINUX} | grep -F -c $i)
      if [ x"$_has_string" = x0 ] ; then
        GRUB_CMDLINE_LINUX="${GRUB_CMDLINE_LINUX} ${i}"
      fi
    done
    sed -i -e "s|^GRUB_CMDLINE_LINUX=.*|GRUB_CMDLINE_LINUX=\"${GRUB_CMDLINE_LINUX}\"|g" %{_sysconfdir}/default/grub
  fi
fi
/usr/sbin/grubby --args='%{_dracutopts}' &>/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
  /usr/sbin/grubby --remove-args='%{_dracutopts}' &>/dev/null
  sed -i -e 's/%{_dracutopts} //g' /etc/default/grub
fi ||:


%files
%{_sysconfdir}/modules-load.d/%{name}.conf
%{_bindir}/*

%changelog
* Thu Jan 05 2023 Andrea Santilli - 1.0.2-20221210git80a31d7
- Initial akmod RPM release.

