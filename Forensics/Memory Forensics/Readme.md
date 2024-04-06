## volatility

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
