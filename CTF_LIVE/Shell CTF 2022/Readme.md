# Shell CTF 2022
#
# Steg
### Alien Communication - 100 points

Aliens are trying to communicate something. They belive in seeing more than what they are hearing. can you help us trying to decode what they are trying to say?

Given [Alien_voice.wav](Alien_voice.wav)

sonic visualiser 
![image](https://github.com/fahimalshihab/CTF/assets/97816146/8613fce8-7233-48ca-8890-5de33bedb372)
Flag : shell{y0u_g07_7h3_f1ag}

### Secret Document - 323 points

"shell is the key if you did'nt get it xorry"

Given: [Secret-Document](Secret-Document.dat)

CyberChef > xor(shell) > render img

![image](https://github.com/fahimalshihab/CTF/assets/97816146/8a7c9bac-f39c-4cdb-8dbe-1e87980801a4)

### Hidden File - 397 points

Our Agent gave us this image can you find whats there with this image?

Given: ![Hidden](https://github.com/fahimalshihab/CTF/assets/97816146/a9560821-3213-45cb-b565-f564dcc2b615)
```
┌──(iftx㉿kali)-[~/Downloads/h]
└─$ ls                      
Hidden.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/h]
└─$ exiftool Hidden.jpg           
ExifTool Version Number         : 12.67
File Name                       : Hidden.jpg
Directory                       : .
File Size                       : 2.1 MB
File Modification Date/Time     : 2023:11:01 22:06:51+06:00
File Access Date/Time           : 2023:11:01 23:55:50+06:00
File Inode Change Date/Time     : 2023:11:01 23:55:32+06:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : the password is shell;
Artist                          : the password is shell
XP Author                       : the password is shell
Padding                         : (Binary data 2060 bytes, use -b option to extract)
About                           : uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b
Creator                         : the password is shell
Image Width                     : 3000
Image Height                    : 4500
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 3000x4500
Megapixels                      : 13.5
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/h]
└─$ steghide extract -sf Hidden.jpg     
Enter passphrase: 
wrote extracted data to "Hidden Files.zip".
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/h]
└─$ ls
'Hidden Files.zip'   Hidden.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/h]
└─$ unzip Hidden\ Files.zip 
Archive:  Hidden Files.zip
  inflating: se3cretf1l3.pdf         
  inflating: something.jpg           
  inflating: flag.zip                
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/h]
└─$ ls
 flag.zip  'Hidden Files.zip'   Hidden.jpg   se3cretf1l3.pdf   something.jpg

```
Found  a pdf file,a flag.zip  main in this pdf file there is the key for flag.zip  but its hidden  .If we only select all thn the key txt is visibble 
[se3cretf1l3.pdf](https://github.com/fahimalshihab/CTF/files/13230262/se3cretf1l3.pdf)

Flag : shell{y0u_g07_th3_flag_N1c3!}

# Heaven - 426 points

"I was in the seventh heaven painted red green and blue"

Given: ![Seventh_Heaven_Image](https://github.com/fahimalshihab/CTF/assets/97816146/f104de41-d0d9-4f8f-aa4e-d3dc72251c21)

using [stegsolver](stegsolver.jar) $ java -jar stegsolve.jar  

![image](https://github.com/fahimalshihab/CTF/assets/97816146/e398e3a9-a1fe-4532-8c2d-52770acd602c)


Flag : SHELL{man1pul4t1ng_w1th_31ts_15_3A5y}


