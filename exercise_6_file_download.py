
# Exercise: Download File

import socket

# Connect to the server
server = "www.tcpipguide.com"
port = 80
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

# Send GET request for file
conn.sendall(b"GET /free/diagrams/tcpswunack.png HTTP/1.1\r\n"
             b"Host:www.tcpipguide.com\r\n"
             b"Connection:close\r\n\r\n")

# Receive response and save file
response = b""
while True:
    data = conn.recv(1024)
    if not data:
        break
    response += data

# Separate headers and content
header_end = response.find(b"\r\n\r\n") + 4
file_content = response[header_end:]

# Write content to a file
with open("tcpswunack.png", "wb") as file:
    file.write(file_content)

conn.close()
