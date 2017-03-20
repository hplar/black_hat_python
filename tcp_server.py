#!/usr/bin/python2.7

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to ip/port and listen
server.bind((bind_ip, bind_port))
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)


# thread for client-handling
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    # send back ACK
    client_socket.send("ACK!")

    # close socket/thread
    client_socket.close()


while True:

    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # spin up client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()

