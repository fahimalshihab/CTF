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

```sh
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
```

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

# PCAP Analysis

<h3>Approaching these problems</h3>

You can think of PCAP analysis challenges as finding a needle in a haystack. You should always be looking for anomalies and what doesn't belong. This could be one of many things:
<li>A file transfer
</li>
<li>A password passed in the clear (i.e., not encrypted)
</li>
<li>Traffic that doesn't fit in (such as a few IPv6 packets in a PCAP comprised mostly of IPv4)
</li>
<li>Anything that looks out of the ordinary is probably worth exploring.
</li>

<h3>Avoiding PCAP tools altogether</h3>

You don't always have to examine a capture file in detail during on of these challenges. Most problems won't be this easy, but sometimes you can find a flag (or related information) by running something like:

<code>strings capture.pcap | grep -i flag</code>

If you just want to try to extract any files within the PCAP, binwalk (installed by default on Kali) might prove fruitful:

<code>binwalk -e capture.pcap</code>

<h3>Wireshark
</h3>
Wireshark is a useful graphical tool for displaying traffic, captured either in real-time or from a PCAP file. It has a lot of great tools that can't be easily replicated in command-line applications, such as following streams of traffic.

<h3>Scoping out a PCAP</h3>
<li>You first step should be to look at the protocol hierarchy analysis, which can be done by selecting Statistics -> Protocol Hierarchy from the toolbar menu. This will show you a distribution of the different protocols present within the PCAP.</li>

<li>Following our goal of finding the needle in the hay stack, this is a great way to identify some low-frequency protocols for examination. For example, if you have a PCAP full of HTTPS traffic, but see a few packets of FTP data, you should probably start by looking at the FTP data.</li>

<li>To start looking at a specific category of traffic identified in the protocol hierarchy, richt click the desired category and click <code>Apply as Filter -> Selected</code>. You can also exclude other traffic that isn't super interesting at first glance (like ARP) via the<code> Apply as Filter -> Not Selected </code> option.</li>

<h3>Quick wins</h3>
Sometimes you do not need to do much work to find a flag, and can take some shortcuts to save time.

<li>Occasionally, a PCAP challenge is only meant to involve pulling out a transferred file (via a protocol like HTTP or SMB) from the PCAP and doing some further analysis on that file. Files transferred via HTTP can be extracted from a PCAP in Wireshark via the <code>File -> Export Objects -> HTTP </code>option. The same can be done for SMB-transferred files via the <code>File -> Export Objects -> SMB</code>option. Note that this technique is not a 100% surefire method of extracting every file, as some files may have been transferred in non-standard ways that Wireshark is not innately privy to.
</li>
<li>We can also just try searching different raw traffic for flag-related text. For example, we can search for the string flag in all TCP traffic with the following filter:

<code>frame contains flag</code>
It's also probably worthwhile to search for the start of the known flag format in its ASCII- and base64-encoded forms, too.</li>

<li>Sometimes, there might be extra information stored via Wireshark's commenting feature. To filter on packets that have comments, use the filter:

<code>pkt_comment</code>
</li>

### Decrypting SSL/TLS traffic

If you are in possession of the private key of a server from which you are examining recorded traffic, you can decrypt SSL/TLS-encrypted traffic from within Wireshark. You can configure this key by filling in the appropriate information in the `Edit -> Preferences -> RSA Keys -> Add new keyfile...` dialog.

### Modifying displayed columns

Wireshark allows you to customize what columns are displayed for matching packets. These can be edited in the `Edit -> Preferences -> Columns`. It may be helpful to add the following columns to your output:

* Source port
* Destination port
* Hostname
* Hex representation of transferred data

### Useful filters

There is a lot of traffic that is considered "ordinary" (i.e., you would see a lot of it in a PCAP on your computer outside of a CTF, too). A good way to filter it out is with something like:

```
not arp and not http and not (udp.port == 53)
```

Alternatively, if you want to keep the http traffic around, you can try (note that this will also exclude DNS over TCP, which you probably want to look at):

```
!(arp or icmp or dns or stp)
```

However, don't discount these classes of traffic just because they align with typical computer usage. DNS, HTTP, and even ARP can easily be an integral part of a PCAP analysis challenge.

Another useful thing to look at when doing something like examining malware is identify failed DNS requests, which involve some kind of C2 domain. This can be done with:

```
dns.flags.rcode != 0
```

To limit the displayed traffic to just what is occurring between two specific hosts, you can use:

```
ip.addr == 1.1.1.1 && ip.addr == 2.2.2.2
```

Abnormal TCP parameters can also be something worth looking into. Some of the below might be a good starting point:

* TCP resets - `tcp.flags.reset == 1`
* TCP pushes - `tcp.flags.push == 1`
* TCP SYN/ACKs - `tcp.flags == 0x012`
* Retransmissions / duplicate ACKs / zero windows - `tcp.analysis.flags && !tcp.analysis.window_update`

## `tshark`

You can think of `tshark` as the command-line version of the Wireshark program. While you won't be getting a nice graphical output of your captured traffic with `tshark`, you will be able to get more creative with how your data is presented and then pass it off to other command-line programs.

### Installation

`tshark` should already be on your system if you already have Wireshark installed.

### Useful options to know

There are a few commonly-used options we will use in the below examples that you should be acquainted with. These are:

* `-r` - TODO
* `-q` - don't continuously display the count of packets, just show it at the very end
* `-R` - TODO
* `-z` - TODO
* `-i` - TODO
* `-f` - TODO

### Useful output formats

Just like in Wireshark, we can print a concise layout of the different protocols present in our capture file. Do so with:
```sh
TODO
```

### Following streams

TODO

### Decrypting SSL/TLS traffic

See: https://minnmyatsoe.com/2016/01/26/using-tshark-to-decrypt-ssl-tls-packets/

Similar to Wireshark, `tshark` supports decrypting SSL/TLS traffic as long as we have the private key used on the server-under-analysis. We can do this with:

```sh
tshark -r encrypted_capture.pcap -V -x \
    -o 'ssl.debug_file:ssldebug.log' \
    -o 'ssl.desegment_ssl_records: TRUE' \
    -o 'ssl.desegment_ssl_appliction_data: TRUE' \
    -o 'ssl.keys_list:127.0.0.1,443,http,/path/to/server.pem'
    # last option is in the format server,port,protocol,private_key_location
```

We can also use our knowledge of following streams in `tshark` to follow stream `1` and print its contents as ASCII:

```sh
tshark -r encrypted_capture.pcap -q \
    -o 'ssl_keys_list:127.0.0.1,443,http,/path/to/server.pem' \
    -z 'follow,ssl,ascii,1'
```

### IP filtering

TODO

### Extracting files from captures

Just like in Wireshark, we can extract files from PCAPs. This can be done for HTTP and SMB with:
```sh
tshark -nr capture.pcap --export-objects smb,./
```

### Examining HTTP traffic metadata

A first good step when examining HTTP data is to print out a tree of all of the HTTP traffic within the specified capture file. This can be done with:

```sh
tshark -r capture.pcap -q -z http,tree
```

We also probably want to output some of the specific fields. Be on the lookout for odd HTTP headers, as this is an exfiltration method you might see in CTFs sometimes. It might be worth piping the below command to `sort | uniq -c | sort -n` in order to spot any anomalies right away.

```sh
tshark -r capture.pcap -Y http.request -T fields -e http.host -e http.user_agent
```

Looking for specific types of HTTP requests can be done with:

```sh
TODO
```

Some additional HTTP fields that might be worth examining can be found in the following command:

```sh
TODO
```

### DNS analysis

TODO

### Database traffic analysis

TODO

## Scapy

[Scapy](https://scapy.readthedocs.io/en/latest/) is a project that lets you read and manipulate network packets in Python.

### Extracting Data from Packets

It offers more fine-grained control for data manipulation than Wireshark or `tshark`. Here is an example of dumping UDP data from a PCAP:

```python
#!/usr/bin/env python

from scapy.all import *

packets = rdpcap("the.pcap")

with open("out.raw", "wb") as f:
    for p in packets:
        if UDP in p:
            chunk = bytes(p[Raw])
            f.write(chunk)
```
