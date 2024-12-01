
# Exercise: HTTP Cookies

import socket

# Start a simple HTTP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 80))
server_socket.listen(30)

content = "<h1>Page HTML</h1>"
cookie_value = input("Enter the value for 'votre_cookie': ")
header = f"HTTP/1.1 200 OK\r\nConnection: close\r\nSet-Cookie: {cookie_value}\r\nContent-Length: {len(content)}\r\n\r\n"

while True:
    client_socket, _ = server_socket.accept()
    client_socket.send(header.encode() + content.encode())
    client_socket.close()
