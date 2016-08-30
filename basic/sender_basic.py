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
    sender_in_port = int(args[1])
    sender_out_port = int(args[2])
    reciever_sender_in = int(args[3])
    filename = str(args[4])

    print("IN PORT: {}\nOUT PORT: {}\n\
reciever_sender_in PORT: {}\nFILENAME: {}".format(sender_in_port, \
     sender_out_port, reciever_sender_in, filename))

else:
    print("Input ERROR")
#raise Exception("Invalid number of parameters")

#Create the sockets
sender_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the sockets
sender_in.bind((HOST,sender_in_port))
sender_out.bind((HOST,sender_out_port))

#Connect the sockets
sender_out.connect((HOST,reciever_sender_in))

#open the file
# try:
#     input_file = open(filename, 'rb')
# except FileExistsError:
#     pass



sender_out.send(filename.encode('utf-8'))
filename = sender_out.recv(512)
print("From Reciever: ", filename.decode('utf-8'))

sender_out.close()
sender_in.close()
