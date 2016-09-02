#!/usr/bin/python
import sys
import socket
import select
import os.path

'''
Reciever Sockets: r_in and r_out

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
    reciever_in_port = int(args[1])
    reciever_out_port = int(args[2])
    sender_in_port = int(args[3])
    out_filename = str(args[4])

    #Opening output file
    if os.path.isfile(out_filename):
        print('File already exists')
    else:
        output_file = open(out_filename, "w")
        stdin_successful = True
    # output_file = open("{}".format(out_filename).read())


else:
    print("Input ERROR")

if stdin_successful:

    print("IN PORT: {}\nOUT PORT: {}\nSENDER IN PORT: {}\nFILENAME: {}"\
    .format(reciever_in_port, reciever_out_port, sender_in_port, out_filename))

    #Create the sockets
    receiver_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Bind the sockets
    receiver_in_socket.bind((HOST,reciever_in_port))
    receiver_out_socket.bind((HOST,reciever_out_port))

    #connect the socket
    receiver_out_socket.connect((HOST,sender_in_port))


    #expected
    expected = 0

    data = receiver_in_socket.recv(512)
    print("From Sender: ", data.decode('utf-8'))
    data = "Back to ya sender"
    receiver_out_socket.send(data.encode('utf-8'))






    #closing sockets
    receiver_in_socket.close()
    receiver_out_socket.close()

    #closing the file
    #output_file.close()
