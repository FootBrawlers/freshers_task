import socket
s=socket.socket()
print("Socket Created")
Host1='192.168.1.101'
Port=9999
s.bind((Host1,Port))
s.listen(3)
print("Waiting for connection...")
while True:
    clientsocket,address=s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server, \nEnter the colour(R/G/B):",'utf-8'))
    colour=clientsocket.recv(10)
    colour=colour.decode('utf-8')
    print("\nColour entered is ",colour,". . . .")
    clientsocket.close()
