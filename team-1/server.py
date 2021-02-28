import socket as soc
from img_processor import *

def initiate_server():
    server = soc.socket()

    server.bind((soc.gethostname(),8080))
    server.listen(5)

    while True:
        clientsocket , address = server.accept()
        print(f"{address} has connected to the server!")
        while True:
            clientsocket.send(bytes("\nEnter the colour.\nTo exit enter exit.",'utf-8'))
            length = clientsocket.recv(5)
            if length == b'' :
                break
            msg = clientsocket.recv(int(length))
            msg = msg.decode("utf-8")
            if msg in [ "red", "green" , "blue" ] :
                print(f"\n{msg.capitalize()} has been entered.")
                for i in range(1,10):
                    colourModifier(msg,f"Sample_pics/{i}.jpg")
                # if you want to see the process in live using webcam
                # comment out the lines 22 & 23 and uncomment line 26
                    # live_colourModifier(msg)
            else: print("invalid colour..!")
        clientsocket.close()
        break

    print("\nThe task is done.")
