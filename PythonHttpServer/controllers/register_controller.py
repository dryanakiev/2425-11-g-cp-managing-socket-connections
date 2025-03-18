def handle_register(method,request):
    if method == "GET":
        return on_get()
    elif method == "POST":
        return on_post(request)
    else:
        return ""

def on_get():
    try:
        with open("./pages/register.html", "r") as file:
            content = file.read()
        return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{content}"
    except FileNotFoundError:
        return "HTTP/1.1 404 Not Found\r\n\r\nPage not found"

def on_post(request): # TODO: Fix data transfer and index out of range
    fields = {item.split("=")[0]: item.split("=")[1] for item in request.split("&")}
    email = fields.get("email", "")
    password = fields.get("password", "")
    print(f"Received registration: {email}:{password}")
    return "HTTP/1.1 200 OK\r\n\r\nRegistration successful"
