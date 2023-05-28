KDIR = /lib/modules/$(shell uname -r)/build
TOOLCHAIN = arm-linux-gnueabihf-
CC = $(TOOLCHAIN)gcc
obj-m := photoregister_driver.o
all: driver
driver:
	$(MAKE) -C $(KDIR) M=$$PWD modules
clean:
	$(MAKE) -C $(KDIR) M=$$PWD clean
