import socket
import threading

usernames = {}
clients = []
def client_connection(client_socket, client_ip):
    global usernames
    client_socket.send(b"succesfully connected")
    waiting_room(client_socket, client_ip)
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            print(f"{usernames[client_ip]} disconnected")
            break
        print(f"{usernames[client_ip]}: {msg.decode()}")
        message = f"{usernames[client_ip]}: {msg.decode()}"
        send_to_all(message, client_socket)
    client_socket.close()

def waiting_room(client_socket, client_ip):
    guard = 1
    while True:
        client_socket.send(b"insert username")
        username = client_socket.recv(1024).decode()
        for user in usernames:
            if username ==  user:
                guard = 0
        if guard == 1:
            break
        else:
            print("this username is taken")
    usernames[client_ip] = username
    print(f"{usernames[client_ip]} connected")
    

def send_to_all(msg, client_socket):
    for client in clients:
        if client != client_socket:
            client.sendall(msg.encode())

def run_server(server_ip = "0.0.0.0", server_port = 8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip,server_port))
    server_socket.listen(5)
    print(f"listening on port {server_port}...")

    while True:
        client_socket, client_ip = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=client_connection, args=(client_socket, client_ip))
        client_thread.start()

if __name__ == "__main__":
    run_server()
    
