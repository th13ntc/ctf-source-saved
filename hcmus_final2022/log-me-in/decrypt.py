import hashlib
import time

token = "9efcb42a42e253f8687acaab0fb0908b"
chars = "0123456789abcdefghijklmnopqrstuvwxyz"


start = time.time()
for i in chars:
    for j in chars:
        for k in chars:
            for l in chars:
                for m in chars:
                    for n in chars:
                        tmp = i+j+k+l+m+n
                        # tmp = "54972c"
                        hash_rs = hashlib.md5(tmp.encode()).hexdigest()
                        print(hash_rs)
                        if token == hash_rs:
                            end = time.time()
                            print(end - start)
                            print("Result:", tmp, "-", hash_rs)
                            exit()
end = time.time()
print(end - start)
print("No Result")
