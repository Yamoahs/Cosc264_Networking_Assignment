#!/usr/bin/python
import os.path
import packet
import random
import select
import socket
import struct
import sys

'''
channel.py
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

MAGICNO = 0x497E

def packet_check(recv_packet):
    '''Function decodes the packet head'''
    head = recv_packet[:16]
    decoded = packet.decoder(head)
    return decoded

if len(args) == 8:
    if len(args) != len(set(args)):
        print("Duplicate Port Numbers")
        quit()
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            print("port {} not a valid port".format(port))
            quit()
    if float(args[7]) < 0 or float(args[7]) >= 1:
        print("Invalid Prob")
        quit()

    chan_send_in_port = int(args[1])
    chan_send_out_port = int(args[2])
    chan_recv_in_port = int(args[3])
    chan_recv_out_port = int(args[4])
    sender_in_port = int(args[5])
    reciever_in_port = int(args[6])
    packet_loss_rate = float(args[7])
    stdin_successful = True


else:
    print("INPUT ERROR. Ports or File invalid")

if stdin_successful:
    print("CS IN PORT: {}\nCS OUT PORT: {}\nCR IN PORT: {}\nCR OUT PORT: {}\n\
SENDER IN PORT: {}\nRECIEVER IN PORT: {}\nLOSS RATE: {}".format(chan_send_in_port,\
 chan_send_out_port, chan_recv_in_port, chan_recv_out_port,\
 sender_in_port,reciever_in_port, packet_loss_rate))


    #Create the sockets
    chan_send_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    chan_send_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    chan_recv_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    chan_recv_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Bind the Sockets
    chan_send_in_socket.bind((HOST,chan_send_in_port))
    chan_send_out_socket.bind((HOST,chan_send_out_port))
    chan_recv_in_socket.bind((HOST,chan_recv_in_port))
    chan_recv_out_socket.bind((HOST,chan_recv_out_port))

    #Connect the sockets
    chan_send_out_socket.connect((HOST,sender_in_port))
    chan_recv_out_socket.connect((HOST,reciever_in_port))

    while True:

        #Blocking Calls
        read = select.select([chan_send_in_socket, chan_recv_in_socket], [], [])

        if chan_send_in_socket in read[0]:
            rcvd_packet = chan_send_in_socket.recv(1024)
            decoded = packet_check(rcvd_packet)
            # rcvd_magicno, rcvd_tpye, rcvd_seqno, rcvd_dataLen = packet.decoder(head)

            if decoded[0] == MAGICNO:
                probability = random.random() < packet_loss_rate
                if not probability:
                    chan_recv_out_socket.send(rcvd_packet)

        if chan_recv_in_socket in read[0]:
            rcvd_packet = chan_recv_in_socket.recv(1024)
            decoded = packet_check(rcvd_packet)

            if decoded[0] == MAGICNO:
                probability = random.random() < packet_loss_rate
                if not probability:
                    chan_send_out_socket.send(rcvd_packet)
