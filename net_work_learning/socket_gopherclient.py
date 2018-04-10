#coding:utf-8

import sys, socket

# host = sys.argv[1]
# filename = sys.argv[2]
# port = 70
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# try:
# 	s.connect((host, port))
# except :
# 	print(e)
# s.sendall((filename + '\r\n').encode())
#
# while 1:
# 	buf = s.recv(2048)
# 	if not len(buf):
# 		break
#
# 	print(buf.decode())



class B(Exception):
	pass

class C(B):
	pass

class D(C):
	pass


for cls in [B, C, D]:

	try:
		raise  cls()
	except D:
		print("d")

	except C:
		print("c")

	except B:
		print("b")



a = 1/0

try:
	pass
except ZeroDivisionError as e:
	print(e.args)
	print(e)
	print(type(e))
	x, y = e.args
	print(x)
	print(y)




