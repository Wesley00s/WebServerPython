import socket
import threading

bind_ip = '192.168.1.135'
bind_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print(f'\n[*]Server running on {bind_ip}:{bind_port}\n')


def handle_client(client_socket):
    path = '/home/wesley/PycharmProjects/WebServer/resources'

    request = client_socket.recv(1024)
    print(f'[*]Received: {request.decode()}')

    try:
        requested_resource = request.decode().split(' ')[1]

        if requested_resource == '/':
            requested_resource = '/index.html'

        with open(path + requested_resource, 'rb') as f:
            content = f.read()

            content_type = 'text/html' if requested_resource.endswith(
                '.html') else 'image/jpeg' if requested_resource.endswith('.jpg') else 'text/plain'
            response_headers = f"HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n"
            client_socket.send(response_headers.encode('utf-8'))
            client_socket.send(content)

    except FileNotFoundError:
        error_message = "HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n<h1>404 Not Found</h1>"
        client_socket.send(error_message.encode('utf-8'))

    client_socket.close()


while True:
    client, addr = server.accept()
    print(f'[*]Accepted from: {addr[0]}: {addr[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()




