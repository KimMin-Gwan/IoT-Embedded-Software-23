#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
	{ 0xedc03953, "iounmap" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x1ec5db1a, "__register_chrdev" },
	{ 0x92997ed8, "_printk" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x1d37eeed, "ioremap" },
	{ 0x17b8e2f4, "gpio_to_desc" },
	{ 0x6761c53d, "gpiod_get_raw_value" },
	{ 0x2d6fcc06, "__kmalloc" },
	{ 0x51a910c0, "arm_copy_to_user" },
	{ 0x78a319e7, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "DF57EDE0783195ED1E4F55D");
