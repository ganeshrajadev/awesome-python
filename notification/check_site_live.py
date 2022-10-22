import requests,os,time

SITE_URL=""
SLEEP_SEC=300 #5 mins
while True:
    response=requests.get(SITE_URL)
    print(response)
    if response.status_code!=200:
          os.system('notify-send "Website Down" "'+SITE_URL+'is down"')
          break
    time.sleep(SLEEP_SEC)