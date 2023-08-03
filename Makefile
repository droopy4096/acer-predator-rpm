.PHONY: kmod driver

CONTAINER_ENGINE?=podman
FEDORA_VERSION?=37
CONTAINER_NAME=fedora-builder:$(FEDORA_VERSION)

kmod:
	# rpmbuild --define "_topdir ${PWD}" -ba SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module-kmod.spec 
	$(CONTAINER_ENGINE) run --rm -t -v ${PWD}:/src:Z -w /src $(CONTAINER_NAME) scripts/builder.sh SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module-kmod.spec 

driver:
	# rmbuild --define "_topdir ${PWD}" -ba SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module.spec
	$(CONTAINER_ENGINE) run --rm -t -v ${PWD}:/src:Z -w /src $(CONTAINER_NAME) scripts/build_driver.sh SPECS/acer-predator-turbo-and-rgb-keyboard-linux-module.spec

container:
	$(CONTAINER_ENGINE) build --build-arg FEDORA_VERSION=$(FEDORA_VERSION) -f Dockerfile -t $(CONTAINER_NAME) .