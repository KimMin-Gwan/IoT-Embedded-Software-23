#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/slab.h>
#include <linux/gpio.h>
#include <linux/io.h>
#include <linux/poll.h>
#include <linux/interrupt.h>
#include <linux/irq.h>
#include <linux/sched.h>
#include <linux/wait.h>

#define PHOTOREGISTER_MAJOR 222
#define PHOTOREGISTER_NAME "PHOTOREGISTER_DRIVER"

#define BCM2711_PERL_BASE 0xFE000000
#define GPIO_BASE (BCM2711_PERL_BASE + 0x200000)
#define GPIO_SIZE 256

#define INPUT_PIN 21

char photoregister_usage = 0;
static void *photoregister_map;
volatile unsigned *photoregister;

DECLARE_WAIT_QUEUE_HEAD(waitqueue);

static int photoregister_open(struct inode *minode, struct file *mfile)
{
    if (photoregister_usage != 0)
        return -EBUSY;
    photoregister_usage = 1;

    photoregister_map = ioremap(GPIO_BASE, GPIO_SIZE);
    if (!photoregister_map)
    {
        printk("error: mapping gpio memory");
        iounmap(photoregister_map);
        return -EBUSY;
    }

    photoregister = (volatile unsigned int *)photoregister_map;
    *(photoregister + 2) &= ~(0x7 << (3 * 1));
    *(photoregister + 2) |= (0x0 << (3 * 1));

    return 0;
}

static int photoregister_release(struct inode *minode, struct file *mfile)
{

    photoregister_usage = 0;
    if (photoregister)
        iounmap(photoregister);

    return 0;
}

static ssize_t photoregister_read(struct file *mfile, const char *gdata, size_t length, loff_t *off_what)
{
    int value = gpio_get_value(INPUT_PIN);
    char *result;
    
    result = kmalloc(length, GFP_KERNEL);
    if (result == NULL)
        return -1;
     
     *result = value;

    int ret = copy_to_user(gdata, result, sizeof(char))
    if (ret < 0)
        retun - 1;
    
    return length
}

static struct file_operations photoregister_fops =
    {
        .owner = THIS_MODULE,
        .open = photoregister_open,
        .release = photoregister_release,
        .read = photoregister_read,
};

static int photoregister_init(void)
{
    int result;
    result = register_chrdev(PHOTOREGISTER_MAJOR, PHOTOREGISTER_NAME, &photoregister_fops);
    if (result < 0)
    {
        printk("KERN_WARNING Can't get any major!\n");
        return result;
    }
    printk("PHOTOREGISTER module uploded.\n");
    return 0;
}

static void photoregister_exit(void)
{
    unregister_chrdev(PHOTOREGISTER_MAJOR, PHOTOREGISTER_NAME);
    printk("PHOTOREGISTER module removed.\n");
}

module_init(photoregister_init);
module_exit(photoregister_exit);

MODULE_LICENSE("GPL");
