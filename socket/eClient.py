import socket 

s = socket.socket()

host = socket.gethostname()
port = 3003

s.connect((host,port))

data_recv = s.recv(1024)
print("Data received from server",data_recv)
s.send(data_recv)

s.close()
