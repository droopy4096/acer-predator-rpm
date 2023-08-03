.PHONY: kmod driver

CONTAINER_BUILDER?=podman
FEDORA_VERSION?=37
CONTAINER_NAME=fedora-builder-$(FEDORA_VERSION)

kmod:
	rpmbuild --define "_topdir ${PWD}" -ba SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module-kmod.spec 

driver:
	rpmbuild --define "_topdir ${PWD}" -ba SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module.spec

container:
	$(CONTAINER_BUILDER) build --build-arg FEDORA_VERSION=$(FEDORA_VERSION) -f Dockerfile -t $(CONTAINER_NAME) .