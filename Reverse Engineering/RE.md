# Reverse Engineering
Reverse Engineering in a CTF is typically the process of taking a compiled (machine code, bytecode) program and converting it back into a more human readable format.

## Reverse Engineering in CTF
- In these competitions, participants are given a piece of software or a system and are asked to reverse engineer it to find hidden flags or vulnerabilities.

## Problems

Typically the goal is to get the application to reach a certain point or perform some action in order to achieve a solution.

#### Common Examples:

- Finding Triggering Inputs:
Determine the exact input that makes a program return a specific value (e.g., True).
- Uncovering Hidden Secrets:
Disassemble a game to reveal hidden easter eggs or create cheat codes for a gameplay advantage.
- Optimizing Performance:
Modify a program's code to enhance its efficiency and enable it to run to completion.

 #### Typical Process:

- File Format Identification:
  
Recognize the type of binary file provided (e.g., PE, ELF, APK, .NET, Java, Python).

- Decompilation:
  
Transform the bytecode into a more readable format like Assembly or C using appropriate decompiler tools.

- Code Analysis:
  
     Meticulously scrutinize the decompiled code, focusing on:
       - Function identification, particularly the flag function containing the solution.
       - Loop and pattern recognition to uncover code behavior insights.
       - Algorithm identification, especially cryptographic techniques.
  
- Cryptography Understanding (if applicable):
  
Grasp the specific cryptographic algorithms employed to decipher encrypted elements.

- Terminal-Based Tools (optional):
  
Utilize debuggers like pwndbg for Assembly-level debugging and code flow manipulation.
Employ other terminal-based tools for tasks such as static analysis, dynamic analysis, or memory examination.
### Tools

*Tools used for solving Reversing challenges*

- [Androguard](https://github.com/androguard/androguard) - Reverse engineer Android applications.
- [Angr](https://github.com/angr/angr) - platform-agnostic binary analysis framework.
- [Apk2Gold](https://github.com/lxdvs/apk2gold) - Yet another Android decompiler.
- [ApkTool](http://ibotpeaches.github.io/Apktool/) - Android Decompiler.
- [Barf](https://github.com/programa-stic/barf-project) - Binary Analysis and Reverse engineering Framework.
- [Binary Ninja](https://binary.ninja/) - Binary analysis framework.
- [BinUtils](http://www.gnu.org/software/binutils/binutils.html) - Collection of binary tools.
- [BinWalk](https://github.com/devttys0/binwalk) - Analyze, reverse engineer, and extract firmware images.
- [Boomerang](https://github.com/BoomerangDecompiler/boomerang) - Decompile x86/SPARC/PowerPC/ST-20 binaries to C.
- [ctf_import](https://github.com/docileninja/ctf_import) – run basic functions from stripped binaries cross platform.
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) - cwe_checker finds vulnerable patterns in binary executables.
- [demovfuscator](https://github.com/kirschju/demovfuscator) - A work-in-progress deobfuscator for movfuscated binaries.
- [Frida](https://github.com/frida/) - Dynamic Code Injection.
- [GDB](https://www.gnu.org/software/gdb/) - The GNU project debugger.
- [GEF](https://github.com/hugsy/gef) - GDB plugin.
- [Ghidra](https://ghidra-sre.org/) - Open Source suite of reverse engineering tools.  Similar to IDA Pro.
- [Hopper](http://www.hopperapp.com/) - Reverse engineering tool (disassembler) for OSX and Linux.
- [IDA Pro](https://www.hex-rays.com/products/ida/) - Most used Reversing software.
- [Jadx](https://github.com/skylot/jadx) - Decompile Android files.
- [Java Decompilers](http://www.javadecompilers.com) - An online decompiler for Java and Android APKs.
- [Krakatau](https://github.com/Storyyeller/Krakatau) - Java decompiler and disassembler.
- [Objection](https://github.com/sensepost/objection) - Runtime Mobile Exploration.
- [PEDA](https://github.com/longld/peda) - GDB plugin (only python2.7).
- [Pin](https://software.intel.com/en-us/articles/pin-a-dynamic-binary-instrumentation-tool) - A dynamic binary instrumentaion tool by Intel.
- [PINCE](https://github.com/korcankaraokcu/PINCE) - GDB front-end/reverse engineering tool, focused on game-hacking and automation.
- [PinCTF](https://github.com/ChrisTheCoolHut/PinCTF) - A tool which uses intel pin for Side Channel Analysis.
- [Plasma](https://github.com/joelpx/plasma) - An interactive disassembler for x86/ARM/MIPS which can generate indented pseudo-code with colored syntax.
- [Pwndbg](https://github.com/pwndbg/pwndbg) - A GDB plugin that provides a suite of utilities to hack around GDB easily.
- [radare2](https://github.com/radare/radare2) - A portable reversing framework.
- [Triton](https://github.com/JonathanSalwan/Triton/) - Dynamic Binary Analysis (DBA) framework.
- [Uncompyle](https://github.com/gstarnberger/uncompyle) - Decompile Python 2.7 binaries (.pyc).
- [WinDbg](http://www.windbg.org/) - Windows debugger distributed by Microsoft.
- [Xocopy](http://reverse.lostrealm.com/tools/xocopy.html) - Program that can copy executables with execute, but no read permission.
- [Z3](https://github.com/Z3Prover/z3) - A theorem prover from Microsoft Research.

*JavaScript Deobfuscators*

- [Detox](http://relentless-coding.org/projects/jsdetox/install) - A Javascript malware analysis tool.
- [Revelo](http://www.kahusecurity.com/posts/revelo_javascript_deobfuscator.html) - Analyze obfuscated Javascript code.

*SWF Analyzers*
- [RABCDAsm](https://github.com/CyberShadow/RABCDAsm) - Collection of utilities including an ActionScript 3 assembler/disassembler.
- [Swftools](http://www.swftools.org/) - Collection of utilities to work with SWF files.
- [Xxxswf](https://bitbucket.org/Alexander_Hanel/xxxswf) -  A Python script for analyzing Flash files.

### Resources
Some useful resources to start learning Reverse Engineering:

https://github.com/FULLSHADE/WindowsExploitationResources
https://www.vx-underground.org/index.html
https://pwn.college/
https://exploit.education/
https://github.com/alphaSeclab/awesome-reverse-engineering
https://www.begin.re/
https://reversewithme.blogspot.com/
https://github.com/x64dbg/x64dbg
https://github.com/NationalSecurityAgency/ghidra
https://github.com/hashcat/hashcat
https://github.com/s3inlc/hashtopolis
https://github.com/maestron/reverse-engineering-tutorials
https://www.ghidra-sre.org/
https://book.rada.re/index.html
https://github.com/radareorg/cutter
https://github.com/lennylxx/ipv6-hosts
https://www.unicorn-engine.org/
https://github.com/google/binnavi
https://github.com/JonathanSalwan/ROPgadget
http://shell-storm.org/
https://github.com/fireeye/flare-vm
https://github.com/plasma-disassembler/plasma
https://github.com/pwndbg/pwndbg
https://github.com/cea-sec/miasm
https://github.com/kaitai-io/kaitai_struct
https://github.com/alphaSeclab/awesome-reverse-engineering

http://hwreblog.com/

https://hasherezade.github.io/

https://github.com/0xZ0F

https://dasmalwerk.eu/
https://chuongdong.com/blog/

https://gist.github.com/navneetmuffin/ff678b1fda17e6188aa0462a99626121

https://legend.octopuslabs.io/sample-page.html
https://puri.sm/posts/primer-to-reverse-engineering/

https://samsclass.info/126/126_F20.shtml

http://highaltitudehacks.com/2020/09/05/arm64-reversing-and-exploitation-part-1-arm-instruction-set-heap-overflow/

https://ctf101.org/reverse-engineering/what-are-disassemblers/

https://onlinedisassembler.com/static/home/index.html

https://en.wikibooks.org/wiki/X86_Disassembly/Disassemblers_and_Decompilers

https://malwaretips.com/
https://any.run/

https://dissectingmalwa.re/
http://malc0de.com/dashboard/
http://vxvault.net/ViriList.php
https://malshare.com/

Mal Researching Room TryHackMe:
https://oldblog.cmnatic.co.uk/ : author website
https://shattered.io/
https://oldblog.cmnatic.co.uk/posts/so-you-want-to-analyse-malware/
https://any.run/
https://hybrid-analysis.com/

https://github.com/LordNoteworthy
https://github.com/wtsxDev/reverse-engineering
https://kalitut.com/
https://github.com/hasherezade/malware_training_vol1
https://www.malvuln.com/
https://dcarlin.github.io/Malware-Analysis/
https://www.sans.org/blog/-must-have-free-resources-for-malware-analysis/
https://github.com/0x4143/malware-gems
https://tsurugi-linux.org/

https://literallymalwa.re/
https://zetcode.com/gui/winapi/
https://software.intel.com/content/www/us/en/develop/articles/introduction-to-x64-assembly.html
https://sonictk.github.io/asm_tutorial/

https://www.youtube.com/channel/UC--DwaiMV-jtO-6EvmKOnqg

https://www.youtube.com/channel/UCwSxJ5kXVFPWi6fYuj6o78w

https://www.youtube.com/channel/UCqfqH-wq12WOm4QG4KiRisw

https://www.youtube.com/results?search_query=disassemblers

### Tips

- Build a strong foundation in programming languages, such as C, C++, Python, and Assembly. Understanding the underlying logic and structures will make reverse engineering tasks more manageable.
- Familiarize yourself with different file formats and their structures. Knowing the ins and outs of various formats will aid in identifying hidden data and vulnerabilities.
- Explore reverse engineering tools like Ghidra, IDA Pro, OllyDbg, and Radare2. Learn their capabilities, strengths, and weaknesses to choose the right tool for each task.
- Engage with online communities and forums dedicated to reverse engineerings, such as GitHub, Stack Overflow, and Reddit. Exchanging knowledge and experiences with fellow learners will foster growth and problem-solving skills.
