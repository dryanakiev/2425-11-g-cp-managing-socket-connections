import socket
import threading

class Client:
    def __init__(self):
        self.server_address = '127.0.0.1'
        self.server_port = 9999
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client_socket.connect((self.server_address, self.server_port))
            print(f'Connection established to {self.server_address}:{self.server_port}')
        except Exception as e:
            print(f'Connection failed: {e}')
            return

        self.handle_server()

    def handle_server(self):
        send_thread = threading.Thread(target=self.send_message)
        receive_thread = threading.Thread(target=self.receive_message)

        send_thread.start()
        receive_thread.start()

        send_thread.join()
        receive_thread.join()

    def receive_message(self):
        while True:
            try:
                received_message = self.client_socket.recv(1024)
                if received_message:
                    print(f'\nServer: {received_message.decode()}')
                else:
                    print('Disconnected from server.')
                    self.client_socket.close()
                    break
            except:
                print('Error receiving message.')
                self.client_socket.close()
                break

    def send_message(self):
        while True:
            message_to_send = input("Enter message to send: ")
            if message_to_send.lower() == 'exit':
                self.client_socket.close()
                print("Disconnected from server.")
                break
            try:
                self.client_socket.send(message_to_send.encode())
            except:
                print("Failed to send message.")
                self.client_socket.close()
                break

client = Client()
