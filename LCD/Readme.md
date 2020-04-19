> crontab -e
and add the below entry

*/3 * * * *  /home/pi/cron/LCD.sh

then restart the cron

> sudo systemctl restart cron.service
