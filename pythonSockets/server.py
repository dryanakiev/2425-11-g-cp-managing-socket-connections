import socket
import threading

class Server:

    def __init__(self):
        self.server_address = '127.0.0.1'
        self.server_port = 9999
        self.clients = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.server_socket.listen(10)

        try:
            print(f'Server started on {self.server_address}:{self.server_port}')
        except:
            print('Server failed to start...')
            return

        self.accept_clients()

    def accept_clients(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f'Client connected: {client_address}')

            # Send welcome message
            client_socket.send("Welcome to our server!".encode())

            # Start a thread for each client
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

    def handle_client(self, client_socket, client_address):
        while True:
            try:
                received_message = client_socket.recv(1024)
                if received_message:
                    message = received_message.decode()
                    print(f'Message from {client_address}: {message}')
                    self.broadcast(message, client_socket, client_address)
                else:
                    print(f'Client {client_address} disconnected.')
                    self.clients.remove(client_socket)
                    client_socket.close()
                    break
            except:
                print(f'Error with client {client_address}')
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, sender_socket, sender_address):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(f'{sender_address} sent: {message}'.encode())
                except:
                    self.clients.remove(client)
                    client.close()

server = Server()