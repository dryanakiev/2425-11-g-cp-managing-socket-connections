import socket
from controllers.index_controller import handle_index
from controllers.about_controller import handle_about
from controllers.contact_controller import handle_contact
from controllers.register_controller import handle_register

def handle_request(request):
    request_lines = request.split("\n")

    if len(request_lines) > 0 and " " in request_lines[0]:
        method, path = request_lines[0].split(" ")[:2]
    else:
        method, path = "GET", "/"

    if path == "/":
        response = handle_index(method)
    elif path == "/about":
        response = handle_about(method)
    elif path == "/contact":
        response = handle_contact(method)
    elif path == "/register":
        response = handle_register(method, request)
    elif path.startswith("/styles/"):
        file_name = path.lstrip("/")
        directory = "./"
        content_type = "text/css"
        file_content = open(f'{directory}{file_name}', 'r').read()
        response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n{file_content}"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\nPage not found"

    return response
