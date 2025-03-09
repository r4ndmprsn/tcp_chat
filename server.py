import socket
import threading

usernames = {}
usernamescount = 0
def client_connection(client_socket, client_ip):
    global usernames
    global usernamescount
    usernamescount+=1
    usernames[client_ip] = f"user{usernamescount}"
    print(f"{usernames[client_ip]} connected")
    client_socket.send(b"succesfully connected")
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            print(f"{usernames[client_ip]} disconnected")
            break
        print(f"{usernames[client_ip]}: {msg.decode()}")
    client_socket.close()
def run_server(server_ip = "0.0.0.0", server_port = 8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip,server_port))
    server_socket.listen(5)
    print(f"listening on port {server_port}...")

    while True:
        client_socket, client_ip = server_socket.accept()
        client_thread = threading.Thread(target=client_connection, args=(client_socket, client_ip))
        client_thread.start()

if __name__ == "__main__":
    run_server()
    
