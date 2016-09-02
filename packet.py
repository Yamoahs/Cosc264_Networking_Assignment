import struct

class Packet():
    def __init__(self, magicno, packet_type, seqno, dataLen, data):
        self.magicno = int(magicno)
        self.packet_type = packet_type
        self.seqno = seqno
        self.dataLen = dataLen
        self.data = data


    # def __str__(self):
    #     '''Returns all data in one string with the packet info at the head'''
    #     return "{}{}{}{}{}\\".format(str)
