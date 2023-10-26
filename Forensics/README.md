# Forensics
Forensics is the art of recovering the digital trail left on a computer. There are plently of methods to find data which is seemingly deleted, not stored, or worse, covertly recorded.

An important part of Forensics is having the right tools, as well as being familair with the following topics:

<pre>
File Formats
EXIF data
Wireshark & PCAPs
Disk Imaging
</pre>


# File Formats
Hex File Header and ASCII Equivalent
File headers are used to identify a file by examining the first 4 or 5 bytes of its hexadecimal content. This table is a good reference for file signatures.

<pre>
Filetype       Start             Start ASCII Translation

  ani         52 49 46 46             RIFF
  au          2E 73 6E 64             snd
  bmp         42 4D F8 A9             BM
  bmp         42 4D 62 25             BMp%
  bmp         42 4D 76 03             BMv
  cab         4D 53 43 46             MSCF
  dll         4D 5A 90 00             MZ
  Excel       D0 CF 11 E0
  exe         4D 5A 50 00             MZP (inno)
  exe         4D 5A 90 00             MZ
  flv         46 4C 56 01             FLV
  gif         47 49 46 38 39 61       GIF89a
  gif         47 49 46 38 37 61       GIF87a
  gz          1F 8B 08 08
  ico         00 00 01 00
  jpeg        FF D8 FF E1
  jpeg        FF D8 FF E0             JFIF
  jpeg        FF D8 FF FE             JFIF
  Linux bin   7F 45 4C 46             ELF
  png         89 50 4E 47             PNG
  msi         D0 CF 11 E0
  mp3         49 44 33 2E             ID3
  mp3         49 44 33 03             ID3
  OFT         4F 46 54 32             OFT2
  PPT         D0 CF 11 E0
  PDF         25 50 44 46             %PDF
  rar         52 61 72 21             Rar!
  sfw         43 57 53 06/08          cws
  tar         1F 8B 08 00
  tgz         1F 9D 90 70
  Word        D0 CF 11 E0
  wmv         30 26 B2 75
  zip         50 4B 03 04             PK
</pre>

# Metadata ->EXIF data

Metadata is data about data. Different types of files have different metadata. The metadata on a photo could include dates, camera information, GPS location, comments, etc. For music, it could include the title, author, track number and album.

Timestamps
Timestamps are data that indicate the time of certain events (MAC):

<li>Modification : when a file was modified
</li>
<li>Access : when a file or entries were read or accessed
</li>
<li>Creation : when files or entries were created
</li>


Types of timestamps

<pre>
Modified
Accessed
Created
Date Changed (MFT)
Filename Date Created (MFT)
Filename Date Modified (MFT)
Filename Date Accessed (MFT)
INDX Entry Date Created
INDX Entry Date Modified
INDX Entry Date Accessed
INDX Entry Date Changed 
</pre>
