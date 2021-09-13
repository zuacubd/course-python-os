import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('www.irit.fr', 80)
sock.connect(server_address)

# req = "GET / HTTP/1.0\n\n"
