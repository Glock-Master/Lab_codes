import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7777
s.bind(('', port))
print('Server socket binded to port:', port)
s.listen(5);

print("Now listening")

while True:
	c, addr = s.accept()
	print("Connected to:", addr)
	
	data = c.recv(1024)
	a, b = data.decode().split()
	a = int(a)
	b = int(b)
	c.send(str(a + b).encode())
	c.close()
