import requests
import base64
import time

api = "http://alex-fan-club-api.litctf.live/api"

req_time = int(4117693555152280233235140304313160393372574785286687169479929583036435327748269177565382885337)

data = {
    "time": base64.urlsafe_b64encode(req_time.to_bytes((req_time.bit_length() + 7) // 8, byteorder="big")),
    "search": "<search>yeh</search>"
}

x = requests.post(api, data=data)
print(x.text)
