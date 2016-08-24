#!/usr/bin/python
import sys
import socket

'''
Sender Sockets: s_in and s_out

'''
#valid Port no.
VALID_PORTS =  range(1024, 64001)

# Get the arguments list
args = (sys.argv)
#cmdargs.pop(0)

#try:
if len(cmdargs) == 5:
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            #HAVE A TRY EXCEPTION
            print("port {} not a valid port".format(port))
else:
    print("Inut ERROR")
#raise Exception("Invalid number of parameters")






s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_in.connect(("localhost", 1234))

data = "hello server"
s_in.send(data.encode('utf-8'))
data = s_in.recv(512)
print("From Reciever: ", data.decode('utf-8'))

s_in.close()
