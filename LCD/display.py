from LCD import I2C_LCD_driver
from time import *

def change_string(date, time):
    year = str(date['year'])
    month = str(date['month'])
    day = str(date['day'])
    hour = str(time['hour'])
    min = str(time['minute'])
    sec = str(time['second'])

    string_date = year + '년' + " " + month + "월 " + " " + day + "일"
    string_time = hour + " : " + month + " : " + day
    return string_date, string_time


def display_lcd(info, mylcd):
    raw_date = info.get_date()
    raw_time = info.get_time()

    date, time = change_string(raw_date, raw_time)

    mylcd.lcd_display_string(date,1)
    mylcd.lcd_display_string(time,2)