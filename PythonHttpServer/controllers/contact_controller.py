def handle_contact(method):
    if method == "GET":
        return on_get()
    elif method == "POST":
        return on_post()
    else:
        return ""

def on_get():
    try:
        with open("./pages/contact.html", "r") as file:
            content = file.read()
        return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{content}"
    except FileNotFoundError:
        return "HTTP/1.1 404 Not Found\r\n\r\nPage not found"

def on_post():
    return "HTTP/1.1 200 OK\r\n\r\nContact form submitted"
