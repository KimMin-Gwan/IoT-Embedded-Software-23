#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/slab.h>
#include <linux/io.h>
#include <linux/gpio.h>
#include <linux/version.h>
#include <linux/delay.h>
#include <asm/io.h>
#include <asm/delay.h>
#include <asm/uaccess.h>

#define SM_MAJOR 221
#define SM_NAME "SM_DRIVER"
#define SPEED_DELAY 1 // 500 ~ 20000

#define BCM2711_PERL_BASE 0xFE000000
#define GPIO_BASE (BCM2711_PERL_BASE + 0x200000)
#define GPIO_SIZE 256

// 4개 GPIO PIN
#define SM_PIN_1 22
#define SM_PIN_2 23
#define SM_PIN_3 24
#define SM_PIN_4 25

static int sm_usage = 0;
static void *sm_map;
volatile unsigned *sm;


static int sm_open(struct inode *minode, struct file *mfile)
{
	if (sm_usage != 0)
		return -EBUSY;
	sm_usage = 1;

	sm_map = ioremap(GPIO_BASE, GPIO_SIZE);
	if (!sm_map)
	{
		printk("error: mapping gpio memory");
		iounmap(sm_map);
		return -EBUSY;
	}

	sm = (volatile unsigned int *)sm_map;

	*(sm + 2) &= ~(0x7 << (3 * 2));
	*(sm + 2) |= (0x1 << (3 * 2));

	*(sm + 2) &= ~(0x7 << (3 * 3));
	*(sm + 2) |= (0x1 << (3 * 3));

	*(sm + 2) &= ~(0x7 << (3 * 4));
	*(sm + 2) |= (0x1 << (3 * 4));

	*(sm + 2) &= ~(0x7 << (3 * 5));
	*(sm + 2) |= (0x1 << (3 * 5));

	return 0;
}

static int sm_release(struct inode *minode, struct file *mfile)
{
	sm_usage = 0;
	if (sm)
		iounmap(sm);

	return 0;
}

static ssize_t sm_write(struct file *mfile, const char *gdata, size_t length, loff_t *offset)
{
	char mode;

	int ret = copy_from_user(&mode, gdata, length);
	if (ret < 0)
		return - 1;

        if(mode == 1)
        {
            *(sm + 7) = (0x1 << SM_PIN_1);
            *(sm + 10) = (0x1 << SM_PIN_4);
            mdelay(10);
            *(sm + 7) = (0x1 << SM_PIN_2);
            *(sm + 10) = (0x1 << SM_PIN_1);
            mdelay(10);
            *(sm + 7) = (0x1 << SM_PIN_3);
            *(sm + 10) = (0x1 << SM_PIN_2);
            mdelay(10);
            *(sm + 7) = (0x1 << SM_PIN_4);
            *(sm + 10) = (0x1 << SM_PIN_3);
            mdelay(10);
        }

        else
        {
            *(sm + 7) = (0x1 << SM_PIN_1);
            *(sm + 10) = (0x1 << SM_PIN_2);
            mdelay(10);
            *(sm + 7) = (0x1 << SM_PIN_4);
            *(sm + 10) = (0x1 << SM_PIN_1);
            mdelay(10);
            *(sm + 7) = (0x1 << SM_PIN_3);
            *(sm + 10) = (0x1 << SM_PIN_4);
            mdelay(10);
            *(sm + 7) = (0x1 << SM_PIN_2);
            *(sm + 10) = (0x1 << SM_PIN_3);
            mdelay(10);
        } 
        return length;
}

static struct file_operations sm_fops =
{
	.owner = THIS_MODULE,
	.open = sm_open,
	.release = sm_release,
	.write = sm_write,
};

static int sm_init(void)
{
	int result;

	result = register_chrdev(SM_MAJOR, SM_NAME, &sm_fops);
	if (result < 0)
	{
		printk(KERN_WARNING "Can't get any major!\n");
		return result;
	}
	return result;
}

static void sm_exit(void)
{
	unregister_chrdev(SM_MAJOR, SM_NAME);
	printk("SM module removed.\n");
}

module_init(sm_init);
module_exit(sm_exit);

MODULE_LICENSE("GPL");
