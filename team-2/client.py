def client_socket():
    import socket

    PORT = 9999
    c=socket.socket()
    c.connect((socket.gethostname(), PORT))
    msg = c.recv(64)
    print(msg.decode('utf-8'))
    color = c.recv(10)
    color = color.decode('utf-8')
    return color
