#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/slab.h>
#include <linux/io.h>
#include <linux/gpio.h>
#include <linux/version.h>
#include <asm/io.h>
#include <asm/delay.h>
#include <asm/uaccess.h>
#include <mach/platform.h>

#define SM_MAJOR 221
#define SM_NAME "SM_DRIVER"
#define SPEED_DELAY 20000 // 500 ~ 20000
#define GPIO_SIZE 256

// 4개 GPIO PIN
#define SM_PIN_1 22
#define SM_PIN_2 23
#define SM_PIN_3 24
#define SM_PIN_4 25

static int sm_usage = 0;
static void *sm_map;
volatile unsigned *sm;

// loopcnt만큼 정방향 회전
static void run_sm(int loopcnt)
{
    int i;

    for (i = 0; i < loopcnt; i++)
    {
        *(sm + 7) = (0x1 << SM_PIN_1);
        *(sm + 10) = (0x1 << SM_PIN_2);
        udelay(SPEED_DELAY);
        *(sm + 7) = (0x1 << SM_PIN_3);
        *(sm + 10) = (0x1 << SM_PIN_4);
        udelay(SPEED_DELAY);
        *(sm + 7) = (0x1 << SM_PIN_1);
        *(sm + 10) = (0x1 << SM_PIN_2);
        udelay(SPEED_DELAY);
        *(sm + 7) = (0x1 << SM_PIN_3);
        *(sm + 10) = (0x1 << SM_PIN_4);
        udelay(SPEED_DELAY);
    }
}

// loopcnt만큼 역방향 회전
static void rev_run_sm(int loopcnt)
{
    int i;

    for (i = 0; i < loopcnt; i++)
    {
    for (i = 0; i < loopcnt; i++)
    {
        *(sm + 7) = (0x1 << SM_PIN_3);
        *(sm + 10) = (0x1 << SM_PIN_4);
        udelay(SPEED_DELAY);
        *(sm + 7) = (0x1 << SM_PIN_1);
        *(sm + 10) = (0x1 << SM_PIN_2);
        udelay(SPEED_DELAY);
        *(sm + 7) = (0x1 << SM_PIN_3);
        *(sm + 10) = (0x1 << SM_PIN_4);
        udelay(SPEED_DELAY);
        *(sm + 7) = (0x1 << SM_PIN_1);
        *(sm + 10) = (0x1 << SM_PIN_2);
        udelay(SPEED_DELAY);
    }
    }
}

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

    *(sm + 1) &= ~(0x7 << (3 * 5));
    *(sm + 1) |= ~(0x1 << (3 * 5));

    *(sm + 1) &= ~(0x7 << (3 * 6));
    *(sm + 1) |= ~(0x1 << (3 * 6));

    *(sm + 1) &= ~(0x7 << (3 * 8));
    *(sm + 1) |= ~(0x1 << (3 * 8));

    *(sm + 2) &= ~(0x7 << (3 * 2));
    *(sm + 2) |= ~(0x1 << (3 * 2));

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

    copy_from_user(&mode, gdata, length);

    switch (mode)
    {
    case '1':
        run_sm(10);
        break;
    case '2':
        rev_run_sm(10);
        break;
    default:
        break;
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