
# Exercise: OPTIONS Request

import socket

# Connect to the server
server = "www.tcpipguide.com"
port = 80
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

# Send OPTIONS request
conn.sendall(b"OPTIONS / HTTP/1.1\r\nHost:www.tcpipguide.com\r\nConnection:close\r\n\r\n")

# Receive response
response = b""
while True:
    data = conn.recv(1024)
    if not data:
        break
    response += data

print(response.decode("unicode_escape"))
conn.close()
