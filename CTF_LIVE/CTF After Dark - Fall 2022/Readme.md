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
now using [Aperi'Solver](https://www.aperisolve.com/114591a2ac4b2a985143c43eefa874d5)
we got 
![image](https://github.com/fahimalshihab/CTF/assets/97816146/e209ab41-700c-4d61-af68-2d48a81cf712)

### camera roll
My friend sent me  this ![camera_roll](https://github.com/fahimalshihab/CTF/assets/97816146/1b655c23-042b-4f76-b955-5694c170517a)
picture he says contains his entire camera roll and told me something about putting out a fire. Can you put the fire out for me?
```
just Binwalk

┌──(iftx㉿kali)-[~/Downloads]
└─$ ls
camera_roll.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ binwalk -e camera_roll.jpg             

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, EXIF standard
12            0xC             TIFF image data, big-endian, offset of first image directory: 8
98462         0x1809E         Zip archive data, at least v2.0 to extract, compressed size: 56239, uncompressed size: 56447, name: amoung.jpg
154741        0x25C75         Zip archive data, at least v2.0 to extract, compressed size: 1450954, uncompressed size: 1451595, name: 4.zip
1605909       0x188115        End of Zip archive, footer length: 22
1605931       0x18812B        Zip archive data, at least v2.0 to extract, compressed size: 1478893, uncompressed size: 1490084, name: maz.png
3084861       0x2F123D        Zip archive data, at least v2.0 to extract, compressed size: 4173923, uncompressed size: 4180475, name: oscar.jpg
7258823       0x6EC2C7        Zip archive data, at least v2.0 to extract, compressed size: 247955, uncompressed size: 247935, name: 5.zip
7507080       0x728C88        End of Zip archive, footer length: 22
7507102       0x728C9E        Zip archive data, at least v2.0 to extract, compressed size: 970918, uncompressed size: 971255, name: fashion.jpg
8478061       0x815D6D        Zip archive data, at least v2.0 to extract, compressed size: 160689, uncompressed size: 160664, name: pain.jpg
8638788       0x83D144        Zip archive data, at least v2.0 to extract, compressed size: 87581, uncompressed size: 88276, name: bald.jpg
8726407       0x852787        Zip archive data, at least v2.0 to extract, compressed size: 131231, uncompressed size: 131862, name: banana.jpg
8858043       0x8729BB        End of Zip archive, footer length: 22

                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ cd _camera_roll.jpg.extracted 
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted]
└─$ ls
1809E.zip   4.zip  728C9E.zip  bald.jpg    fashion.jpg  oscar.jpg
18812B.zip  5.zip  amoung.jpg  banana.jpg  maz.png      pain.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted]
└─$ binwalk -e fashion.jpg    

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
72996         0x11D24         Zip archive data, at least v2.0 to extract, compressed size: 837795, uncompressed size: 864584, name: nik.jpg
910828        0xDE5EC         Zip archive data, at least v2.0 to extract, compressed size: 60186, uncompressed size: 61043, name: cigar.jpg
971233        0xED1E1         End of Zip archive, footer length: 22

                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted]
└─$ cd _fashion.jpg.extracted    
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted]
└─$ ls
11D24.zip  cigar.jpg  nik.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted]
└─$ binwalk -e nik.jpg    

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
618090        0x96E6A         JPEG image data, EXIF standard
618102        0x96E76         TIFF image data, big-endian, offset of first image directory: 8
704488        0xABFE8         JPEG image data, EXIF standard
704500        0xABFF4         TIFF image data, big-endian, offset of first image directory: 8

                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted]
└─$ ls
11D24.zip  cigar.jpg  nik.jpg
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted]
└─$ binwalk --dd=".*"  nik.jpg             

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
618090        0x96E6A         JPEG image data, EXIF standard
618102        0x96E76         TIFF image data, big-endian, offset of first image directory: 8
704488        0xABFE8         JPEG image data, EXIF standard
704500        0xABFF4         TIFF image data, big-endian, offset of first image directory: 8

                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted]
└─$ ls
11D24.zip  cigar.jpg  nik.jpg  _nik.jpg.extracted
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted]
└─$ cd _nik.jpg.extracted    
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted/_nik.jpg.extracted]
└─$ ls
96E6A  96E76  ABFE8  ABFF4
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted/_nik.jpg.extracted]
└─$ eog *           

```
/home/iftx/Downloads/_camera_roll.jpg.extracted/_fashion.jpg.extracted/_nik.jpg.extracted/
and found 

![96E6A](https://github.com/fahimalshihab/CTF/assets/97816146/3ccee204-75b0-4075-90bd-0b7549470dae)

#
# OSINT
### when it all began
Starting off with some detective work... Can you figure out when the domain for ACM Cyber's website was created? 
Answer will be of the form: flag{YYYY-MM-DD}
```
┌──(iftx㉿kali)-[~]
└─$ whois acmcyber.com
   Domain Name: ACMCYBER.COM
   Registry Domain ID: 2438728089_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.registrar.amazon.com
   Registrar URL: http://registrar.amazon.com
   Updated Date: 2023-08-26T23:34:58Z
   Creation Date: 2019-09-29T23:58:03Z
   Registry Expiry Date: 2024-09-29T23:58:03Z
   Registrar: Amazon Registrar, Inc.
   Registrar IANA ID: 468
   Registrar Abuse Contact Email: abuse@amazonaws.com
   Registrar Abuse Contact Phone: +1.2067406200
   Domain Status: ok https://icann.org/epp#ok
   Name Server: NS-1366.AWSDNS-42.ORG
   Name Server: NS-1574.AWSDNS-04.CO.UK
   Name Server: NS-310.AWSDNS-38.COM
   Name Server: NS-961.AWSDNS-56.NET
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2023-10-31T13:49:34Z <<<

For more information on Whois status codes, please visit https://icann.org/epp

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

TERMS OF USE: You are not authorized to access or query our Whois
database through the use of electronic processes that are high-volume and
automated except as reasonably necessary to register domain names or
modify existing registrations; the Data in VeriSign Global Registry
Services' ("VeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
about or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
by the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
to: (1) allow, enable, or otherwise support the transmission of mass
unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
that apply to VeriSign (or its computer systems). The compilation,
repackaging, dissemination or other use of this Data is expressly
prohibited without the prior written consent of VeriSign. You agree not to
use electronic processes that are automated and high-volume to access or
query the Whois database except as reasonably necessary to register
domain names or modify existing registrations. VeriSign reserves the right
to restrict your access to the Whois database in its sole discretion to ensure
operational stability.  VeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
reserves the right to modify these terms at any time.

The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.
Domain Name: acmcyber.com
Registry Domain ID: 2438728089_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.registrar.amazon.com
Registrar URL: https://registrar.amazon.com
Updated Date: 2023-08-26T23:34:58Z
Creation Date: 2019-09-29T23:58:03Z
Registrar Registration Expiration Date: 2024-09-29T23:58:03Z
Registrar: Amazon Registrar, Inc.
Registrar IANA ID: 468
Registrar Abuse Contact Email: abuse@amazonaws.com
Registrar Abuse Contact Phone: +1.2067406200
Domain Status: ok https://icann.org/epp#ok
Registry Registrant ID: Not Available From Registry
Registrant Name: On behalf of acmcyber.com owner
Registrant Organization: Identity Protection Service
Registrant Street: PO Box 786
Registrant City: Hayes
Registrant State/Province: Middlesex
Registrant Postal Code: UB3 9TR
Registrant Country: GB
Registrant Phone: +44.1483307527
Registrant Phone Ext:
Registrant Fax: +44.1483304031
Registrant Fax Ext:
Registrant Email: fdf20d40-4f0c-4833-bd84-7356751e882e@identity-protect.org
Registry Admin ID: Not Available From Registry
Admin Name: On behalf of acmcyber.com owner
Admin Organization: Identity Protection Service
Admin Street: PO Box 786
Admin City: Hayes
Admin State/Province: Middlesex
Admin Postal Code: UB3 9TR
Admin Country: GB
Admin Phone: +44.1483307527
Admin Phone Ext:
Admin Fax: +44.1483304031
Admin Fax Ext:
Admin Email: fdf20d40-4f0c-4833-bd84-7356751e882e@identity-protect.org
Registry Tech ID: Not Available From Registry
Tech Name: On behalf of acmcyber.com owner
Tech Organization: Identity Protection Service
Tech Street: PO Box 786
Tech City: Hayes
Tech State/Province: Middlesex
Tech Postal Code: UB3 9TR
Tech Country: GB
Tech Phone: +44.1483307527
Tech Phone Ext:
Tech Fax: +44.1483304031
Tech Fax Ext:
Tech Email: fdf20d40-4f0c-4833-bd84-7356751e882e@identity-protect.org
Name Server: NS-310.AWSDNS-38.COM
Name Server: NS-961.AWSDNS-56.NET
Name Server: NS-1366.AWSDNS-42.ORG
Name Server: NS-1574.AWSDNS-04.CO.UK
DNSSEC: unsigned
URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/
>>> Last update of WHOIS database: 2023-10-31T13:49:52Z <<<
For more information on Whois status codes, please visit https://icann.org/epp

By submitting a query to the Amazon Registrar, Inc. WHOIS database, you
agree to abide by the following terms. The data in Amazon Registrar, Inc.'s
WHOIS database is provided by Amazon Registrar, Inc. for the sole purpose of
assisting you in obtaining information about domain name accuracy. You agree
to use this data only for lawful purposes and further agree not to use this
data for any unlawful purpose or to: (1) enable, allow, or otherwise support
the transmission by email, telephone, or facsimile of commercial advertising
or unsolicited bulk email, or (2) enable high volume, automated, electronic
processes to collect or compile this data for any purpose, including mining
this data for your own personal or commercial purposes. Amazon Registrar, Inc.
reserves the right to restrict or terminate your access to the data if you fail
to abide by these terms of use. Amazon Registrar, Inc. reserves the right
to modify these terms at any time.

Visit Amazon Registrar, Inc. at https://registrar.amazon.com

Contact information available here:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-contact-support.html

© 2020, Amazon.com, Inc., or its affiliates
```
Flag : flag{2019-09-29}

### Back in my day
What was the first IP address uclaacm.com was hosted on? 
Place your answer within flag{}
so went to [ViewDns.info](https://viewdns.info/)
![image](https://github.com/fahimalshihab/CTF/assets/97816146/ae6b20ef-0b63-4ffa-a7d3-4be772a58daf)

Flag : flag{192.64.119.64}

### Bean stalking

Lima Bean is a senior at Rice University. He used to work as a Project Manager for Super Secure Systems, but recently got a job at Brick. What's his current job title?
so judt had to search in Linkedin
flag{fr0m_beans_t0_bricks}

### pokemon adventures-1
 recently have downloaded Pokemon Go and want to explore all the best gyms and PokeStops here at UCLA! However, my friend has been hiding where all of the good spots to catch Pokemon are. Can you help me find them?
My friend just posted this [photo](pokemon-1.png) of a great spot to study and take classes. The students here... seem a little different than the rest. Can you find which UCLA school is near here? (Hint: The flag is the name of the school all lower case and with underscores used as spaces. The full name is FOUR words. The answer must be wraped in flag{YOUR_ANSWER}.)

solve -> 
Had to find it in google map 
![imageedit_5_9376069411](https://github.com/fahimalshihab/CTF/assets/97816146/2eb372ae-bb38-421e-a916-31dd0342e003)

Flag : flag{anderson_school_of_management}

# Where is my supersuit
Where is my ![secretsuit](https://github.com/fahimalshihab/CTF/assets/97816146/8da197f4-5994-4ee6-80e2-d273a56d1753)
 ? (Hints for submission: Enter as flag{street_address}, all lowercase. Separate word with underscores. Use standard street abbreviations (i.e. blvd, ln, dr).)
 ```          
┌──(iftx㉿kali)-[~/Downloads]
└─$ ls
secretsuit.png
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ binwalk -e secretsuit.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1080 x 686, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, best compression
844144        0xCE170         Zip archive data, at least v2.0 to extract, compressed size: 21, uncompressed size: 21, name: nums.txt
844257        0xCE1E1         End of Zip archive, footer length: 22

                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ ls
secretsuit.png  _secretsuit.png.extracted
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads]
└─$ cd _secretsuit.png.extracted 
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_secretsuit.png.extracted]
└─$ ls
29  29.zlib  CE170.zip  nums.txt
                                                                                                     
┌──(iftx㉿kali)-[~/Downloads/_secretsuit.png.extracted]
└─$ cat nums.txt                
37.832015,-122.283661      `
```
 ![image](https://github.com/fahimalshihab/CTF/assets/97816146/5bdf69bd-68fa-4d8b-afc0-76414912a99d)
Flag : flag{1200_park_ave}


