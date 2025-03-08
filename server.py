import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0",8080))
server_socket.listen(5)
print("listening on port 8080...")
while True:
    client_socket, client_ip = server_socket.accept()
    print(f"{client_ip} connected")
    client_socket.send(b"succesfully connected")
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            print(f"{client_ip} disconnected")
            break
        print(f"{client_ip}: {msg.decode()}")
    client_socket.close()
    