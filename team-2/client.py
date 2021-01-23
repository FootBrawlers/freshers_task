import socket

c=socket.socket()
Host1='192.168.1.101'
Port=9999
c.connect((Host1,Port))
msg=c.recv(64)
print(msg.decode('utf-8'))
colour=input()
c.send(bytes(colour,'utf-8'))
