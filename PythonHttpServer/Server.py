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
        method = request_lines[0].split(" ")[0]
        path = request_lines[0].split(" ")[1]
    else:
        method = "GET"
        path = "/"

    if method == "GET":
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

        elif path.startswith("/favicon"):
            file_name = path.lstrip("/")
            directory = "./assets/"
            content_type = "image/x-icon"

        else:
            file_name = None

        if path.startswith("/favicon"):
            file_content = open(f'{directory}{file_name}', 'br').read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n{len(file_content)}\r\nConnection: close\r\n\r\n"

        else:
            file_content = open(f'{directory}{file_name}', 'r').read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n{file_content}"

        client_connection.sendall(response.encode())

    elif method == "POST":
        body = request.split("\r\n\r\n")[1]
        data = {}
        for item in body.split("&"):
            key, value = item.split("=")
            data[key] = value

        email = data["email"]
        password = data["password"]
        password_repeat = data["password_repeat"]

        print(f"Data received {email}:{password}")

    client_connection.close()
