#!/usr/bin/python
import sys
import socket
import os.path

'''
Sender Sockets: s_in and s_out

'''
#IP address
HOST =  "127.0.0.1"

#valid Port no.
VALID_PORTS =  range(1024, 64001)

# Get the arguments list
args = (sys.argv)

#Flag to make sure stdin arguemtents
stdin_successful = False

#try:
if len(args) == 5:
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            #HAVE A TRY EXCEPTION
            print("port {} not a valid port".format(port))
            quit()
    sender_in_port = int(args[1])
    sender_out_port = int(args[2])
    reciever_in_port = int(args[3])
    filename = str(args[4])

    #Checking if input file exists
    if os.path.isfile(filename):
        #Open File
        input_file = open(filename, 'rb')
        stdin_successful = True
    else:
        print('File does not exists')

else:
    print("Input ERROR")
#raise Exception("Invalid number of parameters")

#if stdin inputs are corerct begin socket initialisation
if stdin_successful:

    print("IN PORT: {}\nOUT PORT: {}\nRECIEVER IN PORT: {}\nFILENAME: {}"\
    .format(sender_in_port, sender_out_port, reciever_in_port, filename))


    #Create the sockets
    sender_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Bind the sockets
    sender_in_socket.bind((HOST,sender_in_port))
    sender_out_socket.bind((HOST,sender_out_port))

    #Connect the sockets
    sender_out_socket.connect((HOST,reciever_in_port))

    next_ = 0

    data = "hello Reciever"
    sender_out_socket.send(data.encode('utf-8'))
    data = sender_in_socket.recv(512)
    print("From Reciever: ", data.decode('utf-8'))


    sender_out_socket.close()
    sender_in_socket.close()

    #closing the file
    input_file.close()
