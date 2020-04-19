import psutil
import I2C_LCD_driver
from time import sleep

mylcd = I2C_LCD_driver.lcd()
cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=False)
virtual_memory = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')
net_io_counters = psutil.net_io_counters(pernic=True)['eth0']
#net_io_counters = psutil.net_io_counters(pernic=True)
#print(psutil.net_if_addrs())
myip = psutil.net_if_addrs()['eth0'][0].address
mylcd.lcd_display_string(myip, 1)
display_str_cpu = \
    'CPU Usage: user {0}%, system {1}%, idle {2}% '.format(cpu_times_percent.user,
            cpu_times_percent.system,
            cpu_times_percent.idle)
display_str_mem = 'Memory Usage: {0}%, ({1}/{2}) '.format(virtual_memory.percent, int(virtual_memory.used/1000000), int(virtual_memory.total/1000000))
display_str_disk = 'Disk Usage: {0}% ({1} / {2}) '.format(disk_usage.percent, disk_usage.used, disk_usage.total)
display_str_net_sent = 'Net IO Sent: {0} MB, {1} Packets '.format(int(net_io_counters.bytes_sent / 1000000), net_io_counters.packets_sent)
display_str_net_recv = 'Net IO Rcvd: {0} MB, {1} Packets '.format(int(net_io_counters.bytes_recv / 1000000), net_io_counters.packets_recv)

display_str = display_str_cpu + display_str_mem + display_str_disk + display_str_net_sent + display_str_net_recv
str_pad = " " * 16
print(display_str)
#mylcd = I2C_LCD_driver.lcd()
#mylcd.lcd_display_string(display_str, 2)
for i in range (0, len(display_str)):
    lcd_text = display_str[i:(i+16)]
    mylcd.lcd_display_string(lcd_text,2)
    sleep(0.2)
    mylcd.lcd_display_string(str_pad,2)

# print('CPU Usage: user {0}%, system {1}%, idle {2}%, interrupt {3}%, dpc {4}%'
#     .format(cpu_times_percent.user,
#             cpu_times_percent.system,
#             cpu_times_percent.idle,
#             cpu_times_percent.interrupt,
#             cpu_times_percent.dpc))
# print('Memory Usage: {0}%, ({1}/{2})'.format(virtual_memory.percent, int(virtual_memory.used/1000000), int(virtual_memory.total/1000000)))
# print('Disk Usage: {0}% ({1} / {2})'.format(disk_usage.percent, disk_usage.used, disk_usage.total))
# print('Net IO Sent: {0} MB, {1} Packets'.format(int(net_io_counters.bytes_sent / 1000000), net_io_counters.packets_sent))
# print('Net IO Rcvd: {0} MB, {1} Packets'.format(int(net_io_counters.bytes_recv / 1000000), net_io_counters.packets_recv))

#print(psutil.cpu_times())
#print(psutil.cpu_percent(interval=1, percpu=True))
#print(psutil.cpu_count())
#print(psutil.cpu_count(logical=False))
#print(psutil.cpu_stats())
#print(psutil.cpu_freq())
#print(psutil.getloadavg())
#print(psutil.swap_memory())
#print(psutil.disk_partitions())
#print(psutil.disk_io_counters(perdisk=False))
#print(psutil.net_connections())
#print(psutil.net_if_addrs())
#print(psutil.net_if_stats())
#print(psutil.sensors_temperatures())
#print(psutil.sensors_fans())
#print(psutil.sensors_battery())
#print(psutil.users())
#print(psutil.boot_time())