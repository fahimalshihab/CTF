# CTF After Dark - Fall 2022

# Forensics
### get a grep
[bigfile.txt](https://github.com/fahimalshihab/CTF/files/13214519/bigfile.txt)
Solve :- 
```
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ cat bigfile.txt| grep flag    
grep: (standard input): binary file matches
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ strings bigfile.txt| grep flag
flag{incompelete
flag
asdglj flag
_flag
flag{wrong parenthese)
flag{grep_mastermind}
flag{aklsdgjnakjehgl;ewjhg;lwejahg;lasdjg;klasdjg;ljwnglj;q342ngl;jwdang;vlnasdg;
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
```
Flag : flag{grep_mastermind}

### missing person
I was zipping all my  [stuff.zip](https://github.com/fahimalshihab/CTF/files/13214688/stuff.zip)
together and realized that I'm missing a person. Could you find them for me?
```
┌──(iftx㉿kali)-[~/Downloads]
└─$ foremost stuff.zip 
Processing: stuff.zip
|foundat=whygod.jpg
��!X�Np=��]�{Є�������3�f��4�O�����]�����c�c�./#'��
foundat=stash2.jpg
*|
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ cd output 
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/output]
└─$ ls
audit.txt  jpg  zip
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/output]
└─$ cd jpg              
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/output/jpg]
└─$ ls   
00001995.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/output/jpg]
└─$ eog 00001995.jpg
```
Flag : flag{sm00th_op3rator}

### No Flags?
This individual known as [megamind.pdf](https://github.com/fahimalshihab/CTF/files/13214942/megamind.pdf)
 has gotten quite the ego, he's even taunting the very cool people in Cyber!
Show them that we do, in fact, have the inappropriate word that the popular meme mentions!
```
┌──(iftx㉿kali)-[~/Downloads]
└─$ pdf-parser megamind.pdf | grep flag
PDF Comment '%%EOFflag{no_compan1onship}\n'
```
Flag : flag{no_compan1onship}

### Tyler is the one
Tyler has an incredibly busy [schedule](https://www.youtube.com/watch?v=zMVOBu1cUro). Government agents are after him for being too alpha, disrupting the balance of alpha and beta energy of the world. He is trying to send a secret message but we can't decipher it.  ![Here](https://github.com/fahimalshihab/CTF/assets/97816146/f50a5511-9684-4ebd-843c-632ebebc4761)
is the last trace he left.
```
┌──(iftx㉿kali)-[~/Downloads]
└─$ binwalk -e alpha.jpg                   

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
246115        0x3C163         Zip archive data, at least v1.0 to extract, compressed size: 1978455, uncompressed size: 1978455, name: hidden.zip
2224616       0x21F1E8        End of Zip archive, footer length: 22
2224638       0x21F1FE        Zip archive data, at least v2.0 to extract, compressed size: 1655251, uncompressed size: 1661078, name: tyler1.png
3880117       0x3B34B5        End of Zip archive, footer length: 22

                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ ls
alpha.jpg  _alpha.jpg.extracted  rockyou.txt
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ cd _alpha.jpg.extracted 
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_alpha.jpg.extracted]
└─$ ls
21F1FE.zip  3C163.zip  hidden.zip  tyler1.png
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_alpha.jpg.extracted]
└─$ unzip hidden.zip    
Archive:  hidden.zip
[hidden.zip] secret.png password: 
   skipping: secret.png              incorrect password
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_alpha.jpg.extracted]
└─$ zsteg tyler1.png          
b1,r,msb,xy         .. file: OpenPGP Public Key
b1,b,lsb,xy         .. file: OpenPGP Secret Key
b1,rgb,lsb,xy       .. text: "r0fLM@OT1okg00dy3s"
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b4,r,lsb,xy         .. file: TeX font metric data
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map (256-256) 17 x 273 x 16 +257 +256 - 1-bit alpha "\001"                                                                                                
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_alpha.jpg.extracted]
└─$ unzip hidden.zip
Archive:  hidden.zip
[hidden.zip] secret.png password: 
  inflating: secret.png              
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_alpha.jpg.extracted]
└─$ ls
21F1FE.zip  3C163.zip  hidden.zip  secret.png  tyler1.png
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_alpha.jpg.extracted]
└─$ eog secret.png
```
now using [stegsolver](https://www.aperisolve.com/114591a2ac4b2a985143c43eefa874d5)
we got 
![image](https://github.com/fahimalshihab/CTF/assets/97816146/e209ab41-700c-4d61-af68-2d48a81cf712)
