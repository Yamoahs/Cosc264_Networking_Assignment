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
if len(args) == 5:
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            #HAVE A TRY EXCEPTION
            print("port {} not a valid port".format(port))
    reciever_in_port = int(args[1])
    reciever_out_port = int(args[2])
    reciever_sender_in = int(args[3])
    filename = str(args[4])

    print("IN PORT: {}\nOUT PORT: {}\n\
reciever_sender_in PORT: {}\nFILENAME: {}".format(sender_in_port, \
     sender_out_port, reciever_sender_in, filename))

else:
    print("Input ERROR")
