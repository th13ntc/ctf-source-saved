import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify
import re


def xor_bytes(bA, bB):
    return bytes([a ^ b for a, b in zip(bA, bB)])


# Login and get cookie
url_login = 'https://cookie-stream.chal.imaginaryctf.org/backend'
obj = {
    "username": "ImaginaryCTFUser",
    "password": "idk"
}
req = requests.Session()
req.post(url=url_login, data=obj)
cookie = req.cookies["auth"]
# cookie = "1e9ab9db51d7fabcf410c9ed0a35fbfa8c5981b3c26383fc1fe49661440be237cde3a73ab5725c1f"
print(f"[+] Cookie\t: {cookie} {len(cookie)}")

# Parse cookie and find key
nonce = cookie[:16]
cipher_text_ImaginaryCTFUser = unhexlify(cookie[16:])
plain_text_ImaginaryCTFUser = pad("ImaginaryCTFUser".encode(), 16)
key = xor_bytes(cipher_text_ImaginaryCTFUser, plain_text_ImaginaryCTFUser)
print(f"[+] Plaintext\t: {hexlify(plain_text_ImaginaryCTFUser)}")
print(f"[+] Cipher\t: {hexlify(cipher_text_ImaginaryCTFUser)}")
print(f"[+] Key\t\t: {hexlify(key)}")

# Find cipher of admin
plain_text_admin = pad("admin".encode(), 16)
cipher_text_admin = xor_bytes(key, plain_text_admin)
print(f"[+] Plaintext_admin\t: {hexlify(plain_text_admin)}")
print(f"[+] Cipher_admin\t: {hexlify(cipher_text_admin)}")

# Hexify and add nonce
cookie_admin = nonce + hexlify(cipher_text_admin).decode()
print(f"[+] Cookie_admin\t: {cookie_admin} {len(cookie_admin)}")

# GET flag
url_home = "https://cookie-stream.chal.imaginaryctf.org/home"
req.cookies.set("auth", cookie_admin)
res = req.get(url=url_home)
if ("ictf{" in res.text):
    print(re.findall("ictf\{[ -z|~]+\}", res.text)[0])
    # ictf{d0nt_r3us3_k3ystr34ms_b72bfd21}
