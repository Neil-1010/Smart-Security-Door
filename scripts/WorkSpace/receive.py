import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',8000)
client_socket.connect(server_address)

# while True:
start = time.time()
for i in range(32):
    response = "A"
    client_socket.send(response.encode())
    client_socket.send(response.encode())
    client_socket.send(response.encode())
    client_socket.send(response.encode())
    client_socket.send(response.encode())
    client_socket.send(response.encode())
    client_socket.send(response.encode())
print(time.time() - start)


client_socket.close()
    # print("Received response: " , response.decode())
client_socket.close()