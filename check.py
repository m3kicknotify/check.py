import requests
import json
import os

USERNAME = "m3kick"
STATE_FILE = "last.json"

url = f"https://www.tiktok.com/@{USERNAME}"
headers = {"User-Agent": "Mozilla/5.0"}

html = requests.get(url, headers=headers).text
marker = '"videoId":"'
idx = html.find(marker)

if idx == -1:
    exit()

video_id = html[idx+len(marker):].split('"')[0]

last = None
if os.path.exists(STATE_FILE):
    last = json.load(open(STATE_FILE)).get("video")

if video_id != last:
    print("NEW VIDEO:", video_id)
    json.dump({"video": video_id}, open(STATE_FILE, "w"))
else:
    print("No change")
