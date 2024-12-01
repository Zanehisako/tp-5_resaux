
# Exercise: Download Content over HTTPS

import socket
import ssl

# Connect to the server
server = "www.coursera.org"
port = 443
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

# Wrap socket with SSL
ssl_conn = ssl.create_default_context().wrap_socket(conn, server_hostname=server)

# Send GET request
ssl_conn.sendall(b"GET /api/certificate.v1/pdf/HDC2GWUR3YT4 HTTP/1.1\r\n"
                 b"Host:www.coursera.org\r\n"
                 b"Connection:close\r\n\r\n")

# Receive response and save file
response = b""
while True:
    data = ssl_conn.recv(1024)
    if not data:
        break
    response += data

# Separate headers and content
header_end = response.find(b"\r\n\r\n") + 4
file_content = response[header_end:]

# Write content to a file
with open("fichier.pdf", "wb") as file:
    file.write(file_content)

ssl_conn.close()
