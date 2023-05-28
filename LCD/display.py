from LCD import I2C_LCD_driver
from time import *

def change_string(date, time):
    year = str(date['year'])
    month = str(date['month'])
    day = str(date['day'])
    week = date['weekday']
    hour = str(time['hour'])
    min = str(time['minute'])
    sec = str(time['second'])

    string_date = year + "/" + month + "/" + day +"/"+ week
    string_time = hour + ":" + min + ":" + sec 
    return string_date, string_time


def display_lcd(info, mylcd):
    raw_date = info.get_date()
    raw_time = info.get_time()

    date, time = change_string(raw_date, raw_time)

    mylcd.lcd_display_string(date,1)
    mylcd.lcd_display_string(time,2)

def display_reset(mylcd):
    mylcd.lcd_display_string(" ",1)
    mylcd.lcd_display_string(" ",2)