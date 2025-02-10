import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

if client_socket:
    print('Connection established!')

while True:
    outgoing_message = input('Enter your message: ')

    client_socket.send(outgoing_message.encode())

    print(f'Server received: {client_socket.recv(1024).decode()}')