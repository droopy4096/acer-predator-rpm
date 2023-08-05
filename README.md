https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues/75

# How to compile

## Setup

It's important to set up target Fedora version for all subsequent operations
```shell
export FEDORA_VERSION=38
```
## Build compiler container

```shell
make container
```

## Build kmod

```shell
make kmod
```

## Build driver

```shell
make driver
```

## RPMs

resulting RPMs will be in `RPMS/x86_64` directory.