#!/bin/sh

dnf builddep SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module.spec
rpmbuild --define "_topdir ${PWD}" -ba SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module.spec