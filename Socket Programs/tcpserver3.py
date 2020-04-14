#!/usr/bin/python3 

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# socket.socket() creates a socket object that supports the context manager type, 
# so you can use it in a with statement. There’s no need to call s.close():

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    # One thing that’s imperative to understand is that we now have a new socket object from accept(). 
    # This is important since it’s the socket that you’ll use to communicate with the client. 
    # It’s distinct from the listening socket that the server is using to accept new connections:

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
