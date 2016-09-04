#!/usr/bin/python
import packet
import os.path
import select
import socket
import struct
import sys

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

DATA_SIZE = 512
MAGICNO = 0x497E
PTYPE_DATA = 0
PTYPE_ACK = 1
TIME_OUT = 1

def create_ack_packet(rcvd_seqno):
    acknowledge_packet = packet.Packet_head(MAGICNO, PTYPE_ACK, rcvd_seqno, 0)
    head_in_bytes = acknowledge_packet.encoder()
    packet_buffer = bytearray(head_in_bytes)
    return packet_buffer


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
        output_file = open(out_filename, "wb")
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

    recieved_data = False
    while not recieved_data:
        # ack = select.select([],[reciever_in_port], [], TIME_OUT)
        # if ack[1] != []:
            lolol = receiver_in_socket.recv(1024)
            head = lolol[:16]#receiver_in_socket.recv(16)
            data = lolol[16:]#receiver_in_socket.recv(1024)
            print("Data", data)
            rcvd_magicno, rcvd_tpye, rcvd_seqno, rcvd_dataLen = packet.decoder(head)

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


    #
    # print("From Sender head: ", head)
    # print(rcvd_magicno)
    # print(rcvd_tpye)
    # print(rcvd_seqno)
    # print(rcvd_dataLen)
    # print("From Sender data: ", data.decode('utf-8'))
    # data = "Back to ya sender"
    # receiver_out_socket.send(data.encode('utf-8'))
