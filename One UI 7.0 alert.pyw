import requests
import re
from winotify import Notification, audio
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def one_ui():
    toast = Notification(
    app_id="One UI 7 alert", 
    title="One UI 7 is here!!",
    msg="One UI 7 is here!!",
    )
    toast.add_actions(label="موفق", launch="https://doc.samsungmobile.com/SM-S928B/KSA/doc.html")
    toast.set_audio(audio.Default, loop=False)
    toast.show()


while True:
    res = requests.get("https://doc.samsungmobile.com/SM-S928B/029316240224/ara.html", allow_redirects=True, headers=headers)
    find = re.search("Android 15",res.text)
    if find:
        one_ui()
    time.sleep(300)