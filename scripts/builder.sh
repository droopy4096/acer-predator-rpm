#!/bin/sh -x 

SPECFILE=${1:-SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module-kmod.spec}

dnf builddep -y ${SPECFILE}
spectool --define "_topdir ${PWD}" -g -R ${SPECFILE} 

rpmbuild --define "_topdir ${PWD}" -ba ${SPECFILE}