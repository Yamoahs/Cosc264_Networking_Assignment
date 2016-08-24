#!/usr/bin/python
import sys
import socket

'''
Sender Sockets: s_in and s_out

'''
#IP address
HOST =  "127.0.0.1"

#valid Port no.
VALID_PORTS =  range(1024, 64001)

# Get the arguments list
args = (sys.argv)
#cmdargs.pop(0)

#try:
if len(args) == 5:
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            #HAVE A TRY EXCEPTION
            print("port {} not a valid port".format(port))
    sender_in_port = args[1]
    sender_out_port = args[2]
    channel_sender_in = args[3]
    filename = str(args[4])

    print("IN PORT: {}\nOUT PORT: {}\n\
channel_sender_in PORT: {}\nFILENAME: {}".format(sender_in_port, \
     sender_out_port, channel_sender_in, filename))

else:
    print("Input ERROR")
#raise Exception("Invalid number of parameters")

#Create the sockets
sender_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the sockets
sender_in.bind((HOST,sender_in_port))
sender_out.bind((HOST,sender_out_port))


s_in.connect(("localhost", 1234))

data = "hello server"
s_in.send(data.encode('utf-8'))
data = s_in.recv(512)
print("From Reciever: ", data.decode('utf-8'))

s_in.close()
