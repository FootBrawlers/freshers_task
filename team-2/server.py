
import socket

PORT = 9999
s=socket.socket()
print("Socket Created")
s.bind((socket.gethostname(), PORT))
s.listen(3)
print("Waiting for connection...")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server, \nHappy to see you here...", 'utf-8'))
    color = 'Red'
    clientsocket.send(bytes(color, 'utf-8'))
    break
clientsocket.close()
