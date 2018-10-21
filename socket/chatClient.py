import socket 

s = socket.socket()

host = socket.gethostname()
port = 3003

s.connect((host,port))

while(True):
	data_recv = s.recv(1024)
	print("Data received from server",data_recv)
	data_send = input("Enter the data for Server")
	s.send(data_send.encode())

	c = input("Do you want to continue (y/n)")
	if c =="n":
		break

s.close()
