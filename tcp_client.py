#!/usr/bin/python2.7

import socket

target_host = "www.basenet.nl"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\r\nHost: basenet.nl\r\n\r\n")

response = client.recv(4096)

print response
