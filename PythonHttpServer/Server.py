import socket

ip_address, port = 'localhost', 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen(5)

print(f"Server running on http://{ip_address}:{port}")

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode().strip()

    if not request:
        client_connection.close()
        continue

    print(f"Request received:\n{request}")

    request_lines = request.split("\n")

    if len(request_lines) > 0 and " " in request_lines[0]:
        path = request_lines[0].split(" ")[1]
    else:
        path = "/"

    if path == "/":
        file_name = "index.html"
        directory = "./pages/"
        content_type = "text/html"

    elif path == "/about":
        file_name = "about.html"
        directory = "./pages/"
        content_type = "text/html"

    elif path == "/contact":
        file_name = "contact.html"
        directory = "./pages/"
        content_type = "text/html"

    elif path == "/register":
        file_name = "register.html"
        directory = "./pages/"
        content_type = "text/html"

    elif path.startswith("/styles/"):
        file_name = path.lstrip("/")
        directory = "./"
        content_type = "text/css"
    else:
        file_name = None

    file_content = open(f'{directory}{file_name}', 'r').read()
    response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n{file_content}"

    client_connection.sendall(response.encode())
    client_connection.close()
