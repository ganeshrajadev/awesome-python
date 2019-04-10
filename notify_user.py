import os,constants

# if you want notifcation to send at a specific time, user cron or schedule from python
# Though I prefer using Node-red for scheduleing i am not gonna use other methods here.

os.system('notify-send "'+constants.NOTIFY_TITLE+'" "'+constants.NOTIFY_MESSAGE+'"')