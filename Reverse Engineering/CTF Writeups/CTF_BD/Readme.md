<pre>
iftx@iftx-Modern-15-A5M:~/Desktop/RE/rev$ <b>gdb ./CTF_BD </b>

GNU gdb (Ubuntu 12.1-0ubuntu1~22.04) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 157 pwndbg commands and 45 shell commands. Type pwndbg [--shell | --all] [filter] for a list.
pwndbg: created $rebase, $base, $ida GDB functions (can be used with print/break)
Reading symbols from ./CTF_BD...
(No debugging symbols found in ./CTF_BD)
------- tip of the day (disable with set show-tips off) -------
Use hi to see if a an address belongs to a glibc heap chunk
pwndbg> <b>info functions </b> 
All defined functions:

Non-debugging symbols:
0x00000000000005b8  _init
0x00000000000005e0  puts@plt
0x00000000000005f0  strlen@plt
0x0000000000000600  __stack_chk_fail@plt
0x0000000000000610  printf@plt
0x0000000000000620  __cxa_finalize@plt
0x0000000000000630  _start
0x0000000000000660  deregister_tm_clones
0x00000000000006a0  register_tm_clones
0x00000000000006f0  __do_global_dtors_aux
0x0000000000000730  frame_dummy
0x000000000000073a  isitreal
0x000000000000086b  main
0x00000000000008a0  __libc_csu_init
0x0000000000000910  __libc_csu_fini
0x0000000000000914  _fini
pwndbg> <b>disassemble main</b> 
Dump of assembler code for function main:
   0x000000000000086b <+0>:	push   rbp
   0x000000000000086c <+1>:	mov    rbp,rsp
   0x000000000000086f <+4>:	sub    rsp,0x10
   0x0000000000000873 <+8>:	mov    DWORD PTR [rbp-0x8],0x0
   0x000000000000087a <+15>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000000881 <+22>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000000884 <+25>:	mov    edi,eax
  <b> 0x0000000000000886 <+27>:	call   0x73a isitreal  </b>
   0x000000000000088b <+32>:	mov    eax,0x0
   0x0000000000000890 <+37>:	leave  
   0x0000000000000891 <+38>:	ret    
End of assembler dump.
pwndbg> <b>disassemble isitreal </b> 
Dump of assembler code for function isitreal:
   0x000000000000073a <+0>:	push   rbp
   0x000000000000073b <+1>:	mov    rbp,rsp
   0x000000000000073e <+4>:	push   rbx
   0x000000000000073f <+5>:	sub    rsp,0x78
   0x0000000000000743 <+9>:	mov    DWORD PTR [rbp-0x74],edi
   0x0000000000000746 <+12>:	mov    rax,QWORD PTR fs:0x28
   0x000000000000074f <+21>:	mov    QWORD PTR [rbp-0x18],rax
   0x0000000000000753 <+25>:	xor    eax,eax
   0x0000000000000755 <+27>:	mov    DWORD PTR [rbp-0x68],0x0
   0x000000000000075c <+34>:	mov    DWORD PTR [rbp-0x64],0x61
   0x0000000000000763 <+41>:	movabs rax,0x5960624d64565d5d
   0x000000000000076d <+51>:	movabs rdx,0x742f564e72707a43
   0x0000000000000777 <+61>:	mov    QWORD PTR [rbp-0x60],rax
   0x000000000000077b <+65>:	mov    QWORD PTR [rbp-0x58],rdx
   0x000000000000077f <+69>:	movabs rax,0x4d42784e5c507847
   0x0000000000000789 <+79>:	movabs rdx,0x534d70515a4d705f
   0x0000000000000793 <+89>:	mov    QWORD PTR [rbp-0x50],rax
   0x0000000000000797 <+93>:	mov    QWORD PTR [rbp-0x48],rdx
   0x000000000000079b <+97>:	movabs rax,0x5d235d655d5a475f
   0x00000000000007a5 <+107>:	movabs rdx,0x2571242462515f7a
   0x00000000000007af <+117>:	mov    QWORD PTR [rbp-0x40],rax
   0x00000000000007b3 <+121>:	mov    QWORD PTR [rbp-0x38],rdx
   0x00000000000007b7 <+125>:	movabs rax,0x727e21594e556d44
   0x00000000000007c1 <+135>:	mov    QWORD PTR [rbp-0x30],rax
   0x00000000000007c5 <+139>:	mov    DWORD PTR [rbp-0x28],0x46635170
   0x00000000000007cc <+146>:	mov    BYTE PTR [rbp-0x24],0x0
   <b>0x00000000000007d0 <+150>:	cmp    DWORD PTR [rbp-0x74],0x1</b>
   0x00000000000007d4 <+154>:	jne    0x844 <isitreal+266>
   <b>0x00000000000007d6 <+156>:	mov    DWORD PTR [rbp-0x68],0x0</b>
   0x00000000000007dd <+163>:	jmp    0x7fb <isitreal+193>
   0x00000000000007df <+165>:	mov    eax,DWORD PTR [rbp-0x68]
   0x00000000000007e2 <+168>:	cdqe   
   0x00000000000007e4 <+170>:	movzx  eax,BYTE PTR [rbp+rax*1-0x60]
   0x00000000000007e9 <+175>:	xor    eax,0x17
   0x00000000000007ec <+178>:	mov    edx,eax
   0x00000000000007ee <+180>:	mov    eax,DWORD PTR [rbp-0x68]
   0x00000000000007f1 <+183>:	cdqe   
   0x00000000000007f3 <+185>:	mov    BYTE PTR [rbp+rax*1-0x60],dl
   0x00000000000007f7 <+189>:	add    DWORD PTR [rbp-0x68],0x1
   0x00000000000007fb <+193>:	mov    eax,DWORD PTR [rbp-0x68]
   0x00000000000007fe <+196>:	movsxd rbx,eax
   0x0000000000000801 <+199>:	lea    rax,[rbp-0x60]
   0x0000000000000805 <+203>:	mov    rdi,rax
   0x0000000000000808 <+206>:	call   0x5f0 <strlen@plt>
   0x000000000000080d <+211>:	cmp    rbx,rax
   0x0000000000000810 <+214>:	jb     0x7df <isitreal+165>
   0x0000000000000812 <+216>:	lea    rdi,[rip+0x10f]        # 0x928
   0x0000000000000819 <+223>:	call   0x5e0 <puts@plt>
   0x000000000000081e <+228>:	lea    rax,[rbp-0x60]
   0x0000000000000822 <+232>:	mov    rsi,rax
   0x0000000000000825 <+235>:	lea    rdi,[rip+0x125]        # 0x951
   0x000000000000082c <+242>:	mov    eax,0x0
   0x0000000000000831 <+247>:	call   0x610 <printf@plt>
   0x0000000000000836 <+252>:	lea    rdi,[rip+0x120]        # 0x95d
   0x000000000000083d <+259>:	call   0x5e0 <puts@plt>
   0x0000000000000842 <+264>:	jmp    0x850 <isitreal+278>
   0x0000000000000844 <+266>:	lea    rdi,[rip+0x12d]        # 0x978
   0x000000000000084b <+273>:	call   0x5e0 <puts@plt>
   0x0000000000000850 <+278>:	mov    rax,QWORD PTR [rbp-0x18]
   0x0000000000000854 <+282>:	xor    rax,QWORD PTR fs:0x28
   0x000000000000085d <+291>:	je     0x864 <isitreal+298>
   0x000000000000085f <+293>:	call   0x600 <__stack_chk_fail@plt>
   0x0000000000000864 <+298>:	add    rsp,0x78
   0x0000000000000868 <+302>:	pop    rbx
   0x0000000000000869 <+303>:	pop    rbp
   0x000000000000086a <+304>:	ret    
End of assembler dump.
pwndbg><b> r</b>
Starting program: /home/iftx/Desktop/RE/rev/CTF_BD 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Sorry!!! You are not admin
[Inferior 1 (process 21938) exited normally]
pwndbg> <b>disassemble isitreal </b>
Dump of assembler code for function isitreal:
   0x000055555540073a <+0>:	push   rbp
   0x000055555540073b <+1>:	mov    rbp,rsp
   0x000055555540073e <+4>:	push   rbx
   0x000055555540073f <+5>:	sub    rsp,0x78
   0x0000555555400743 <+9>:	mov    DWORD PTR [rbp-0x74],edi
   0x0000555555400746 <+12>:	mov    rax,QWORD PTR fs:0x28
   0x000055555540074f <+21>:	mov    QWORD PTR [rbp-0x18],rax
   0x0000555555400753 <+25>:	xor    eax,eax
   0x0000555555400755 <+27>:	mov    DWORD PTR [rbp-0x68],0x0
   0x000055555540075c <+34>:	mov    DWORD PTR [rbp-0x64],0x61
   0x0000555555400763 <+41>:	movabs rax,0x5960624d64565d5d
   0x000055555540076d <+51>:	movabs rdx,0x742f564e72707a43
   0x0000555555400777 <+61>:	mov    QWORD PTR [rbp-0x60],rax
   0x000055555540077b <+65>:	mov    QWORD PTR [rbp-0x58],rdx
   0x000055555540077f <+69>:	movabs rax,0x4d42784e5c507847
   0x0000555555400789 <+79>:	movabs rdx,0x534d70515a4d705f
   0x0000555555400793 <+89>:	mov    QWORD PTR [rbp-0x50],rax
   0x0000555555400797 <+93>:	mov    QWORD PTR [rbp-0x48],rdx
   0x000055555540079b <+97>:	movabs rax,0x5d235d655d5a475f
   0x00005555554007a5 <+107>:	movabs rdx,0x2571242462515f7a
   0x00005555554007af <+117>:	mov    QWORD PTR [rbp-0x40],rax
   0x00005555554007b3 <+121>:	mov    QWORD PTR [rbp-0x38],rdx
   0x00005555554007b7 <+125>:	movabs rax,0x727e21594e556d44
   0x00005555554007c1 <+135>:	mov    QWORD PTR [rbp-0x30],rax
   0x00005555554007c5 <+139>:	mov    DWORD PTR [rbp-0x28],0x46635170
   0x00005555554007cc <+146>:	mov    BYTE PTR [rbp-0x24],0x0
  <b>0x00005555554007d0 <+150>:	cmp    DWORD PTR [rbp-0x74],0x1</b>
   0x00005555554007d4 <+154>:	jne    0x555555400844 <isitreal+266>
  <b>0x00005555554007d6 <+156>:	mov    DWORD PTR [rbp-0x68],0x0</b>
   0x00005555554007dd <+163>:	jmp    0x5555554007fb <isitreal+193>
   0x00005555554007df <+165>:	mov    eax,DWORD PTR [rbp-0x68]
   0x00005555554007e2 <+168>:	cdqe   
   0x00005555554007e4 <+170>:	movzx  eax,BYTE PTR [rbp+rax*1-0x60]
   0x00005555554007e9 <+175>:	xor    eax,0x17
   0x00005555554007ec <+178>:	mov    edx,eax
   0x00005555554007ee <+180>:	mov    eax,DWORD PTR [rbp-0x68]
   0x00005555554007f1 <+183>:	cdqe   
   0x00005555554007f3 <+185>:	mov    BYTE PTR [rbp+rax*1-0x60],dl
   0x00005555554007f7 <+189>:	add    DWORD PTR [rbp-0x68],0x1
   0x00005555554007fb <+193>:	mov    eax,DWORD PTR [rbp-0x68]
   0x00005555554007fe <+196>:	movsxd rbx,eax
   0x0000555555400801 <+199>:	lea    rax,[rbp-0x60]
   0x0000555555400805 <+203>:	mov    rdi,rax
   0x0000555555400808 <+206>:	call   0x5555554005f0 <strlen@plt>
   0x000055555540080d <+211>:	cmp    rbx,rax
   0x0000555555400810 <+214>:	jb     0x5555554007df <isitreal+165>
   0x0000555555400812 <+216>:	lea    rdi,[rip+0x10f]        # 0x555555400928
   0x0000555555400819 <+223>:	call   0x5555554005e0 <puts@plt>
   0x000055555540081e <+228>:	lea    rax,[rbp-0x60]
   0x0000555555400822 <+232>:	mov    rsi,rax
   0x0000555555400825 <+235>:	lea    rdi,[rip+0x125]        # 0x555555400951
   0x000055555540082c <+242>:	mov    eax,0x0
   0x0000555555400831 <+247>:	call   0x555555400610 <printf@plt>
   0x0000555555400836 <+252>:	lea    rdi,[rip+0x120]        # 0x55555540095d
   0x000055555540083d <+259>:	call   0x5555554005e0 <puts@plt>
   0x0000555555400842 <+264>:	jmp    0x555555400850 <isitreal+278>
   0x0000555555400844 <+266>:	lea    rdi,[rip+0x12d]        # 0x555555400978
   0x000055555540084b <+273>:	call   0x5555554005e0 <puts@plt>
   0x0000555555400850 <+278>:	mov    rax,QWORD PTR [rbp-0x18]
   0x0000555555400854 <+282>:	xor    rax,QWORD PTR fs:0x28
   0x000055555540085d <+291>:	je     0x555555400864 <isitreal+298>
   0x000055555540085f <+293>:	call   0x555555400600 <__stack_chk_fail@plt>
   0x0000555555400864 <+298>:	add    rsp,0x78
   0x0000555555400868 <+302>:	pop    rbx
   0x0000555555400869 <+303>:	pop    rbp
   0x000055555540086a <+304>:	ret    
End of assembler dump.
pwndbg><b> b *0x00005555554007d0</b>
Breakpoint 1 at 0x5555554007d0
pwndbg><b> r</b>
Starting program: /home/iftx/Desktop/RE/rev/CTF_BD 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00005555554007d0 in isitreal ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
──────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]──────────────────────────────────
*RAX  0x727e21594e556d44 ('DmUNY!~r')
 RBX  0
*RCX  0x5555554008a0 (__libc_csu_init) ◂— push r15
*RDX  0x2571242462515f7a ('z_Qb$$q%')
 RDI  0
*RSI  0x7fffffffdde8 —▸ 0x7fffffffe193 ◂— '/home/iftx/Desktop/RE/rev/CTF_BD'
*R8   0x7ffff7e1bf10 (initial+16) ◂— 4
*R9   0x7ffff7fc9040 (_dl_fini) ◂— endbr64 
*R10  0x7ffff7fc3908 ◂— 0xd00120000000e
*R11  0x7ffff7fde660 (_dl_audit_preinit) ◂— endbr64 
*R12  0x7fffffffdde8 —▸ 0x7fffffffe193 ◂— '/home/iftx/Desktop/RE/rev/CTF_BD'
*R13  0x55555540086b (main) ◂— push rbp
 R14  0
*R15  0x7ffff7ffd040 (_rtld_global) —▸ 0x7ffff7ffe2e0 —▸ 0x555555400000 ◂— jg 0x555555400047
*RBP  0x7fffffffdcb0 —▸ 0x7fffffffdcd0 ◂— 1
*RSP  0x7fffffffdc30 ◂— 0
*RIP  0x5555554007d0 (isitreal+150) ◂— cmp dword ptr [rbp - 0x74], 1
───────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]───────────────────────────────────────────
 ► 0x5555554007d0 <isitreal+150>    cmp    dword ptr [rbp - 0x74], 1     0 - 1     EFLAGS => 0x297 [ CF PF AF zf SF IF df of ]
   0x5555554007d4 <isitreal+154>  ✔ jne    isitreal+266                <isitreal+266>
    ↓
   0x555555400844 <isitreal+266>    lea    rdi, [rip + 0x12d]            RDI => 0x555555400978 ◂— push rbx /* 'Sorry!!! You are not admin' */
   0x55555540084b <isitreal+273>    call   puts@plt                    <puts@plt>
 
   0x555555400850 <isitreal+278>    mov    rax, qword ptr [rbp - 0x18]
   0x555555400854 <isitreal+282>    xor    rax, qword ptr fs:[0x28]
   0x55555540085d <isitreal+291>    je     isitreal+298                <isitreal+298>
 
   0x55555540085f <isitreal+293>    call   __stack_chk_fail@plt        <__stack_chk_fail@plt>
 
   0x555555400864 <isitreal+298>    add    rsp, 0x78
   0x555555400868 <isitreal+302>    pop    rbx
   0x555555400869 <isitreal+303>    pop    rbp
────────────────────────────────────────────────────────[ STACK ]─────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffdc30 ◂— 0
... ↓        2 skipped
03:0018│-068 0x7fffffffdc48 ◂— 0x6100000000
04:0020│-060 0x7fffffffdc50 ◂— ']]VdMb`YCzprNV/tGxP\\NxBM_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
05:0028│-058 0x7fffffffdc58 ◂— 'CzprNV/tGxP\\NxBM_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
06:0030│-050 0x7fffffffdc60 ◂— 'GxP\\NxBM_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
07:0038│-048 0x7fffffffdc68 ◂— '_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
──────────────────────────────────────────────────────[ BACKTRACE ]───────────────────────────────────────────────────────
 ► 0   0x5555554007d0 isitreal+150
   1   0x55555540088b main+32
   2   0x7ffff7c29d90 __libc_start_call_main+128
   3   0x7ffff7c29e40 __libc_start_main+128
   4   0x55555540065a _start+42
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg><b> jump *0x00005555554007d6</b>
Continuing at 0x5555554007d6.
Congratulations!!! Here is your flag ...
<b>CTF_BD{JJAsZuwNTmgeYA8cPoGKYoUZHgZMFgZDHPMJrJ4JmHFu33f2SzBYN6iegFtQ}</b>
?? Is it really the flag??
[Inferior 1 (process 21943) exited normally]
</pre>
