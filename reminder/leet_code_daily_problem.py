import requests
import json
import os
from datetime import datetime

LETT_CODE_URL = "https://leetcode.com/graphql/"

LEET_CODE_USER_NAME='' # Add the leetcode username

json_array={
  "query": "\n    query recentAcSubmissions($username: String!, $limit: Int!) {\n  recentAcSubmissionList(username: $username, limit: $limit) {\n    id\n    title\n    titleSlug\n    timestamp\n  }\n}\n    ",
  "variables": {
    "username": LEET_CODE_USER_NAME,
    "limit": 10
  }
}

r = requests.post(LETT_CODE_URL, json=json_array)

submissions = json.loads(r.text)

isSolvedToday=False

for submission in  submissions['data']['recentAcSubmissionList']:
  if "timestamp" in submission:
    dt_object = datetime.fromtimestamp(int(submission["timestamp"]))
    if dt_object.date() == datetime.today().date():
      isSolvedToday=True
      break 
if not isSolvedToday:
  os.system('notify-send "Solve Leet Code Problem" "You have yet to solve any leet code problem Today"')  