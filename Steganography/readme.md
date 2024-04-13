# IMP
[stegsolver](stegsolver.jar) $ java -jar stegsolve.jar 
online Tools :

[Aperi'Solve](https://www.aperisolve.com/)

[Steg Online](https://stegonline.georgeom.net/upload)
 ```
exiftool <file.xyz>  | grep flag

file <file.xyz>

unrar e file.rar

steghide extract -sf <file.xyz>

foremost file.xyz

binwalk -e fule.xyz

binwalk -M --dd=".*" <file.xyz>

strings <file.xyz>

hexedit <file.xyz>

ghex <file.xyz>

unzip <file.docx>

zbarimg file.xyz

outguess -k key -r file.xyz out

pdf-parser megamind.pdf | grep flag

xxd -r ./Dumplex.txt ./flag.jpg

stegsnow -C WhiteSnow.txt
```
# Linux cmnd
To select the specific length 
```
└─$ grep -E '^.{8}$' lost_map.log
```
# ZWSP

Zero width (also zero-width) refers to a non-printing character used in computer typesetting of some complex scripts

--> copy 

Hi buddy ﻿‌​​​​​‌⁠‌‌​‌‌​‌⁠‌​​​​​⁠‌‌​​​​‌⁠‌​​​​​⁠‌​​‌​​​⁠‌‌​​​​‌⁠‌‌​​​‌‌⁠‌‌​‌​‌‌⁠‌‌​​‌​‌⁠‌‌‌​​‌​⁠‌​​​​​⁠‌​‌​‌​​⁠‌‌​‌​​​⁠‌‌​‌‌‌‌⁠‌​​​​​⁠‌‌​‌​​‌⁠‌​​​​​⁠‌‌​​​‌‌⁠‌‌​​​​‌⁠‌‌​‌‌‌​⁠‌‌‌​‌​​⁠‌​​​​​⁠‌‌​‌​​​⁠‌‌​​​​‌⁠‌‌​​​‌‌⁠‌‌​‌​‌‌⁠‌​​​​​⁠‌‌‌‌​​‌⁠‌‌​‌‌‌‌⁠‌‌‌​‌​‌⁠‌​​​​​⁠‌‌‌​‌​⁠‌​‌​​​⁠‌​​​​​⁠‌​​​​​⁠‌​‌​​‌‌⁠‌‌​‌‌‌‌⁠‌‌‌​​‌​⁠‌‌‌​​‌​⁠‌‌‌‌​​‌⁠‌​‌‌‌​⁠‌‌​‌⁠‌​‌​⁠‌‌​‌​​​⁠‌‌‌​‌​​⁠‌‌‌​‌​​⁠‌‌‌​​​​⁠‌‌‌​​‌‌⁠‌‌‌​‌​⁠‌​‌‌‌‌⁠‌​‌‌‌‌⁠‌‌​​‌‌‌⁠‌‌​‌​​‌⁠‌‌‌​‌​​⁠‌‌​‌​​​⁠‌‌‌​‌​‌⁠‌‌​​​‌​⁠‌​‌‌‌​⁠‌‌​​​‌‌⁠‌‌​‌‌‌‌⁠‌‌​‌‌​‌⁠‌​‌‌‌‌⁠‌‌​​‌‌​⁠‌‌​​​​‌⁠‌‌​‌​​​⁠‌‌​‌​​‌⁠‌‌​‌‌​‌⁠‌‌​​​​‌⁠‌‌​‌‌​​⁠‌‌‌​​‌‌⁠‌‌​‌​​​⁠‌‌​‌​​‌⁠‌‌​‌​​​⁠‌‌​​​​‌⁠‌‌​​​‌​﻿am ifty .

--> paste

<a href="https://neatnik.net/steganographr/">Here :)</a>
or 
<a href="https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder">here</a>
# keepass 
```
─$ file woof
woof: Keepass password database 2.x KDBX
└─$ keepass2john woof.kdbx >> woof.hash
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt --format=keepass woof.hash
└─$ john  woof.hash --show 
```
thn open with keepass tool

# cracking
```
stegseek file.jpg rockyou.txt
```
or
```
stegcracker file.jpg rockyou.txt    
```
example :- stegseek crack_me.jpg rockyou.txt

# zsteg 
```
zsteg -a file.png | grep flag  

```
example :- zsteg -a ch.png | grep SecVa  
# zip cracking 
```
fcrackzip -v -D -u -p rockyou.txt file.zip
```
example:- fcrackzip -v -D -u -p rockyou.txt archive.zip

#### Audio

- Fax machine audio:
    - [Example](https://devcraft.io/2018/04/08/sunshine-ctf-2018.html)
    - [Decoder](http://www.dxsoft.com/en/products/seatty/)
- SSTV (slow-scan tv) audio (moon stuff)
    - [Example](https://ctftime.org/writeup/25606)
    - [Decoder](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04)
    - [Alt Decoder](https://www.blackcatsystems.com/software/sstv.html)
    - Use these qsstv settings:
    
    ![SSTV settings](.resources/SSTV_settings.png)
    
- Spectrogram image
    - [Decoder](https://academo.org/demos/spectrum-analyzer/)
- Change pitch, speed, direction...
    - [Pitch, speed, tune](https://29a.ch/timestretch/)
    - [Reverse](https://audiotrimmer.com/online-mp3-reverser/)
- DTMF (dual tone multiple frequency) phone keys
    - `multimon-ng -a DTMF -t wav <file.wav>`
        - Keep in mind that these could me multitap letters.
            - [This](https://www.dcode.fr/multitap-abc-cipher) can decode the numbers into text
- Cassette tape
    - [Example](https://ctftime.org/writeup/25597)
    - [Decoder](https://github.com/lunderhage/c64tapedecode) (wav to **tap** files)
- Morse code
    - [Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

#### Image

- [stegsolve](https://stegonline.georgeom.net/upload)
    - Switch through bits
- [foremost](https://github.com/korczis/foremost)
    - Special tool for extracting images
    - Can be used to put together broken images (in pcap for example)
- [Depix](https://github.com/beurtschipper/Depix)
    - Unpixelate text
- Check if something was photoshopped (look at highlights)
    - [https://29a.ch/photo-forensics/#error-level-analysis](https://29a.ch/photo-forensics/#error-level-analysis)
- [zsteg](https://github.com/zed-0xff/zsteg)
    - LSB decoder
- [jsteg](https://github.com/lukechampine/jsteg)
    - jpeg steganography solver
- [pixrecovery](https://online.officerecovery.com/pixrecovery/)
    - so far the most effective png recovery tool i've found (as long as you don't care about watermarks)
    - [photopea](https://www.photopea.com/) also works very well
- [crc32fix](https://github.com/Aloxaf/crc32fix)
    - fix height and width of png based on checksum
- [PCRT](https://github.com/sherlly/PCRT)
    - fix png header and footer info
    
- [png-crc-fix](https://github.com/landaire/png-crc-fix)
    - fix png checksum
- pngcheck
    - find out if there are errors in the png
    - pngcheck <file>

#### Video

#### Machine Image

- Recovering files
    - `photorec <file.bin>`
- You can mount an image as a virtual machine
    - [https://habr.com/en/post/444940/](https://habr.com/en/post/444940/)
- Mount a `.img` file:
    - `binwalk -M --dd=".*" <fileName>`
    - run `file` on output and select the Linux filesystem file
    - `losetup /dev/loop<freeLoopNumber> <fileSystemFile>`

#### Pcap

- Extract data with tcpflow
    - `tcpflow -r <file.pcap>`
- Extract data with wireshark
    - File → Export Objects → Make selection
    

