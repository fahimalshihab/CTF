# Misc 
### Guidelines of the Caribbean - 100
```
"Yo ho ho! Listen, sea rover so bright,

In the rule book's words, a hint takes flight.

To find the gold, follow the guide's song,

The secret's whispered, don't get it wrong."

```
![image](https://github.com/fahimalshihab/CTF/assets/97816146/ed20a48b-e9e3-4e31-b1a4-decbbf05e0a0)
Flag -> QUESTCON{C0d3Break3r_Rul35_Expl0r3r}

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
<li>I convert the text in hex and found the flag   ÌSI[´.Oec¶ÛÝ^L*´´õ<(u6þªQUESTCON{Bl4ckB34rd_Malw4r3_Pir4t3s} </li>                                 Flag -> QUESTCON{Bl4ckB34rd_Malw4r3_Pir4t3s}     



### Pirate's Port Paradox - 100
```
The mysterious seas of network ports.

Your flag: ((((WHOIS + QOTD) * CHARGEN) - XFER) % ECHO) * (DCE + NNTP) * NSCA

Wrap you answer with standard flag format: QUESTCON{your answer}

Solve->

((((WHOIS + QOTD) * CHARGEN) — XFER) % ECHO) * (DCE + NNTP) * NSCA

= ((((43+17)19)-82)%7)(135+119)*5667

flag: QUESTCON{1439418}
```
