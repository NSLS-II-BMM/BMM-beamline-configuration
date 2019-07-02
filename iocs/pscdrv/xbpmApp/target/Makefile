CROSS_COMPILE=/opt/buildroot/2015.05/output/host/usr/bin/arm-buildroot-linux-gnueabi-
ARCH=arm

ifeq ($(KERNELRELEASE),)
# Non-kernel build (entry point)

## build for target kernel
KERNELDIR=$(dir $(firstword $(wildcard /opt/buildroot/2015.05/output/build/linux-*/Module.symvers)))
## Test build w/ host kernel
#KERNELDIR ?= /lib/modules/$(shell uname -r)/build



CC=$(CROSS_COMPILE)gcc

CFLAGS=-g -O2 -Wall
LDFLAGS=-g -pthread

LDADD=-Wl,-Bstatic -levent_core -Wl,-Bdynamic

all: xbpm uioread module-modules

xbpm: main.o app.o
uioread: uioread.o

xbpm uioread:
	$(CC) -o $@ $(LDFLAGS) $^ $(LDADD) $($*_LDADD)

%.o: %.c
	$(CC) -o $@ -c $< $(CPPFLAGS) $(CFLAGS)

module-%::
	$(MAKE) -C $(KERNELDIR) M=$(PWD) ARCH=$(ARCH) CROSS_COMPILE=$(CROSS_COMPILE) $*

clean: module-clean
	rm -f xbpm *.o

else
# Kernel build

  obj-m := xbpm.o

  xbpm-objs := uio_xbpm.o

endif
