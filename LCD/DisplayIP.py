import I2C_LCD_driver
from time import *
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_addr = s.getsockname()[0]
    s.close()
    return ip_addr

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)