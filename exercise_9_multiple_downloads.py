
# Exercise: Multiple Downloads

import socket

def download_resources(conn, server_name, resources, filenames):
    for resource, filename in zip(resources, filenames):
        # Send GET request
        conn.sendall(f"GET {resource} HTTP/1.1\r\nHost:{server_name}\r\nConnection: keep-alive\r\n\r\n".encode())

        # Receive response
        response = b""
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response += data

        # Separate headers and content
        header_end = response.find(b"\r\n\r\n") + 4
        file_content = response[header_end:]

        # Write content to file
        with open(filename, "wb") as file:
            file.write(file_content)

# Connect to the server
server = "www.tcpipguide.com"
port = 80
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

# Resources and filenames
resources = ["/free/diagrams/osinotation.png", "/free/diagrams/tcpswunack.png"]
filenames = ["test.png", "test2.png"]

# Download resources
download_resources(conn, server, resources, filenames)

conn.close()
