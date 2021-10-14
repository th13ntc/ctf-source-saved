import json
import base64
from Crypto.PublicKey import RSA


header = '{"typ":"JWT","alg":"RS256"}'

payload = '{"admin":false,"now":1632570313.6604908}'

encodedHeader = base64.b64encode(header.encode('utf-8'))
encodedPayload = base64.b64encode(payload.encode('utf-8'))


print(encodedHeader)
print(encodedPayload)

# print(base64.b64decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhZG1pbiI6ZmFsc2UsIm5vdyI6MTYzMjU3MDEzNC4zMzYxNDR9.AdXPWGVC92RbYi-hcbF98A6eg9f0MgvBCzlm2Ra7UKGl6mTjZoLZ-qjXz7g4sfmt6K5tayFvf1yAq6lQQl2FPOMe7Szln2ozrUzLPQK_57p9FROBn8mMV0sQNxe15JSktg'))
