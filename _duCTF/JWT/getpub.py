from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, urlsafe_b64decode
from gmpy2 import gcd, mpz
import requests

url = 'https://web-jwt-b9766b1f.chal-2021.duc.tf/'
jwt0 = requests.get(f'{url}get_token').text
jwt1 = requests.get(f'{url}/get_token').text
target_bit_length = 2048
jwt_list = [
    jwt0,
    jwt1
]


def b64urldecode(b64: str) -> str:
    return urlsafe_b64decode(b64+("=" * (len(b64) % 4)))


def parse(jwt: str) -> (bytes, bytes):
    tokens = jwt.split(".")
    return ".".join(tokens[0:2]), b64urldecode(tokens[2])


def get_rsa_mc(jwt: str) -> int:
    inp, sig = parse(jwt)
    h = SHA256.new(inp.encode())
    m = bytes_to_long(
        PKCS1_v1_5.pkcs1_15._EMSA_PKCS1_V1_5_ENCODE(h, target_bit_length // 8)
    )
    c = bytes_to_long(sig)
    return mpz(m), mpz(c)


def get_pubkey(n: int, e: int) -> str:
    k = RSA.construct([n, e])
    return k.export_key("PEM")


ms = []
cs = []
for jwt in jwt_list:
    m, c = get_rsa_mc(jwt)
    ms.append(m)
    cs.append(c)

assert len(ms) > 0 and len(cs) == len(ms)

e = 65537
n = pow(cs[0], e) - ms[0]
for i in range(1, len(ms)):
    m = ms[i]
    c = cs[i]
    n = gcd(n, pow(c, e) - m)

for i in range(2, 1000):
    while n % i == 0:
        n //= i
n = int(n)

print(n)
print(get_pubkey(n, e))
