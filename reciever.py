import socket

r_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

r_in.bind(("", 1234))

r_in.listen(5)

r_in, address = r_in.accept()

data = r_in.recv(512)
print("From Sender: ", data.decode('utf-8'))
data = "Back to ya sender"
r_in.send(data.encode('utf-8'))

r_in.close()
