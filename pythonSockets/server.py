import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()

print(f'Client connected: {client_address}')

while True:
    received_message = client_socket.recv(1024)

    print(f'Client sent: {received_message.decode()}')

    client_socket.send(received_message)