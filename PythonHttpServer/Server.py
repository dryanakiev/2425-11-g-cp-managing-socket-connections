import socket

ip_address, port = 'localhost', 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen(5)

print(f"Server running on http://{ip_address}:{port}")

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print(f"Request received:\n{request}")

    # Define HTML response
    response = """HTTP/1.1 200 OK\nContent-Type: text/html\n\n
    <html>
    <head><title>Simple Python HTTP Server</title></head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a simple HTTP server in Python.</p>
    </body>
    </html>
    """

    client_connection.sendall(response.encode())
    client_connection.close()
