#coding:utf-8

import sys, socket

host = sys.argv[1]
filename = sys.argv[2]
port = 70

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall((filename + '\r\n').encode())

while 1:
	buf = s.recv(2048)
	if not len(buf):
		break

	print(buf.decode())




