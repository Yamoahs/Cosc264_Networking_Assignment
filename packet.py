import struct

class Packet():

    def __init__(self, magicno, packet_type, seqno, dataLen, data):
        self.magicno = int(magicno)
        self.packet_type = int(packet_type)
        self.seqno = int(seqno)
        self.dataLen = int(dataLen)
        self.data = data
        self.packet_format = "iiii"


    def encoder(self):
        encoded = struct.pack(self.packet_format, self.magicno, self.packet_type, self.seqno, self.dataLen)
        return encoded


    def decoder(self, output):
        decoded = struct.unpack(self.packet_format, output)
        return decoded


new_packet = Packet(1,2,3,4,None)
byte = new_packet.encoder()
print(byte)
w,x,y,z = new_packet.decoder(byte)
print(w)
print(x)
print(y)
print(z)
