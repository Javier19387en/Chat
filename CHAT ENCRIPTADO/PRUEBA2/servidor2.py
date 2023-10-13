
# Import the libraries
import socket
import threading
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")

# Define the host and port for the server
host = "127.0.0.1"
port = 55555

# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Define a function to handle the client connections
def handle_client(client,server):
    # Receive the message from the client
    message = client.recv(1024)
    # Decrypt the message using the key
    decrypted_message = f.decrypt(message)
    server.sendall(message)
    # Print the message in the server console
    print(f"Received message: {decrypted_message.decode()}")
    # Close the connection with the client
    client.close()

# Define a function to run the server
def run_server():
    # Print a message to indicate that the server is running
    print(f"Server is listening on {host}:{port}")
    # Accept incoming connections from clients
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        # Create a thread to handle each client
        thread = threading.Thread(target=handle_client, args=(client,server))
        thread.start()

# Create a socket object for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_thread = threading.Thread(target=run_server)
server_thread.start()
