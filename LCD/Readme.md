sudo nano /etc/rc.local

and add below just before exit 0

sleep 10
/usr/bin/python3 /home/pi/git/RaspberryIIOT/LCD/DisplayIP.py