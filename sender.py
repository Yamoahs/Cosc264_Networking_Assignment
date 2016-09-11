#!/usr/bin/python
import packet
import os.path
import select
import socket
import struct
import sys

'''
Sender.py
Samuel Yamoah & Sarang Leehan 2016
'''

#IP address
HOST =  "127.0.0.1"

#valid Port no.
VALID_PORTS =  range(1024, 64001)

# Get the arguments list
args = (sys.argv)

#Flag to make sure stdin arguemtents
stdin_successful = False

#Data size in bytes
DATA_SIZE = 512
#Magic Number
MAGICNO = 0x497E
#Packet types
PTYPE_DATA = 0
PTYPE_ACK = 1

TIME_OUT = 1

sent_packets = 0

if len(args) == 5:
    if len(args) != len(set(args)):
        print("Duplicate Port Numbers")
        quit()
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            print("port {} not a valid port".format(port))
            quit()
    sender_in_port = int(args[1])
    sender_out_port = int(args[2])
    chan_send_in_port = int(args[3])
    filename = str(args[4])

    #Checking if input file exists
    if os.path.isfile(filename):
        #Open File in byte mode
        input_file = open(filename, 'rb')
        stdin_successful = True
    else:
        print('File does not exists')

else:
    print("INPUT ERROR. Ports or File invalid")

#if stdin inputs are corerct begin socket initialisation
if stdin_successful:

    print("IN PORT: {}\nOUT PORT: {}\CHAN SENDER IN PORT: {}\nFILENAME: {}"\
    .format(sender_in_port, sender_out_port, chan_send_in_port, filename))


    #Create the sockets
    try:
        sender_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))
    try:
        sender_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))

    #Bind the sockets
    try:
        sender_in_socket.bind((HOST,sender_in_port))
    except socket.error as e:
        print(str(e))
    try:
        sender_out_socket.bind((HOST,sender_out_port))
    except socket.error as e:
        print(str(e))

    #Connect the sockets
    try:
        sender_out_socket.connect((HOST,chan_send_in_port))
    except socket.error as e:
        print(str(e))

    next_ = 0
    exist_flag = False

    while not exist_flag:
        data = input_file.read(DATA_SIZE)
        data_len = len(data)
        if data_len == 0:
            data_packet = packet.Packet_head(MAGICNO, PTYPE_DATA, next_, \
            data_len)
            head_in_bytes = data_packet.encoder()
            exist_flag = True

        else:
            data_packet = packet.Packet_head(MAGICNO, PTYPE_DATA,next_, \
             data_len)
            head_in_bytes = data_packet.encoder()

        #Setting the Packet Buffer
        packet_buffer = bytearray(head_in_bytes + data)



        recieved_packet = False
        while not recieved_packet:
            sender_out_socket.send(packet_buffer)
            sent_packets += 1
            print(sent_packets)

            ack = select.select([sender_in_socket], [], [], TIME_OUT)
            if ack[0] != []:
                rcvd = sender_in_socket.recv(1024)
                rcvd_magicno, rcvd_tpye, rcvd_seqno, rcvd_dataLen = \
                packet.decoder(rcvd)

                if rcvd_magicno == MAGICNO and rcvd_tpye == PTYPE_ACK\
                 and rcvd_dataLen == 0 and rcvd_seqno == next_:
                    next_ = 1 - next_
                    recieved_packet = True

    #Closing the Sockets
    sender_out_socket.close()
    sender_in_socket.close()

    #closing the file
    input_file.close()
    print("Packets Sent:", sent_packets)
