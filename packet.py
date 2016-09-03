import struct

class Packet_head():

    def __init__(self, magicno, packet_type, seqno, dataLen):
        self.magicno = int(magicno)
        self.packet_type = int(packet_type)
        self.seqno = int(seqno)
        self.dataLen = int(dataLen)
        self.packet_format = "iiii"


    def encoder(self):
        encoded = struct.pack(self.packet_format, self.magicno, self.packet_type, self.seqno, self.dataLen)
        return encoded



def decoder(output):
    packet_format = "iiii"
    decoded = struct.unpack(packet_format, output)
    return decoded

# new_packet = Packet_head(1,2,3,10)
# byte = new_packet.encoder()
# print(byte)
# w,x,y,z = new_packet.decoder(byte)
# print(w)
# print(x)
# print(y)
# print(z)
# yo = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\n\x00\x00\x00'
# a,b,c,d = decoder2(yo)
# print(a)
# print(b)
# print(c)
# print(d)
