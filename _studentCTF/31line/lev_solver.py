import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_#'
url = 'https://cat-step.disasm.me/'


# for c in chars:
#     data = {
#         "flag": flag+c
#     }
#     res = requests.post(url=url, data=data)
#     data = res.json()
# RESULT: "05abcefginstuwyzAFGOS_"

dis = 26
ok = '05abcefginstuwyzAFGOS_'
flag = 'spbctf{e'
while (dis != 0):
    maxLen = -1
    maxStr = ''
    nextChr = ''
    for o in ok:
        tmpF = flag+o
        tmpO = ''
        for c in ok:
            data = {
                "flag": tmpF+c
            }
            res = requests.post(url=url, data=data)
            if f"{dis}" in res.text:
                tmpO = tmpO+c
        if len(tmpO) > maxLen:
            maxLen = len(tmpO)
            maxStr = tmpO
            nextChr = o
            print(nextChr, maxStr, maxLen)
    flag = flag+nextChr
    ok = maxStr
    dis = dis - 1
    print("===================")
    print("Result:", flag, dis, ok)
    print("===================")
