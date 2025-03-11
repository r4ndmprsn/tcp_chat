import socket
import threading

def server_connection(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    recive = client_socket.recv(1024).decode()
    if recive == "succesfully connected":
        print(recive)
        recive_thread = threading.Thread(target=recive_messages, args=(client_socket,), daemon=True)
        recive_thread.start()
        while True:
            msg = input()
            if msg.lower() == "exit":
                print("Closing connection.")
                break
            client_socket.sendall(msg.encode())
    else:
        print("connection failed")

def recive_messages(client_socket):
    while True:
        rcv_msg = client_socket.recv(1024).decode()
        if not rcv_msg:
            break
        print(rcv_msg)
if __name__ == "__main__":
    server_ip = input("server ip: ")
    server_port = int(input("server port: "))
    server_connection(server_ip, server_port)
