# Socket programming 
# Db access 
# sys os 

# response = requests.get("wwww.zekelabs.com")

# Server listen  => ip port no 80 => server socket in listening mode

# Client => ip 80 => socket 80 => connect 


# http : 80 
# smtp : 25

# endpoint 

# Server :
# ip port

# bind(ip,port)
# listen
# accept 
# send/recv => bytes  TCP = > connection oriented 3 way handshake to cleint to server client   
# 					or UDP  => conection less  DNS 



# Client :

# ip port 
# connect 
# send/recv 


import socket

s = socket.socket()

# gethostname => localhost 
# gethostbyname => www.zekelabs.com
# getfqdn > ip 

host = socket.gethostname()
port = 3003

s.bind((host,port))
s.listen(1)

client_sock,addr = s.accept()
data_send = "this is the data from server".encode()
client_sock.send(data_send)

data_recv = client_sock.recv(1024)

if data_send == data_recv :
	print("Hanshaking successful")
else:
	print("Invalid data")

s.close()
# send(byte)
# sendall()
# recv(no_bytes)
