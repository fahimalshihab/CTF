<pre>
<b>iftx@iftx-Modern-15-A5M:~/Desktop/RE/rev$ gdb ./check </b>
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
Reading symbols from ./check...
(No debugging symbols found in ./check)
------- tip of the day (disable with set show-tips off) -------
Use vmmap -A|-B <number> <filter> to display <number> of maps after/before filtered ones
<b>pwndbg> info functions </b>
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  puts@plt
0x0000000000001040  strlen@plt
0x0000000000001050  __stack_chk_fail@plt
0x0000000000001060  setbuf@plt
0x0000000000001070  printf@plt
0x0000000000001080  fgets@plt
0x0000000000001090  strcmp@plt
0x00000000000010a0  _start
0x00000000000010d0  deregister_tm_clones
0x0000000000001100  register_tm_clones
0x0000000000001140  __do_global_dtors_aux
0x0000000000001190  frame_dummy
0x0000000000001199  main
0x00000000000012d0  __libc_csu_init
0x0000000000001340  __libc_csu_fini
0x0000000000001348  _fini
<b>pwndbg> disassemble main </b>
Dump of assembler code for function main:
   0x0000000000001199 <+0>:	push   rbp
   0x000000000000119a <+1>:	mov    rbp,rsp
   0x000000000000119d <+4>:	sub    rsp,0x50
   0x00000000000011a1 <+8>:	mov    rax,QWORD PTR fs:0x28
   0x00000000000011aa <+17>:	mov    QWORD PTR [rbp-0x8],rax
   0x00000000000011ae <+21>:	xor    eax,eax
   0x00000000000011b0 <+23>:	mov    rax,QWORD PTR [rip+0x2ea9]        # 0x4060 <stdout@@GLIBC_2.2.5>
   0x00000000000011b7 <+30>:	mov    esi,0x0
   0x00000000000011bc <+35>:	mov    rdi,rax
   0x00000000000011bf <+38>:	call   0x1060 <setbuf@plt>
   0x00000000000011c4 <+43>:	mov    BYTE PTR [rbp-0x50],0x63
   0x00000000000011c8 <+47>:	mov    BYTE PTR [rbp-0x4f],0x68
   0x00000000000011cc <+51>:	mov    BYTE PTR [rbp-0x4e],0x33
   0x00000000000011d0 <+55>:	mov    BYTE PTR [rbp-0x4d],0x63
   0x00000000000011d4 <+59>:	mov    BYTE PTR [rbp-0x4c],0x6b
   0x00000000000011d8 <+63>:	mov    BYTE PTR [rbp-0x4b],0x5f
   0x00000000000011dc <+67>:	mov    BYTE PTR [rbp-0x4a],0x61
   0x00000000000011e0 <+71>:	mov    BYTE PTR [rbp-0x49],0x6e
   0x00000000000011e4 <+75>:	mov    BYTE PTR [rbp-0x48],0x44
   0x00000000000011e8 <+79>:	mov    BYTE PTR [rbp-0x47],0x5f
   0x00000000000011ec <+83>:	lea    rdi,[rip+0xe15]        # 0x2008
   0x00000000000011f3 <+90>:	mov    eax,0x0
   0x00000000000011f8 <+95>:	call   0x1070 <printf@plt>
   0x00000000000011fd <+100>:	mov    BYTE PTR [rbp-0x46],0x72
   0x0000000000001201 <+104>:	mov    BYTE PTR [rbp-0x45],0x33
   0x0000000000001205 <+108>:	mov    BYTE PTR [rbp-0x44],0x63
   0x0000000000001209 <+112>:	mov    BYTE PTR [rbp-0x43],0x68
   0x000000000000120d <+116>:	mov    BYTE PTR [rbp-0x42],0x65
   0x0000000000001211 <+120>:	mov    BYTE PTR [rbp-0x41],0x63
   0x0000000000001215 <+124>:	mov    BYTE PTR [rbp-0x40],0x4b
   0x0000000000001219 <+128>:	mov    BYTE PTR [rbp-0x3f],0x5f
   0x000000000000121d <+132>:	mov    rdx,QWORD PTR [rip+0x2e4c]        # 0x4070 <stdin@@GLIBC_2.2.5>
   0x0000000000001224 <+139>:	lea    rax,[rbp-0x30]
   0x0000000000001228 <+143>:	mov    esi,0x28
   0x000000000000122d <+148>:	mov    rdi,rax
   0x0000000000001230 <+151>:	call   0x1080 <fgets@plt>
   0x0000000000001235 <+156>:	mov    BYTE PTR [rbp-0x3e],0x61
   0x0000000000001239 <+160>:	mov    BYTE PTR [rbp-0x3d],0x67
   0x000000000000123d <+164>:	mov    BYTE PTR [rbp-0x3c],0x61
   0x0000000000001241 <+168>:	mov    BYTE PTR [rbp-0x3b],0x31
   0x0000000000001245 <+172>:	mov    BYTE PTR [rbp-0x3a],0x6e
   0x0000000000001249 <+176>:	lea    rax,[rbp-0x30]
   0x000000000000124d <+180>:	mov    rdi,rax
   0x0000000000001250 <+183>:	call   0x1040 <strlen@plt>
   0x0000000000001255 <+188>:	sub    rax,0x1
   0x0000000000001259 <+192>:	mov    BYTE PTR [rbp+rax*1-0x30],0x0
   0x000000000000125e <+197>:	mov    BYTE PTR [rbp-0x39],0x21
   0x0000000000001262 <+201>:	mov    BYTE PTR [rbp-0x38],0x0
   0x0000000000001266 <+205>:	lea    rdx,[rbp-0x30]
   0x000000000000126a <+209>:	lea    rax,[rbp-0x50]
   0x000000000000126e <+213>:	mov    rsi,rdx
   0x0000000000001271 <+216>:	mov    rdi,rax
<b>0x0000000000001274 <+219>:	call   0x1090 strcmp@plt </b>
   0x0000000000001279 <+224>:	test   eax,eax
   0x000000000000127b <+226>:	je     0x1290 <main+247>
   0x000000000000127d <+228>:	lea    rdi,[rip+0xdaa]        # 0x202e
   0x0000000000001284 <+235>:	call   0x1030 <puts@plt>
   0x0000000000001289 <+240>:	mov    eax,0x0
   0x000000000000128e <+245>:	jmp    0x12ad <main+276>
   0x0000000000001290 <+247>:	lea    rax,[rbp-0x30]
   0x0000000000001294 <+251>:	mov    rsi,rax
   0x0000000000001297 <+254>:	lea    rdi,[rip+0xda2]        # 0x2040
   0x000000000000129e <+261>:	mov    eax,0x0
   0x00000000000012a3 <+266>:	call   0x1070 <printf@plt>
   0x00000000000012a8 <+271>:	mov    eax,0x0
   0x00000000000012ad <+276>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x00000000000012b1 <+280>:	sub    rcx,QWORD PTR fs:0x28
   0x00000000000012ba <+289>:	je     0x12c1 <main+296>
   0x00000000000012bc <+291>:	call   0x1050 <__stack_chk_fail@plt>
   0x00000000000012c1 <+296>:	leave  
   0x00000000000012c2 <+297>:	ret    
End of assembler dump.
<b>pwndbg> r</b>
Starting program: /home/iftx/Desktop/RE/rev/check 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
TopSpy Association
Enter the secret: 123
Incorrect! >_<
[Inferior 1 (process 22174) exited normally]
<b>pwndbg> disassemble main </b>
Dump of assembler code for function main:
   0x0000555555555199 <+0>:	push   rbp
   0x000055555555519a <+1>:	mov    rbp,rsp
   0x000055555555519d <+4>:	sub    rsp,0x50
   0x00005555555551a1 <+8>:	mov    rax,QWORD PTR fs:0x28
   0x00005555555551aa <+17>:	mov    QWORD PTR [rbp-0x8],rax
   0x00005555555551ae <+21>:	xor    eax,eax
   0x00005555555551b0 <+23>:	mov    rax,QWORD PTR [rip+0x2ea9]        # 0x555555558060 <stdout@@GLIBC_2.2.5>
   0x00005555555551b7 <+30>:	mov    esi,0x0
   0x00005555555551bc <+35>:	mov    rdi,rax
   0x00005555555551bf <+38>:	call   0x555555555060 <setbuf@plt>
   0x00005555555551c4 <+43>:	mov    BYTE PTR [rbp-0x50],0x63
   0x00005555555551c8 <+47>:	mov    BYTE PTR [rbp-0x4f],0x68
   0x00005555555551cc <+51>:	mov    BYTE PTR [rbp-0x4e],0x33
   0x00005555555551d0 <+55>:	mov    BYTE PTR [rbp-0x4d],0x63
   0x00005555555551d4 <+59>:	mov    BYTE PTR [rbp-0x4c],0x6b
   0x00005555555551d8 <+63>:	mov    BYTE PTR [rbp-0x4b],0x5f
   0x00005555555551dc <+67>:	mov    BYTE PTR [rbp-0x4a],0x61
   0x00005555555551e0 <+71>:	mov    BYTE PTR [rbp-0x49],0x6e
   0x00005555555551e4 <+75>:	mov    BYTE PTR [rbp-0x48],0x44
   0x00005555555551e8 <+79>:	mov    BYTE PTR [rbp-0x47],0x5f
   0x00005555555551ec <+83>:	lea    rdi,[rip+0xe15]        # 0x555555556008
   0x00005555555551f3 <+90>:	mov    eax,0x0
   0x00005555555551f8 <+95>:	call   0x555555555070 <printf@plt>
   0x00005555555551fd <+100>:	mov    BYTE PTR [rbp-0x46],0x72
   0x0000555555555201 <+104>:	mov    BYTE PTR [rbp-0x45],0x33
   0x0000555555555205 <+108>:	mov    BYTE PTR [rbp-0x44],0x63
   0x0000555555555209 <+112>:	mov    BYTE PTR [rbp-0x43],0x68
   0x000055555555520d <+116>:	mov    BYTE PTR [rbp-0x42],0x65
   0x0000555555555211 <+120>:	mov    BYTE PTR [rbp-0x41],0x63
   0x0000555555555215 <+124>:	mov    BYTE PTR [rbp-0x40],0x4b
   0x0000555555555219 <+128>:	mov    BYTE PTR [rbp-0x3f],0x5f
   0x000055555555521d <+132>:	mov    rdx,QWORD PTR [rip+0x2e4c]        # 0x555555558070 <stdin@@GLIBC_2.2.5>
   0x0000555555555224 <+139>:	lea    rax,[rbp-0x30]
   0x0000555555555228 <+143>:	mov    esi,0x28
   0x000055555555522d <+148>:	mov    rdi,rax
   0x0000555555555230 <+151>:	call   0x555555555080 <fgets@plt>
   0x0000555555555235 <+156>:	mov    BYTE PTR [rbp-0x3e],0x61
   0x0000555555555239 <+160>:	mov    BYTE PTR [rbp-0x3d],0x67
   0x000055555555523d <+164>:	mov    BYTE PTR [rbp-0x3c],0x61
   0x0000555555555241 <+168>:	mov    BYTE PTR [rbp-0x3b],0x31
   0x0000555555555245 <+172>:	mov    BYTE PTR [rbp-0x3a],0x6e
   0x0000555555555249 <+176>:	lea    rax,[rbp-0x30]
   0x000055555555524d <+180>:	mov    rdi,rax
   0x0000555555555250 <+183>:	call   0x555555555040 <strlen@plt>
   0x0000555555555255 <+188>:	sub    rax,0x1
   0x0000555555555259 <+192>:	mov    BYTE PTR [rbp+rax*1-0x30],0x0
   0x000055555555525e <+197>:	mov    BYTE PTR [rbp-0x39],0x21
   0x0000555555555262 <+201>:	mov    BYTE PTR [rbp-0x38],0x0
   0x0000555555555266 <+205>:	lea    rdx,[rbp-0x30]
   0x000055555555526a <+209>:	lea    rax,[rbp-0x50]
   0x000055555555526e <+213>:	mov    rsi,rdx
   0x0000555555555271 <+216>:	mov    rdi,rax
<b>0x0000555555555274 <+219>:	call   0x555555555090 <strcmp@plt></b>
   0x0000555555555279 <+224>:	test   eax,eax
   0x000055555555527b <+226>:	je     0x555555555290 <main+247>
   0x000055555555527d <+228>:	lea    rdi,[rip+0xdaa]        # 0x55555555602e
   0x0000555555555284 <+235>:	call   0x555555555030 <puts@plt>
   0x0000555555555289 <+240>:	mov    eax,0x0
   0x000055555555528e <+245>:	jmp    0x5555555552ad <main+276>
   0x0000555555555290 <+247>:	lea    rax,[rbp-0x30]
   0x0000555555555294 <+251>:	mov    rsi,rax
   0x0000555555555297 <+254>:	lea    rdi,[rip+0xda2]        # 0x555555556040
   0x000055555555529e <+261>:	mov    eax,0x0
   0x00005555555552a3 <+266>:	call   0x555555555070 <printf@plt>
   0x00005555555552a8 <+271>:	mov    eax,0x0
   0x00005555555552ad <+276>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x00005555555552b1 <+280>:	sub    rcx,QWORD PTR fs:0x28
   0x00005555555552ba <+289>:	je     0x5555555552c1 <main+296>
   0x00005555555552bc <+291>:	call   0x555555555050 <__stack_chk_fail@plt>
   0x00005555555552c1 <+296>:	leave  
   0x00005555555552c2 <+297>:	ret    
End of assembler dump.
<b>pwndbg> b *0x0000555555555274</b>
Breakpoint 1 at 0x555555555274
<b>pwndbg> r</b>
Starting program: /home/iftx/Desktop/RE/rev/check 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
TopSpy Association
Enter the secret: 123

Breakpoint 1, 0x0000555555555274 in main ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
──────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]──────────────────────────────────
*RAX  0x7fffffffdc80 ◂— 'ch3ck_anD_r3checK_aga1n!'
 RBX  0
*RCX  0x5555555592a4 ◂— 0
*RDX  0x7fffffffdca0 ◂— 0x333231 /* '123' */
*RDI  0x7fffffffdc80 ◂— 'ch3ck_anD_r3checK_aga1n!'
*RSI  0x7fffffffdca0 ◂— 0x333231 /* '123' */
 R8   0
*R9   0x5555555592a0 ◂— 0xa333231 /* '123\n' */
*R10  0x7ffff7c0e940 ◂— 0xf001a00007035 /* '5p' */
*R11  0x7ffff7d9d7e0 (__strlen_avx2) ◂— endbr64 
*R12  0x7fffffffdde8 —▸ 0x7fffffffe195 ◂— '/home/iftx/Desktop/RE/rev/check'
*R13  0x555555555199 (main) ◂— push rbp
 R14  0
*R15  0x7ffff7ffd040 (_rtld_global) —▸ 0x7ffff7ffe2e0 —▸ 0x555555554000 ◂— 0x10102464c457f
*RBP  0x7fffffffdcd0 ◂— 1
*RSP  0x7fffffffdc80 ◂— 'ch3ck_anD_r3checK_aga1n!'
*RIP  0x555555555274 (main+219) ◂— call 0x555555555090
───────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]───────────────────────────────────────────
 ► 0x555555555274 <main+219>    call   strcmp@plt                  <strcmp@plt>
        s1: 0x7fffffffdc80 ◂— 'ch3ck_anD_r3checK_aga1n!'
        s2: 0x7fffffffdca0 ◂— 0x333231 /* '123' */
 
   0x555555555279 <main+224>    test   eax, eax
   0x55555555527b <main+226>    je     main+247                    <main+247>
 
   0x55555555527d <main+228>    lea    rdi, [rip + 0xdaa]     RDI => 0x55555555602e ◂— 'Incorrect! >_<'
   0x555555555284 <main+235>    call   puts@plt                    <puts@plt>
 
   0x555555555289 <main+240>    mov    eax, 0                 EAX => 0
   0x55555555528e <main+245>    jmp    main+276                    <main+276>
    ↓
   0x5555555552ad <main+276>    mov    rcx, qword ptr [rbp - 8]
   0x5555555552b1 <main+280>    sub    rcx, qword ptr fs:[0x28]
   0x5555555552ba <main+289>    je     main+296                    <main+296>
 
   0x5555555552bc <main+291>    call   __stack_chk_fail@plt        <__stack_chk_fail@plt>
────────────────────────────────────────────────────────[ STACK ]─────────────────────────────────────────────────────────
<b>00:0000│ rax rdi rsp 0x7fffffffdc80 ◂— 'ch3ck_anD_r3checK_aga1n!'</b>
01:0008│-048         0x7fffffffdc88 ◂— 'D_r3checK_aga1n!'
02:0010│-040         0x7fffffffdc90 ◂— 'K_aga1n!'
03:0018│-038         0x7fffffffdc98 ◂— 0x10101000000
04:0020│ rdx rsi     0x7fffffffdca0 ◂— 0x333231 /* '123' */
05:0028│-028         0x7fffffffdca8 ◂— 0x178bfbff
06:0030│-020         0x7fffffffdcb0 —▸ 0x7fffffffe189 ◂— 0x34365f363878 /* 'x86_64' */
07:0038│-018         0x7fffffffdcb8 ◂— 0x64 /* 'd' */
──────────────────────────────────────────────────────[ BACKTRACE ]───────────────────────────────────────────────────────
 ► 0   0x555555555274 main+219
   1   0x7ffff7c29d90 __libc_start_call_main+128
   2   0x7ffff7c29e40 __libc_start_main+128
   3   0x5555555550ce _start+46
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> quit
<b>iftx@iftx-Modern-15-A5M:~/Desktop/RE/rev$ ./check</b> 
TopSpy Association
<b>Enter the secret: ch3ck_anD_r3checK_aga1n!</b>
Welcome Agent, heres's a small gift:<b> HTB{ch3ck_anD_r3checK_aga1n!}</b>
</pre>
