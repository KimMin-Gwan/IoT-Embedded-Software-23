#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/slab.h>
#include <linux/io.h>
#include <linux/gpio.h>
#include <asm/uaccess.h>

#define LED_MAJOR 220
#define LED_NAME "LED_DRIVER"
//#define GPIO_BASE 0xFE000000
#define GPIO_SIZE 256
#define GPIO_BASE (0xFE000000 + 0x200000)

static int led_usage = 0;
static void *led_map;
volatile unsigned *led;

static int led_open(struct inode *minode, struct file *mfile)
{
	if (led_usage != 0)
		return -EBUSY;
	led_usage = 1;

	led_map = ioremap(GPIO_BASE, GPIO_SIZE);
	if (!led_map)
	{
		printk("error: mapping gpio memory");
		iounmap(led_map);
		return -EBUSY;
	}

	led = (volatile unsigned int *)led_map;
	*(led + 1) &= ~(0x7 << (3 * 7));
	*(led + 1) |= (0x1 << (3 * 7));

	return 0;
}

static int led_release(struct inode *minode, struct file *mfile)
{
	led_usage = 0;
	if (led)
		iounmap(led);

	return 0;
}

static ssize_t led_write(struct file *mfile, const char *gdata, size_t length, loff_t *off_what)
{
	char tmp_buf;
	int result;

	result = copy_from_user(&tmp_buf, gdata, length);
	if (result < 0)
	{
		printk("Error: copy from user");
		return result;
	}

	printk("data from app : %d\n", tmp_buf);

	if (tmp_buf != 0)
		*(led + 7) |= (0x1 << 17);
	else
		*(led + 10) |= (0x1 << 17);

	return length;
}

static struct file_operations led_fops =
{
	.owner = THIS_MODULE,
	.open = led_open,
	.release = led_release,
	.write = led_write,
};

static int led_init(void)
{
	int result;

	result = register_chrdev(LED_MAJOR, LED_NAME, &led_fops);
	if (result < 0)
	{
		printk(KERN_WARNING "Can't get any major!\n");
		return result;
	}
	return 0;
}

static void led_exit(void)
{
	unregister_chrdev(LED_MAJOR, LED_NAME);
	printk("LED module removed.\n");
}

module_init(led_init);
module_exit(led_exit);

MODULE_LICENSE("GPL");
