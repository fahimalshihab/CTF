## volatility



**Informations :** 
```
volatility -f OtterCTF.vmem imageinfo
```  


**Process List :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 pslist
```


**Registry :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 hivelist
```


**Extract Password :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 hashdump -y 0x00000000211eb010
```


**Secrets :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 lsadump
```


**Computer Name :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 printkey -o 0xfffff8a000024010 -K "ControlSet001\Control\ComputerName\ComputerName"
```   
- get the offset of the registry. using hivelist 


**Network Connectiom :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 netscan
```
- get Ip Add


**Processes :**
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 pstree
```


**Grep :** 
```
strings OtterCTF.vmem| grep Lunar-3  -A 2 -B 3
```
- The -A parameter will print content of number of lines that is trailing the searched item and -B parameter will print content of number of lines that is leading searched item. 


**ClipBoard :** 
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 clipboard
```
- copy Paste

**Malware :**
```
volatility -f OtterCTF.vmem --profile=Win7SP1x64 malfind
```

**Command Line :**
```
volatility -f MemoryDump_Lab6.raw --profile=Win7SP1x64 cmdline
```

**File Scan :**
```
volatility -f MemoryDump_Lab6.raw --profile=Win7SP1x64 filescan | grep -i flag
```

**Dump Files :**
```
volatility -f MemoryDump_Lab6.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000005fcfc4b0 -D .

```

**Chromehistory :**
```
volatility -f MemoryDump_Lab6.raw --profile=Win7SP1x64 chromehistory
```




# 	Supported Plugin Commands:


<pre>
  

		amcache        	Print AmCache information
		apihooks       	Detect API hooks in process and kernel memory
		atoms          	Print session and window station atom tables
		atomscan       	Pool scanner for atom tables
		auditpol       	Prints out the Audit Policies from HKLM\SECURITY\Policy\PolAdtEv
		bigpools       	Dump the big page pools using BigPagePoolScanner
		bioskbd        	Reads the keyboard buffer from Real Mode memory
		cachedump      	Dumps cached domain hashes from memory
		callbacks      	Print system-wide notification routines
		clipboard      	Extract the contents of the windows clipboard
		cmdline        	Display process command-line arguments
		cmdscan        	Extract command history by scanning for _COMMAND_HISTORY
		consoles       	Extract command history by scanning for _CONSOLE_INFORMATION
		crashinfo      	Dump crash-dump information
		deskscan       	Poolscaner for tagDESKTOP (desktops)
		devicetree     	Show device tree
		dlldump        	Dump DLLs from a process address space
		dlllist        	Print list of loaded dlls for each process
		driverirp      	Driver IRP hook detection
		drivermodule   	Associate driver objects to kernel modules
		driverscan     	Pool scanner for driver objects
		dumpcerts      	Dump RSA private and public SSL keys
		dumpfiles      	Extract memory mapped and cached files
		dumpregistry   	Dumps registry files out to disk 
		editbox        	Displays information about Edit controls. (Listbox experimental.)
		envars         	Display process environment variables
		eventhooks     	Print details on windows event hooks
		filescan       	Pool scanner for file objects
		gahti          	Dump the USER handle type information
		gditimers      	Print installed GDI timers and callbacks
		getservicesids 	Get the names of services in the Registry and return Calculated SID
		getsids        	Print the SIDs owning each process
		handles        	Print list of open handles for each process
		hashdump       	Dumps passwords hashes (LM/NTLM) from memory
		hibinfo        	Dump hibernation file information
		hivedump       	Prints out a hive
		hivelist       	Print list of registry hives.
		hivescan       	Pool scanner for registry hives
		hpakextract    	Extract physical memory from an HPAK file
		hpakinfo       	Info on an HPAK file
		iehistory      	Reconstruct Internet Explorer cache / history
		imagecopy      	Copies a physical address space out as a raw DD image
		imageinfo      	Identify information for the image 
		impscan        	Scan for calls to imported functions
		joblinks       	Print process job link information
		kdbgscan       	Search for and dump potential KDBG values
		kpcrscan       	Search for and dump potential KPCR values
		ldrmodules     	Detect unlinked DLLs
		lsadump        	Dump (decrypted) LSA secrets from the registry
		machoinfo      	Dump Mach-O file format information
		malfind        	Find hidden and injected code
		mbrparser      	Scans for and parses potential Master Boot Records (MBRs) 
		memdump        	Dump the addressable memory for a process
		memmap         	Print the memory map
		messagehooks   	List desktop and thread window message hooks
		mftparser      	Scans for and parses potential MFT entries 
		moddump        	Dump a kernel driver to an executable file sample
		modscan        	Pool scanner for kernel modules
		modules        	Print list of loaded modules
		multiscan      	Scan for various objects at once
		mutantscan     	Pool scanner for mutex objects
		netscan        	Scan a Vista (or later) image for connections and sockets
		objtypescan    	Scan for Windows object type objects
		patcher        	Patches memory based on page scans
		poolpeek       	Configurable pool scanner plugin
		pooltracker    	Show a summary of pool tag usage
		printkey       	Print a registry key, and its subkeys and values
		privs          	Display process privileges
		procdump       	Dump a process to an executable file sample
		pslist         	Print all running processes by following the EPROCESS lists 
		psscan         	Pool scanner for process objects
		pstree         	Print process list as a tree
		psxview        	Find hidden processes with various process listings
		qemuinfo       	Dump Qemu information
		raw2dmp        	Converts a physical memory sample to a windbg crash dump
		screenshot     	Save a pseudo-screenshot based on GDI windows
		sessions       	List details on _MM_SESSION_SPACE (user logon sessions)
		shellbags      	Prints ShellBags info
		shimcache      	Parses the Application Compatibility Shim Cache registry key
		shutdowntime   	Print ShutdownTime of machine from registry
		ssdt           	Display SSDT entries
		strings        	Match physical offsets to virtual addresses (may take a while, VERY verbose)
		svcscan        	Scan for Windows services
		symlinkscan    	Pool scanner for symlink objects
		thrdscan       	Pool scanner for thread objects
		threads        	Investigate _ETHREAD and _KTHREADs
		timeliner      	Creates a timeline from various artifacts in memory 
		timers         	Print kernel timers and associated module DPCs
		truecryptmaster	Recover TrueCrypt 7.1a Master Keys
		truecryptpassphrase	TrueCrypt Cached Passphrase Finder
		truecryptsummary	TrueCrypt Summary
		unloadedmodules	Print list of unloaded modules
		userassist     	Print userassist registry keys and information
		userhandles    	Dump the USER handle tables
		vaddump        	Dumps out the vad sections to a file
		vadinfo        	Dump the VAD info
		vadtree        	Walk the VAD tree and display in tree format
		vadwalk        	Walk the VAD tree
		vboxinfo       	Dump virtualbox information
		verinfo        	Prints out the version information from PE images
		vmwareinfo     	Dump VMware VMSS/VMSN information
		volshell       	Shell in the memory image
		windows        	Print Desktop Windows (verbose details)
		wintree        	Print Z-Order Desktop Windows Tree
		wndscan        	Pool scanner for window stations
		yarascan       	Scan process or kernel memory with Yara signatures

</pre>







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
