#!/usr/bin/python2.7

import socket

target_host = "127.0.0.1"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data through socket
client.sendto("AAABBBCCC", (target_host, target_port))

# receive data through socket
data, addr = client.recvfrom(4096)

print "data: %s\nAddr: %s" % (data, addr)
