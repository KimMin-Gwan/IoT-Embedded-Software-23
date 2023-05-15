#include <linux/init.h>
#include <linux/module.h>
#include <linux/interrupt.h>
#include <linux/delay.h>
#include <linux/gpio.h>

static int photoregister_pin = 0;
static int gpio_irq = 0;

static irqreturn_t interrupt_handler(int irq, void *data)
{
    int value;

    value = gpio_get_value(photoregister_pin);
    printk(KERN_INFO "Value of pin is [%d]\n", value);

    return IRQ_HANDLED;
}

static int __init photoregister_init(void)
{
    int ret;

    ret = gpio_request_one(photoregister_pin, GPIOF_IN, "LINE");
    if (ret < 0)
    {
        printk("gpio_request_error");
        return -1
    }

    ret = gpio_to_irq(photoregister_pin);
    if (ret < 0)
    {
        printk("gpio_set_error");
        return -1
    }
    else{
        gpio_irq=ret;
    }

#if 1
    ret = request_irq(gpio_irq, interrupt_handler, IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING, "photoregister", NULL);
#else
    ret = request_irq(gpio_irq, interrupt_handler, IRQF_TRIGGER_High, "photoregister", NULL);
#endif
    if (ret)
    {
        printk("failed to request IRQ");
        return -1;
    }
    return 0;
}

static void __exit photoregister_exit(void)
{
    synchronize_irq(gpio_irq);
    free_irq(gpio_irq, NULL);
    gpio_free(photoregister_pin);
}

module_init(photoregister_init);
module_exit(photoregister_exit);