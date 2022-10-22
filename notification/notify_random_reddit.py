import json,requests
from random import randint,choice
import os,constants

subreddit_list= constants.fav_subreddit_list # List of favorite sub reddit name

subreddit=choice(subreddit_list)

url=r"https://json.reddit.com/r/"+subreddit+r"/top/?sort=top&t=day"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data=json.loads(requests.get(url,headers=headers).text)

response_data=data["data"]
count= int(response_data["dist"])


random_post=(response_data["children"][randint(0,count)]["data"])

text=random_post["selftext"]
subreddit=random_post["subreddit"].title()

os.system('notify-send "'+subreddit+'" "'+text+'"')