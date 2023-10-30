  # QUESTCON 2023
# Misc 
### Guidelines of the Caribbean - 100
```
"Yo ho ho! Listen, sea rover so bright,

In the rule book's words, a hint takes flight.

To find the gold, follow the guide's song,

The secret's whispered, don't get it wrong."

```
![image](https://github.com/fahimalshihab/CTF/assets/97816146/ed20a48b-e9e3-4e31-b1a4-decbbf05e0a0)
#### Flag : QUESTCON{C0d3Break3r_Rul35_Expl0r3r}

### Hexa Pirate's Code - 100
Set sail on a digital adventure as you uncover the ancient Pirate's Code. The code is shrouded by Hexa, a language known to only the savviest of pirates. Can you decode the hidden message and claim your prize?
[Hexa Pirates code.zip](https://github.com/fahimalshihab/CTF/blob/main/CTF_LIVE/Questcon_CTF/Hexa_Pirates_Code.zip)
solve-->
<li>our flag was hidden there in hex format ,so i was sure the first of our flahg would be there in hex . so "QUESTCON{" in hex "5155455354434f4e7b"</li>
<li>So I grep it like this <code>grep 5155455354434f4e7b *</code></li>
<li>┌──(iftx㉿kali)-[~/Desktop/QuestCON]
└─$ grep 5155455354434f4e7b *              
cc53495bb42e4f6563b68cdbdd5e4c2a9119b498b488f53c0f281d751a368f19:    if (!String.Equals(pass, "5155455354434f4e7b426c34636b42333472645f4d616c773472335f50697234"+"7433737d-0000-0000-000000000000")) {
                                                                                             </li>
<li>I convert the text in hex and found the flag   ÌSI[´.Oec¶ÛÝ^L*´´õ<(u6þªQUESTCON{Bl4ckB34rd_Malw4r3_Pir4t3s} </li>                                   

#### Flag : QUESTCON{Bl4ckB34rd_Malw4r3_Pir4t3s}   

### Pirate's Port Paradox - 100
```
The mysterious seas of network ports.

Your flag: ((((WHOIS + QOTD) * CHARGEN) - XFER) % ECHO) * (DCE + NNTP) * NSCA

Wrap you answer with standard flag format: QUESTCON{your answer}
```
#### Solve-> These are the values of ports and then it's easy maths.

((((WHOIS + QOTD) * CHARGEN) — XFER) % ECHO) * (DCE + NNTP) * NSCA

= ((((43+17)19)-82)%7)(135+119)*5667

#### Flag: QUESTCON{1439418}

# 

# Crypto
### Riddle of the Hidden Scrolls - 100
Captain Jack Sparrow, notorious for his cunning wit and love for the sea, intercepted a letter sent by his arch-nemesis, Barbossa.

```VUUEV2QGW364QGN3YE:MN16eUGMpaE:La2:VMDty`03>```
![image](https://github.com/fahimalshihab/CTF/assets/97816146/b2fd4fe2-5c7a-4f39-a2ab-c80f8d709672)
XOR 3 -> base 64
#### Flag : QUESTCON{D34d_M3n_T3ll_No_T4l3s}

### Sparrow's Cryptographic Treasure - 100
Jack Sparrow has encrypted a secret message using RSA cryptography to protect the location of his hidden treasure.
```
N = 882564595536224140639625987659416029426239230804614613279163
E = 65537
C = 164269225538436495685306542268826436068505673594249194166792
```
simple RSA -_-
![image](https://github.com/fahimalshihab/CTF/assets/97816146/5b8e06cd-2dd9-4743-880f-b20601cd7cbf)
#### Flag : QUESTCON{1_HaT3_RS1}
#
# Forensic
### Island of Hidden Bounty - 100
```
"In a digital realm where mysteries reside,

An image conceals what you can't deride.

Navigate the web, find the clue to cite,

Unravel the flag hidden in plain sight."
```
![blackperl](https://github.com/fahimalshihab/CTF/assets/97816146/32c7d3e5-318c-424f-8611-e1c7c741af21)

```
┌──(iftx㉿kali)-[~/Downloads]
└─$ stegseek blackperl.jpg rockyou.txt       
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "password"
[i] Original filename: "hidden_treasure.txt".
[i] Extracting to "blackperl.jpg.out".
the file "blackperl.jpg.out" does already exist. overwrite ? (y/n) 
Y
[!] error: did not write to file "blackperl.jpg.out".
                                                                                                                                                                                                                                           
┌──(iftx㉿kali)-[~/Downloads]
└─$ cat blackperl.jpg.out              
https://hiddenbounty.netlify.app
```
#### link huh??? Lets try /robots.txt

User-agent: *
Disallow: /HiddenInMist.html

#### so try  /HiddenInMist.html

#### Flag : QUESTCON{X_M4rk5Th3Digit4lTr34sur3}

# Isla de Muerta's Secrets - 100
Intruders have intercepted a suspicious message from a villainous character in Jack Sparrow's crew. The message contains a hidden secret—coordinates related to Isla de Muerta's hidden treasure. Can you find the local address of intruder?

Wrap you answer with standard flag format: QUESTCON{your answer}
[intruder.pcapng.zip](https://github.com/fahimalshihab/CTF/files/13199142/intruder.pcapng.zip)
#### Wire Shark
![image](https://github.com/fahimalshihab/CTF/assets/97816146/a638cf39-5980-468d-b773-bdaa0ead88a5)

#### Flag : QUESTCON{192.168.0.129}

### Head Jack Sparrow - 110
Captain got an unknown image...Help him out and inspect the file.
![Head_Jack_Sparrow](https://github.com/fahimalshihab/CTF/assets/97816146/951668fe-2b0a-4b7a-8372-0fc85ce35c40)
```
00000000   26 ED AF 21  0D 0A 1A 0A  00 00 00 0D  76 22 E2 52  00 00 04 38  00 00 04 38  &..!........v".R...8...8
00000018   08 06 00 00  00 EC 10 6C  8F 00 00 00  09 70 48 59  73 00 00 0E  C4 00 00 0E  .......l.....pHYs.......
00000030   C4 01 95 2B  0E 1B 00 00  00 3B 74 45  58 74 43 6F  6D 6D 65 6E  74 00 78 72  ...+.....;tEXtComment.xr
00000048   3A 64 3A 44  41 46 79 50  71 78 6E 71  58 51 3A 37  2C 6A 3A 31  38 34 39 31  :d:DAFyPqxnqXQ:7,j:18491
00000060   33 34 37 34  30 31 33 35  36 38 36 33  34 34 2C 74  3A 32 33 31  30 32 35 30  34740135686344,t:2310250
00000078   37 BB 0D 91  CE 00 00 04  DE 69 54 58  74 58 4D 4C  3A 63 6F 6D  2E 61 64 6F  7........iTXtXML:com.ado
00000090   62 65 2E 78  6D 70 00 00  00 00 00 3C  78 3A 78 6D  70 6D 65 74  61 20 78 6D  be.xmp.....<x:xmpmeta xm
000000A8   6C 6E 73 3A  78 3D 27 61  64 6F 62 65  3A 6E 73 3A  6D 65 74 61  2F 27 3E 0A  lns:x='adobe:ns:meta/'>.
000000C0   20 20 20 20  20 20 20 20  3C 72 64 66  3A 52 44 46  20 78 6D 6C  6E 73 3A 72          <rdf:RDF xmlns:r
000000D8   64 66 3D 27  68 74 74 70  3A 2F 2F 77  77 77 2E 77  33 2E 6F 72  67 2F 31 39  df='http://www.w3.org/19
000000F0   39 39 2F 30  32 2F 32 32  2D 72 64 66  2D 73 79 6E  74 61 78 2D  6E 73 23 27  99/02/22-rdf-syntax-ns#'
00000108   3E 0A 0A 20  20 20 20 20  20 20 20 3C  72 64 66 3A  44 65 73 63  72 69 70 74  >..        <rdf:Descript
00000120   69 6F 6E 20  72 64 66 3A  61 62 6F 75  74 3D 27 27  0A 20 20 20  20 20 20 20  ion rdf:about=''.
00000138   20 78 6D 6C  6E 73 3A 64  63 3D 27 68  74 74 70 3A  2F 2F 70 75  72 6C 2E 6F   xmlns:dc='http://purl.o
00000150   72 67 2F 64  63 2F 65 6C  65 6D 65 6E  74 73 2F 31  2E 31 2F 27  3E 0A 20 20  rg/dc/elements/1.1/'>.
00000168   20 20 20 20  20 20 3C 64  63 3A 74 69  74 6C 65 3E  0A 20 20 20  20 20 20 20        <dc:title>.
00000180   20 3C 72 64  66 3A 41 6C  74 3E 0A 20  20 20 20 20  20 20 20 3C  72 64 66 3A   <rdf:Alt>.        <rdf:
00000198   6C 69 20 78  6D 6C 3A 6C  61 6E 67 3D  27 78 2D 64  65 66 61 75  6C 74 27 3E  li xml:lang='x-default'>
000001B0   66 6F 72 65  6E 73 69 63  73 20 63 33  20 2D 20 31  3C 2F 72 64  66 3A 6C 69  forensics c3 - 1</rdf:li
000001C8   3E 0A 20 20  20 20 20 20  20 20 3C 2F  72 64 66 3A  41 6C 74 3E  0A 20 20 20  >.        </rdf:Alt>.
000001E0   20 20 20 20  20 3C 2F 64  63 3A 74 69  74 6C 65 3E  0A 20 20 20  20 20 20 20       </dc:title>.
000001F8   20 3C 2F 72  64 66 3A 44  65 73 63 72  69 70 74 69  6F 6E 3E 0A  0A 20 20 20   </rdf:Description>..
00000210   20 20 20 20  20 3C 72 64  66 3A 44 65  73 63 72 69  70 74 69 6F  6E 20 72 64       <rdf:Description rd
00000228   66 3A 61 62  6F 75 74 3D  27 27 0A 20  20 20 20 20  20 20 20 78  6D 6C 6E 73  f:about=''.        xmlns
00000240   3A 41 74 74  72 69 62 3D  27 68 74 74  70 3A 2F 2F  6E 73 2E 61  74 74 72 69  :Attrib='http://ns.attri
00000258   62 75 74 69  6F 6E 2E 63  6F 6D 2F 61  64 73 2F 31  2E 30 2F 27  3E 0A 20 20  bution.com/ads/1.0/'>.
00000270   20 20 20 20  20 20 3C 41  74 74 72 69  62 3A 41 64  73 3E 0A 20  20 20 20 20        <Attrib:Ads>.
00000288   20 20 20 3C  72 64 66 3A  53 65 71 3E  0A 20 20 20  20 20 20 20  20 3C 72 64     <rdf:Seq>.        <rd
000002A0   66 3A 6C 69  20 72 64 66  3A 70 61 72  73 65 54 79  70 65 3D 27  52 65 73 6F  f:li rdf:parseType='Reso
000002B8   75 72 63 65  27 3E 0A 20  20 20 20 20  20 20 20 3C  41 74 74 72  69 62 3A 43  urce'>.        <Attrib:C
000002D0   72 65 61 74  65 64 3E 32  30 32 33 2D  31 30 2D 32  35 3C 2F 41  74 74 72 69  reated>2023-10-25</Attri
000002E8   62 3A 43 72  65 61 74 65  64 3E 0A 20  20 20 20 20  20 20 20 3C  41 74 74 72  b:Created>.        <Attr
00000300   69 62 3A 45  78 74 49 64  3E 64 39 64  62 32 36 35  64 2D 36 62  62 61 2D 34  ib:ExtId>d9db265d-6bba-4
---  Head_Jack_Sparrow.png       --0x0/0x164E39--0%--------------------------------------------------------------
```
Lets check the hex values using hexedit in the terminal.

We can see the hex header values are:

26 ED AF 21 0D 0A 1A 0A 00 00 00 0D 76 22 E2 52

Lets change them to png hexheader values i.e.

89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52

Now, check the png image and there will be the image of a ship

![Head_Jack_Sparrow.png](https://github.com/fahimalshihab/CTF/assets/97816146/7d2e86a2-7adc-4b49-94fc-e80415134420)
At the bottom right we see the flag.

#### Flag: QUESTCON{P1RaT3s_Ha13s_PNG_F1l3}



