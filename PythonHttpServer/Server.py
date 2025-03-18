import socket
from controllers.server_controller import handle_request

ip_address, port = 'localhost', 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen(5)

print(f'Server running on http://{ip_address}:{port}')

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode().strip()

    if not request:
        client_connection.close()
        continue

    print(f"Request received:\n{request}")

    response = handle_request(request)
    client_connection.sendall(response.encode())
    client_connection.close()

