Reverse Engineering
An art of code analysis to analyse the inner working codes.
Note:
This challenge is quite hard for beginner. This checklist is not fully cover all things in RE and it will not applicable if you don't have the foundation to play with reverse engineering. 
Whenever you get a file, issuing file  command first to it to know what really file is it.
Use strings <filename> command to read the strings in the binary to find some clues. Maybe some grep -i command too.
You need to strong in C, Assembly Language and computer architecture for this challenge!
Most of CTF reversing require scripting if it involve with encryption etc. It may can be solve using Debugger.
Usually they gave a binary file. Weather it a...
PE File (.exe or .dll)
ELF File (elf)
APK File (apk)
.NET File (exe)
Java file
Python File (pyc or py)
PE File
Use DIE, PEID, PEBear, or PEView software to do static file analysis. Find details of file in there!
Use HxD to check the header file, file signature. Maybe the corrupt file sign one.
Find it whether it packed or not. Find online unpack.
Find it whether the binary has anti-debug or not.
Use IDA Pro software to perform static analysis on the binary.
When do analysis static or dynamic focus on strcmp, function call, conditional jump.
You can use Snowman or Ghidra software  to perform decompiler.
Use debugger like Immunity Debugger, x64Dbg/x32Dbg, or WinDbg to debug the binary.  
API monitor
Frida-trace  
ELF
Use ltrace ./<filename> command to know what library function are being called in the binary.
Use strace ./<filename> command to know what system and signal function are being called in the binary.
Use nm <filename> command to know what symbol being called in the binary.
Use readelf -a <filename>  command. It will displays information about ELF files.
Use Gdb debugger extension. Peda, pwndbg or gef will help you!.
Or you can use edb debugger.
Use IDA Pro software to perform static analysis on the binary.
APK File
Use APKTool <filename> command tools.
Use Android Emulator to run the program.
Use Android Debug Bridge.
Use dex2jar <filename> command tools.
Use jd-gui. 
JADX is good alternative to jd-gui.
Rename the file to zip file. Unzip it. Take a look the file in your favorite text editor.
.Net File
Use dnSpy software. Very powerful. You can compile the program by
Edit in the main interface -> compile -> save all. Try run the program back!
Java file
Use JADX
Python file
There are many options, one of it is uncompyle6. Just google dor python decompiler.
​ - Python EXE to pyc
Shellcode
scdbg
shellcode2exe
pdfstreamdumper shellcode analysis
debugger
IDA Pro
unicode2hex-escaped
hxd
Others
