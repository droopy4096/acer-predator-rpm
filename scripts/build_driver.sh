#!/bin/sh -x

set -e

dnf install -y \
    ./RPMS/x86_64/acer-predator-turbo-and-rgb-keyboard-linux-module-kmodsrc-0-1.20221223git8c2b628.fc37.x86_64.rpm # \
    # ./RPMS/x86_64/akmod-acer-predator-turbo-and-rgb-keyboard-linux-module-0-1.20221223git8c2b628.fc37.x86_64.rpm \
    # ./RPMS/x86_64/kmod-acer-predator-turbo-and-rgb-keyboard-linux-module-0-1.20221223git8c2b628.fc37.x86_64.rpm

scripts/builder.sh $@