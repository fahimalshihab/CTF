## volatility



**Informations :** ```volatility -f OtterCTF.vmem imageinfo```  

**Process List :** ```volatility -f OtterCTF.vmem --profile=Win7SP1x64 pslist```

**Registry :** ```volatility -f OtterCTF.vmem --profile=Win7SP1x64 hivelist```

**Extract Password :** ```volatility -f OtterCTF.vmem --profile=Win7SP1x64 hashdump -y 0x00000000211eb010```

**Secrets :** ```volatility -f OtterCTF.vmem --profile=Win7SP1x64 lsadump```































# ...............................................................................................................
[Plugins](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)

``` volatility -f Challenge.raw imageinfo ```  
- The image info plugin displays operating system that was in use, the date and time of the sample that was collected, the number of CPUs present.
  
``` volatility -f Challenge.raw kdbgscan ```
- This plugin finds and analyses the profiles based on the Kernel debugger data block.

``` volatility -f Challenge.raw --profile=Win7SP1x86_23418 pslist ```
- To identify the presence of any rogue processes and to view any high-level running processes.

```  volatility -f Challenge.raw --profile=Win7SP1x86_23418 cmdscan```
- This plugin searches the memory dump of XP/2003/Vista/2008 and Windows 7 for commands that the attacker might have entered through a command prompt (cmd.exe).

```volatility -f Challenge.raw --profile=Win7SP1x86_23418 consoles```
- Similar to cmdscan the consoles plugin finds commands that attackers typed into cmd.exe or executed via backdoors.

  ``` volatility -f Challenge.raw --profile=Win7SP1x86_23418 envars```
- To display a process's environment variables, use the envars plugin.

```volatility -f Challenge.raw --profile=Win7SP1x86_23418 hashdump```
- To extract and decrypt cached domain credentials stored in the registry, use the hashdump command

```volatility -f MemoryDump_Lab1.raw --profile=Win7SP1x64 cmdline```
-  used to display the process command-line arguments.
## For memory dump
```volatility -f MemoryDump_Lab1.raw --profile=Win7SP1x64 memdump -p 2424 -D .```
Example ![image](https://github.com/fahimalshihab/CTF/assets/97816146/ba664d2a-5ee3-4228-92e3-87955de7e701)

### Find specific file
```volatility -f MemoryDump_Lab1.raw --profile=Win7SP1x64 filescan | grep -i important.rar```
![image](https://github.com/fahimalshihab/CTF/assets/97816146/5ded368c-35d0-4e5e-99c0-42236b575787)
### dump file from a adress
```volatility -f MemoryDump_Lab1.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000003fa3ebc0 -D .```
![image](https://github.com/fahimalshihab/CTF/assets/97816146/e13a405e-8828-473f-994b-b383e2a876f8)

```volatility -f MemoryDump_Lab2.raw --profile=Win7SP1x64 clipboard```
- For copied anything

```volatility -f MemoryDump_Lab2.raw --profile=Win7SP1x64 filescan | grep -i password```
- search anything thts is a password file
### Browser History
``` volatility --plugins=../volatility-plugins/  -f MemoryDump_Lab2.raw --profile=Win7SP1x64 chromehistory```
