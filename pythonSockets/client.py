import socket
import threading

class Client:
    def __init__(self):
        self.client_socket = None
        self.server_address = '127.0.0.1'
        self.server_port = 9999

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address,self.server_port))

        if self.client_socket:
            print(f'Connection established to {self.server_address} {self.server_port}')

        self.handle_server()

    def handle_server(self):

        print(self.receive_message())

        send_thread = threading.Thread(target=self.send_message())
        receive_thread = threading.Thread(target=self.receive_message())

        send_thread.start()
        receive_thread.start()
        send_thread.join()
        receive_thread.join()


    def receive_message(self):
        while True:
            received_message = self.client_socket.recv(1024)
            print(received_message.decode())

    def send_message(self):
        while True:
            message_to_send = input('Enter your message: ')
            self.client_socket.send(message_to_send.encode())

client = Client()