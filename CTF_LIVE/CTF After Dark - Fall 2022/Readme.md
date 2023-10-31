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

