#!/bin/sh

SPECFILE=${1:-SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module-kmod.spec}

dnf builddep -y ${SPECFILE}
spectool -g -R ${SPECFILE} -C SOURCES

rpmbuild --define "_topdir ${PWD}" -ba ${SPECFILE}