
# Import the libraries
import socket
import threading
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(key)

# Define the host and port for the server
host = "127.0.0.1"
port = 55555

# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Define a function to handle the client connections
def handle_client(client):
    # Receive the message from the client
    message = client.recv(1024)
    # Decrypt the message using the key
    decrypted_message = f.decrypt(message)
    client.sendall(message)
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
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Create a socket object for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a function to run the client
def run_client():
    # Connect to the server
    client.connect((host, port))
    # Print a message to indicate that the client is connected
    print(f"Connected to {host}:{port}")
    # Prompt the user to enter a message to send to the server
    message = input("Enter a message: ")
    # Encrypt the message using the key
    encrypted_message = f.encrypt(message.encode())
    # Send the encrypted message to the server
    client.send(encrypted_message)
    # Print a message to indicate that the message was sent
    print("Message sent")

# Run the server and the client in separate threads
server_thread = threading.Thread(target=run_server)
client_thread = threading.Thread(target=run_client)
server_thread.start()
client_thread.start()
