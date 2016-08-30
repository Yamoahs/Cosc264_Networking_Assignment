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
if len(args) == 4:
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            #HAVE A TRY EXCEPTION
            print("port {} not a valid port".format(port))
    sender_in_port = int(args[1])
    sender_out_port = int(args[2])
    filename = str(args[0])

    print("IN PORT: {}\nOUT PORT: {}\nFILENAME: {}".format(sender_in_port, \
     sender_out_port, filename))

else:
    print("Input ERROR")
#raise Exception("Invalid number of parameters")

#Create the sockets
sender_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the sockets
sender_in_socket.bind((HOST,sender_in_port))
sender_out_socket.bind((HOST,sender_out_port))

#Connect the sockets
sender_out_socket.connect((HOST,sender_out_port))

#open the file
input_file = open(filename, 'rb')




sender_out_socket.send(filename.encode('utf-8'))
filename = sender_out_socket.recv(512)
print("From Reciever: ", filename.decode('utf-8'))

sender_out_socket.close()
sender_in_socket.close()

#closing the file
input_file.close()
