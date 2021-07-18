import requests
import base64
import time

api = "http://alex-fan-club-api.litctf.live/api"

req_time = int(time.time())

data = {
    "time": base64.urlsafe_b64encode(req_time.to_bytes((req_time.bit_length() + 7) // 8, byteorder="big")),
    "search": "<search>yeh</search>"
}

x = requests.post(api, data=data)
print(x.text)
