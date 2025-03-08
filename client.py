import socket

server_ip = input("server ip: ")
server_port = int(input("server port: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
recive = client_socket.recv(1024).decode()
if recive == "succesfully connected":
    while True:
        msg = input("send something: ")
        if msg.lower() == "exit":
            print("Closing connection.")
            break
        client_socket.sendall(msg.encode())
else:
    print("connection failed")