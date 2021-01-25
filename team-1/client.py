import socket as soc

client = soc.socket()
client.connect((soc.gethostname(),8080))

while True:
    init_msg = client.recv(38)
    print(init_msg.decode("utf-8"))
    colour = str(input())
    if colour.lower() == 'exit' :
        break
    col_len = str(len(colour)).zfill(5)
    client.send(bytes(col_len,'utf-8'))
    client.send(bytes(colour,'utf-8'))
