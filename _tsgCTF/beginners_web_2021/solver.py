from threading import Thread
import threading
import requests


def setHash():
    res = requests.get('http://34.84.69.72:59101/?action=SetSalt&data=flag')
    print(res.text)


def getHash():
    res = requests.get('http://34.84.69.72:59101/?action=GetSalt')
    print(res.text)


try:
    t1 = threading.Thread(target=setHash)
    t2 = threading.Thread(target=getHash)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except:
    print('error')
