import os
import sys

os.system('mknod /dev/led_driver c 220 0')
os.system('insmod ./led/led_driver.ko')

os.system('mknod /dev/step_motor_driver c 221 0')
os.system('insmod ./step_motor/step_motor_driver.ko')

os.system('mknod /dev/photoregister_driver c 222 0')
os.system('insmod ./photoregister/photoregister_driver.ko')

