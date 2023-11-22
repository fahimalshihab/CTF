# Diffie–Hellman
![dh-revised](https://github.com/fahimalshihab/CTF/assets/97816146/ac0053da-176c-4763-bc3e-85760ceb70ea)


```
#Diffie–Hellman

g = 173247436685893593416376928
p = 271046059989500989696377226
gA = 182351711645430656964122520
gB = 60508729390849113619409504

for i in range(1000000000):
	if pow(g, i, p) == gA:
		a = i
		break
s1 = pow(gB, a, p)
print("a:",a)
print("s1:",s1)

```
