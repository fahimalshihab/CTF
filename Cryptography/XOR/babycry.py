from pwn import*
from base64 import b64decode

with open('ciphertext.txt') as handle:
	
	cipher = handle.read()
	cipher = b64decode(cipher)
	
	for i in range(256):
		 txt = xor(cipher,i)
		 
		 print(txt)
