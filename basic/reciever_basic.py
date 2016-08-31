# import socket
#
# r_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# r_in.bind(("", 1234))
#
# r_in.listen(5)
#
# r_in, address = r_in.accept()
#
# data = r_in.recv(512)
# print("From Sender: ", data.decode('utf-8'))
# data = "Back to ya sender"
# r_in.send(data.encode('utf-8'))
#
# r_in.close()

#!/usr/bin/python
import sys
import socket
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

#try:
if len(args) == 4:
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            #HAVE A TRY EXCEPTION
            print("port {} not a valid port".format(port))
    reciever_in_port = int(args[1])
    reciever_out_port = int(args[2])
    out_filename = str(args[3])

    print("IN PORT: {}\nOUT PORT: {}\nFILENAME: {}".format(reciever_in_port, \
     reciever_out_port, out_filename))

else:
    print("Input ERROR")

#Create the sockets
receiver_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the sockets
receiver_in_socket.bind((HOST,reciever_in_port))
receiver_out_socket.bind((HOST,reciever_out_port))

#connect the socket
receiver_out_socket.connect((HOST,reciever_out_port))

#Opening output file
if os.path.isfile(out_filename):
    print('File already exists')
else:
    output_file = open(out_filename, "w")
# output_file = open("{}".format(out_filename).read())

#expected
expected = 0






#closing sockets
receiver_in_socket.close()
receiver_out_socket.close()

#closing the file
#output_file.close()
