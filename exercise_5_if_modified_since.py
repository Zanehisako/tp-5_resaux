
# Exercise: If-Modified-Since Header

import socket

# Connect to the server
server = "www.tcpipguide.com"
port = 80
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

# Send GET request with If-Modified-Since header
conn.sendall(b"GET /free/diagrams/tcpswunack.png HTTP/1.1\r\n"
             b"Host:www.tcpipguide.com\r\n"
             b"If-Modified-Since: Mon, 07 Jun 2005 00:26:52 GMT\r\n"
             b"Connection:close\r\n\r\n")

# Receive response
response = b""
while True:
    data = conn.recv(1024)
    if not data:
        break
    response += data

print(response.decode("unicode_escape"))
conn.close()
