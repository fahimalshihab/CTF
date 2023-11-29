# baby crypto
Decode the  [ciphertext](ciphertext.txt) and find the flag

```
from pwn import*
from base64 import b64decode

with open('ciphertext.txt') as handle:
	
	cipher = handle.read()
	cipher = b64decode(cipher)
	
	for i in range(256):
		 txt = xor(cipher,i)
		 
		 print(txt)

```
$ python3 babycrypto.py | grep flag
