import os
import sys

os.system('cd led')
os.system('ls')
os.system('mknod /dev/led_driver c 220 0')
os.system('insmod led_driver.ko')

os.system('cd ..')

os.system('cd step_motor')
os.system('ls')
os.system('mknod /dev/step_motor_driver c 221 0')
os.system('insmod step_motor_driver.ko')

os.system('cd ..')

os.system('cd photoregister')
os.system('ls')
os.system('mknod /dev/photoregister_driver c 222 0')
os.system('insmod photoregister_driver.ko')

os.system('cd ..')
