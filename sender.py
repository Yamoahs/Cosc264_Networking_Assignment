import socket

'''
Sender Sockets: s_in and s_out

'''
s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_in.connect(("localhost", 1234))

data = "hello server"
s_in.send(data.encode('utf-8'))
data = s_in.recv(512)
print("From Reciever: ", data.decode('utf-8'))

s_in.close()
