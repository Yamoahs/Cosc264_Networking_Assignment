#!/usr/bin/python
import packet
import os.path
import select
import socket
import struct
import sys

'''
Reciever.py
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

def create_ack_packet(rcvd_seqno):
    '''Function creates an acknowledge packet'''
    acknowledge_packet = packet.Packet_head(MAGICNO, PTYPE_ACK, rcvd_seqno, 0)
    head_in_bytes = acknowledge_packet.encoder()
    packet_buffer = bytearray(head_in_bytes)
    return packet_buffer


if len(args) == 5:
    if len(args) != len(set(args)):
        print("Duplicate Port Numbers")
        quit()
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            print("port {} not a valid port".format(port))
            quit()
    reciever_in_port = int(args[1])
    reciever_out_port = int(args[2])
    chan_recv_in_port = int(args[3])
    out_filename = str(args[4])

    #Opening output file
    if os.path.isfile(out_filename):
        print('File already exists')
    else:
        output_file = open(out_filename, "wb")
        stdin_successful = True

else:
    print("INPUT ERROR. Ports or File invalid")

#if stdin inputs are corerct begin socket initialisation
if stdin_successful:

    print("IN PORT: {}\nOUT PORT: {}\nCHAN RECV IN PORT: {}\nFILENAME: {}"\
    .format(reciever_in_port, reciever_out_port, chan_recv_in_port, out_filename))

    #Create the sockets
    try:
        receiver_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))
    try:
        receiver_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))

    #Bind the sockets
    try:
        receiver_in_socket.bind((HOST,reciever_in_port))
    except socket.error as e:
        print(str(e))
    try:
        receiver_out_socket.bind((HOST,reciever_out_port))
    except socket.error as e:
        print(str(e))

    #connect the socket
    try:
        receiver_out_socket.connect((HOST,chan_recv_in_port))
    except socket.error as e:
        print(str(e))

    #expected
    expected = 0

    recieved_data = False
    while not recieved_data:
            incoming_packet = receiver_in_socket.recv(1024)
            head = incoming_packet[:16]
            data = incoming_packet[16:]
            rcvd_magicno, rcvd_tpye, rcvd_seqno, rcvd_dataLen = \
            packet.decoder(head)

            if rcvd_magicno == MAGICNO and rcvd_tpye == PTYPE_DATA:
                if rcvd_seqno != expected:
                    packet_buffer = create_ack_packet(rcvd_seqno)
                    receiver_out_socket.send(packet_buffer)
                else:
                    packet_buffer = create_ack_packet(rcvd_seqno)
                    receiver_out_socket.send(packet_buffer)
                    expected = 1 - expected

                    if rcvd_dataLen > 0:
                        output_file.write(data)

                    else:
                        #closing sockets
                        receiver_in_socket.close()
                        receiver_out_socket.close()
                        recieved_data = True
                        print("Closing Sockets")

                        #closing the file
                        output_file.close()
