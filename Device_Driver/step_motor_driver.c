#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/slab.h>
#include <linux/gpio.h>
#include <mach/platform.h>
#include <linux/io.h>
#include <linux/version.h>
#include <asm/delay.h>
#include <linux/proc_fs.h>

#define SM_MAJOR 68
#define SM_NAME "SM_DRIVER"
#define SPEED_DELAY 20000 // 500 ~ 20000
#define GPIO_SIZE 256

// 4개 GPIO
#define GPIO1 81
#define GPIO2 82
#define GPIO3 83
#define GPIO4 84

char sm_usage = 0;
static void *sm_map;
volatile unsigned *sm;

// loopcnt만큼 정방향 회전
static void run_sm(int loopcnt)
{
    int i;

    for (i = 0; i < loopcnt; i++)
    {
        GPSR2 = (1 << (GPIO1 - 64));
        GPCR2 = (1 << (GPIO2 - 64));
        udelay(SPEED_DELAY);
        GPSR2 = (1 << (GPIO3 - 64));
        GPCR2 = (1 << (GPIO4 - 64));
        udelay(SPEED_DELAY);
        GPCR2 = (1 << (GPIO1 - 64));
        GPSR2 = (1 << (GPIO2 - 64));
        udelay(SPEED_DELAY);
        GPCR2 = (1 << (GPIO3 - 64));
        GPSR2 = (1 << (GPIO4 - 64));
        udelay(SPEED_DELAY);
    }
}

// loopcnt만큼 역방향 회전
static void rev_run_sm(int loopcnt)
{
    int i;

    for (i = 0; i < loopcnt; i++)
    {
        GPSR2 = (1 << (GPIO3 - 64));
        GPCR2 = (1 << (GPIO4 - 64));
        udelay(SPEED_DELAY);
        GPSR2 = (1 << (GPIO1 - 64));
        GPCR2 = (1 << (GPIO2 - 64));
        udelay(SPEED_DELAY);
        GPCR2 = (1 << (GPIO3 - 64));
        GPSR2 = (1 << (GPIO4 - 64));
        udelay(SPEED_DELAY);
        GPCR2 = (1 << (GPIO1 - 64));
        GPSR2 = (1 << (GPIO2 - 64));
        udelay(SPEED_DELAY);
    }
}

static int sm_open(struct inode *inode, struct file *filp)
{
    /*
    if (sm_usage != 0)
        return -EBUSY;
    sm_usage = 1;

    sm_map = ioremap(GPIO_BASE, GPIO_SIZE);
    if (!sm_map)
    {
        printk("error: mapping gpio memory");
        iounmap(sm_map);
        return _EBUSY;
    }

    sm = (volatile unsigned int *)sm_map;
    *(sm + 1) &= ~(0x7 << (3 * 7));
    *(sm + 1) |= ~(0x1 << (3 * 7));

    return 0;
    */
   
    int reg;

    reg = (GPLR2 & 0x001E0000) >> 17;
    reg = (GPDR2 & 0x001E0000) >> 17;

    MOD_INC_USE_COUNT;
    return 0;
}

static int sm_release(struct inode *inode, struct file *filp)
{
    MOD_DEC_USE_COUNT;
    return 0;
}

static static ssize_t sm_write(struct file *filp, const char *buffer, size_t length, loff_t *offset)
{
    int mode;
    size_t len;

    printk("sm_write: stepmotor operation\n");
    len = length;
    get_user(mode, (int *)buffer);

    switch (mode)
    {
    case 1:
        run_sm(30);
        break;
    case 2:
        rev_run_sm(30);
        break;
    default:
        break;
    }

    return len;
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