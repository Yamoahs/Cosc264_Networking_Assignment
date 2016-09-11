import struct

'''
Packet.py
Samuel Yamoah & Sarang Leehan 2016
'''

class Packet_head():
    '''Class Builds a Packet with the Magicno, packet type, seqno and Data len
    as the head and the data is added as the payload'''

    def __init__(self, magicno, packet_type, seqno, dataLen):
        self.magicno = int(magicno)
        self.packet_type = int(packet_type)
        self.seqno = int(seqno)
        self.dataLen = int(dataLen)
        self.packet_format = "iiii"


    def encoder(self):
        '''Converts raw input head into byte form'''
        encoded = struct.pack(self.packet_format, self.magicno, \
        self.packet_type, self.seqno, self.dataLen)
        return encoded



def decoder(output):
    '''Converts pack head from bytes to raw input'''
    packet_format = "iiii"
    decoded = struct.unpack(packet_format, output)
    return decoded
