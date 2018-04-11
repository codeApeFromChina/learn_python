import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = socket.getservbyname('http', 'tcp')
print(port)
s.connect(("taobao.com", port))


try:
    pass
except socket.gaierror:
    pass
