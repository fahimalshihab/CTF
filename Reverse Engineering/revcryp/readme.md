<code>


 ┌──(iftx㉿kali)-[~/Desktop/revcryp]
└─$ <b>gdb revcryp</b>
GNU gdb (Debian 13.2-1) 13.2
Copyright (C) 2023 Free Software Foundation, Inc.
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
pwndbg: loaded 148 pwndbg commands and 47 shell commands. Type pwndbg [--shell | --all] [filter] for a list.
pwndbg: created $rebase, $ida GDB functions (can be used with print/break)
Reading symbols from revcryp...
(No debugging symbols found in revcryp)
------- tip of the day (disable with set show-tips off) -------
If your program has multiple threads they will be displayed in the context display or using the context threads command
pwndbg> info functions
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
<b>pwndbg> disass isitreal</b>
Dump of assembler code for function isitreal:
   0x000000000000073a <+0>:     push   rbp
   0x000000000000073b <+1>:     mov    rbp,rsp
   0x000000000000073e <+4>:     push   rbx
   0x000000000000073f <+5>:     sub    rsp,0x78
   0x0000000000000743 <+9>:     mov    DWORD PTR [rbp-0x74],edi
   0x0000000000000746 <+12>:    mov    rax,QWORD PTR fs:0x28
   0x000000000000074f <+21>:    mov    QWORD PTR [rbp-0x18],rax
   0x0000000000000753 <+25>:    xor    eax,eax
   0x0000000000000755 <+27>:    mov    DWORD PTR [rbp-0x68],0x0
   0x000000000000075c <+34>:    mov    DWORD PTR [rbp-0x64],0x61
   0x0000000000000763 <+41>:    movabs rax,0x5960624d64565d5d
   0x000000000000076d <+51>:    movabs rdx,0x742f564e72707a43
   0x0000000000000777 <+61>:    mov    QWORD PTR [rbp-0x60],rax
   0x000000000000077b <+65>:    mov    QWORD PTR [rbp-0x58],rdx
   0x000000000000077f <+69>:    movabs rax,0x4d42784e5c507847
   0x0000000000000789 <+79>:    movabs rdx,0x534d70515a4d705f
   0x0000000000000793 <+89>:    mov    QWORD PTR [rbp-0x50],rax
   0x0000000000000797 <+93>:    mov    QWORD PTR [rbp-0x48],rdx
   0x000000000000079b <+97>:    movabs rax,0x5d235d655d5a475f
   0x00000000000007a5 <+107>:   movabs rdx,0x2571242462515f7a
   0x00000000000007af <+117>:   mov    QWORD PTR [rbp-0x40],rax
   0x00000000000007b3 <+121>:   mov    QWORD PTR [rbp-0x38],rdx
   0x00000000000007b7 <+125>:   movabs rax,0x727e21594e556d44
   0x00000000000007c1 <+135>:   mov    QWORD PTR [rbp-0x30],rax
   0x00000000000007c5 <+139>:   mov    DWORD PTR [rbp-0x28],0x46635170
   0x00000000000007cc <+146>:   mov    BYTE PTR [rbp-0x24],0x0
   0x00000000000007d0 <+150>:   cmp    DWORD PTR [rbp-0x74],0x1
   0x00000000000007d4 <+154>:   jne    0x844 <isitreal+266>
   0x00000000000007d6 <+156>:   mov    DWORD PTR [rbp-0x68],0x0
   0x00000000000007dd <+163>:   jmp    0x7fb <isitreal+193>
   0x00000000000007df <+165>:   mov    eax,DWORD PTR [rbp-0x68]
   0x00000000000007e2 <+168>:   cdqe
   0x00000000000007e4 <+170>:   movzx  eax,BYTE PTR [rbp+rax*1-0x60]
   0x00000000000007e9 <+175>:   xor    eax,0x17
   0x00000000000007ec <+178>:   mov    edx,eax
   0x00000000000007ee <+180>:   mov    eax,DWORD PTR [rbp-0x68]
   0x00000000000007f1 <+183>:   cdqe
   0x00000000000007f3 <+185>:   mov    BYTE PTR [rbp+rax*1-0x60],dl
   0x00000000000007f7 <+189>:   add    DWORD PTR [rbp-0x68],0x1
   0x00000000000007fb <+193>:   mov    eax,DWORD PTR [rbp-0x68]
   0x00000000000007fe <+196>:   movsxd rbx,eax
   0x0000000000000801 <+199>:   lea    rax,[rbp-0x60]
   0x0000000000000805 <+203>:   mov    rdi,rax
   0x0000000000000808 <+206>:   call   0x5f0 <strlen@plt>
   0x000000000000080d <+211>:   cmp    rbx,rax
   0x0000000000000810 <+214>:   jb     0x7df <isitreal+165>
   0x0000000000000812 <+216>:   lea    rdi,[rip+0x10f]        # 0x928
   0x0000000000000819 <+223>:   call   0x5e0 <puts@plt>
   0x000000000000081e <+228>:   lea    rax,[rbp-0x60]
   0x0000000000000822 <+232>:   mov    rsi,rax
   0x0000000000000825 <+235>:   lea    rdi,[rip+0x125]        # 0x951
   0x000000000000082c <+242>:   mov    eax,0x0
   0x0000000000000831 <+247>:   call   0x610 <printf@plt>
   0x0000000000000836 <+252>:   lea    rdi,[rip+0x120]        # 0x95d
   0x000000000000083d <+259>:   call   0x5e0 <puts@plt>
   0x0000000000000842 <+264>:   jmp    0x850 <isitreal+278>
   0x0000000000000844 <+266>:   lea    rdi,[rip+0x12d]        # 0x978
   0x000000000000084b <+273>:   call   0x5e0 <puts@plt>
   0x0000000000000850 <+278>:   mov    rax,QWORD PTR [rbp-0x18]
   0x0000000000000854 <+282>:   xor    rax,QWORD PTR fs:0x28
   0x000000000000085d <+291>:   je     0x864 <isitreal+298>
   0x000000000000085f <+293>:   call   0x600 <__stack_chk_fail@plt>
   0x0000000000000864 <+298>:   add    rsp,0x78
   0x0000000000000868 <+302>:   pop    rbx
   0x0000000000000869 <+303>:   pop    rbp
   0x000000000000086a <+304>:   ret
End of assembler dump.
<b>pwndbg> b *0x00005555554007d0</b>
Breakpoint 1 at 0x5555554007d0
pwndbg> r
Starting program: /home/iftx/Desktop/revcryp/revcryp 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00005555554007d0 in isitreal ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]───────────────────────────────────
*RAX  0x727e21594e556d44 ('DmUNY!~r')
*RBX  0x7fffffffdef8 —▸ 0x7fffffffe269 ◂— '/home/iftx/Desktop/revcryp/revcryp'
*RCX  0x7ffff7f95840 (__exit_funcs) —▸ 0x7ffff7f97300 (initial) ◂— 0x0
*RDX  0x2571242462515f7a ('z_Qb$$q%')
 RDI  0x0
*RSI  0x7fffffffdef8 —▸ 0x7fffffffe269 ◂— '/home/iftx/Desktop/revcryp/revcryp'
*R8   0x555555400910 (__libc_csu_fini) ◂— repz ret 
*R9   0x7ffff7fcfb10 (_dl_fini) ◂— push r15
*R10  0x7ffff7fcb858 ◂— 0xa00120000000e
*R11  0x7ffff7fe1e30 (_dl_audit_preinit) ◂— mov eax, dword ptr [rip + 0x1b022]
 R12  0x0
*R13  0x7fffffffdf08 —▸ 0x7fffffffe28c ◂— 'COLORFGBG=15;0'
 R14  0x0
*R15  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2d0 —▸ 0x555555400000 ◂— jg 0x555555400047
*RBP  0x7fffffffddc0 —▸ 0x7fffffffdde0 ◂— 0x1
*RSP  0x7fffffffdd40 ◂— 0x8
*RIP  0x5555554007d0 (isitreal+150) ◂— cmp dword ptr [rbp - 0x74], 1
────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]────────────────────────────────────────────
 ► 0x5555554007d0 <isitreal+150>    cmp    dword ptr [rbp - 0x74], 1
   0x5555554007d4 <isitreal+154>    jne    isitreal+266                <isitreal+266>
    ↓
   0x555555400844 <isitreal+266>    lea    rdi, [rip + 0x12d]
   0x55555540084b <isitreal+273>    call   puts@plt                <puts@plt>
 
   0x555555400850 <isitreal+278>    mov    rax, qword ptr [rbp - 0x18]
   0x555555400854 <isitreal+282>    xor    rax, qword ptr fs:[0x28]
   0x55555540085d <isitreal+291>    je     isitreal+298                <isitreal+298>
 
   0x55555540085f <isitreal+293>    call   __stack_chk_fail@plt                <__stack_chk_fail@plt>
 
   0x555555400864 <isitreal+298>    add    rsp, 0x78
   0x555555400868 <isitreal+302>    pop    rbx
   0x555555400869 <isitreal+303>    pop    rbp
─────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffdd40 ◂— 0x8
01:0008│     0x7fffffffdd48 ◂— 0x40 /* '@' */
02:0010│     0x7fffffffdd50 ◂— 0x80000
03:0018│     0x7fffffffdd58 ◂— 0x6100000000
04:0020│     0x7fffffffdd60 ◂— ']]VdMb`YCzprNV/tGxP\\NxBM_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
05:0028│     0x7fffffffdd68 ◂— 'CzprNV/tGxP\\NxBM_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
06:0030│     0x7fffffffdd70 ◂— 'GxP\\NxBM_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
07:0038│     0x7fffffffdd78 ◂— '_pMZQpMS_GZ]e]#]z_Qb$$q%DmUNY!~rpQcF'
───────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────
 ► 0   0x5555554007d0 isitreal+150
   1   0x55555540088b main+32
   2   0x7ffff7de96ca __libc_start_call_main+122
   3   0x7ffff7de9785 __libc_start_main+133
   4   0x55555540065a _start+42
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
<b>pwndbg> jump * 0x00005555554007d6</b>
Continuing at 0x5555554007d6.
Congratulations!!! Here is your flag ...
<b>CTF_BD{JJAsZuwNTmgeYA8cPoGKYoUZHgZMFgZDHPMJrJ4JmHFu33f2SzBYN6iegFtQ}</b>
?? Is it really the flag??
[Inferior 1 (process 8986) exited normally]
 
</code>
