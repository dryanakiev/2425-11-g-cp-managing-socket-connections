import socket
import threading


class Server:

    def __init__(self):
        self.client_socket = None
        self.server_address = '127.0.0.1'
        self.client_address = str
        self.server_port = 9999

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.server_socket.listen(10)

        try:
            print(f'Server started on {self.server_address}:{self.server_port}')
        except:
            print('Server failed to start...')
            return

        self.handle_client()

    def handle_client(self):

        self.accept_client()
        self.send_message("Welcome to our server!")

        receive_thread = threading.Thread(target=self.receive_message())

        receive_thread.start()
        receive_thread.join()

    def accept_client(self):
        self.client_socket, client_address = self.server_socket.accept()

        print(f'Client connected: {self.client_address}')

    def receive_message(self):
        while True:
            received_message = self.client_socket.recv(1024)
            print(received_message.decode())

    def send_message(self, message):
        while True:
            self.client_socket.send(message.encode())


server = Server()
