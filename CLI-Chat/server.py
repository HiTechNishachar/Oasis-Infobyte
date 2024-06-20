import socket
import threading

# Function to handle client connections
def handle_client(client_socket, clients, usernames):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                username = usernames[client_socket]
                broadcast(f"{username}: {message}", client_socket, clients)
            else:
                remove_client(client_socket, clients, usernames)
                break
        except:
            continue

# Function to broadcast messages to all clients
def broadcast(message, connection, clients):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client, clients, usernames)

# Function to remove a client
def remove_client(connection, clients, usernames):
    if connection in clients:
        clients.remove(connection)
        del usernames[connection]

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)
clients = []
usernames = {}

print("Server started, waiting for connections...")

# Accept connections in an infinite loop
while True:
    client_socket, addr = server.accept()
    print(f"Connection established with {addr}")

    # Prompt for and store the username
    client_socket.send("Enter your username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    usernames[client_socket] = username
    clients.append(client_socket)

    print(f"{username} has joined the chat.")

    # Start a new thread to handle the client
    threading.Thread(target=handle_client, args=(client_socket, clients, usernames)).start()
