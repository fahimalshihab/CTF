# 1)the_shark

[auth_sniff.pcapng.zip](https://github.com/fahimalshihab/CTF/files/12936119/auth_sniff.pcapng.zip)
 TCP
--> wireshark --> follow --> TCP stram


└─$ echo "c2VjdmFsOlNlY1ZhbHs4NDVJYzR1N2hfaTVfNVVQM1JfNWhJN30=" |base64 -d

SecVal{845Ic4u7h_i5_5UP3R_5hI7}                                                                                              

# 2)the_shell

[rev_shell.pcapng.zip](https://github.com/fahimalshihab/CTF/files/12936616/rev_shell.pcapng.zip)


--> wireshark --> follow --> TCP stram

SecVal{rev_shell_fun_insec}

# 3)the_data
[the_data.pcapng.zip](https://github.com/fahimalshihab/CTF/files/12936688/the_data.pcapng.zip)

HTTP

--> wireshark --> follow --> TCP stram

found file.png so

--> file --> export object --> HTTP --> save all

found flag.png


