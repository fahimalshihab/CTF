# HOW TO START
<pre>
>> strings ./test 
  //to see if the flag is obvious.
  
>>strings ./test | grep flag
  //to grep flag from stirngs.
  
>> file test
  //ELF ,PE, AIF
  //if the file not stripted then we have to make it exicutable 
  
>>ls -al
  
>> chmod +x test
  
>> ./test
  
>> ltrace ./test 
   //how ltrace is used: The output of ltrace shows a readable code of what the program did. ltrace logged library functions that the program called and received. 
  
>> r2 -dA test
  // d for debugging A for analysis
  What is radare2?
Radare2 is an open-source reversing framework. It combines multiple tools together to help analyze a binary. I usually run it along with gdb to understand what a binary is doing (when we don’t have the source code 😄).

 [ afl ]-->list functions
 [pdf @main] -->To print disassembly of function
  






  
</pre>
