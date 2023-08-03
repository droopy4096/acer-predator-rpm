FROM fedora:$FEDORA_VERSION
ARG FEDORA_VERSION

RUN dnf update -y
# get rpmfusion
RUN dnf install -y rpm-build dnf-plugins-core rpmdevtools
RUN dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm