import socket

# make a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost',8000)

server_socket.bind(server_address)

server_socket.listen(1)

print('Server started and listenign for connections...')

while True:
    client_socket = None
    try:
        client_socket, client_address = server_socket.accept()
        print("Connection established with: ", client_address)
        response = "a"
        client_socket.send(response.encode())

        response = client_socket.recv(1024)
        print("Received response: " , response.decode())
    except KeyboardInterrupt:
        if client_socket:
            client_socket.close()
        break
    except socket.timeout:
        pass

server_socket.close()