import socket
import threading

# Function to handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Receive and print the prompt for username
print(client.recv(1024).decode('utf-8'))
# Send username to the server
username = input()
client.send(username.encode('utf-8'))

print("Connected to the server. You can start sending messages.")

# Start a thread to receive messages
threading.Thread(target=receive_messages, args=(client,)).start()

# Send messages in an infinite loop
while True:
    message = input()
    client.send(message.encode('utf-8'))
