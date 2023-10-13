
# Import the libraries
import socket
import threading
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")

# Define the host and port for the server
#host = "127.0.0.1"
host = "localhost"
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a function to run the client
def run_client():
    print("clave de encriptacion: ",key)
    client.connect((host, port))
    print(f"Connected to {host}:{port}")
    PERMANENCIA=True
    EXIT=False
    while PERMANENCIA:
        if EXIT==True:
            # Cierra la conexión
            client.close()
            PERMANENCIA=False
        MSG=""
        print("INGRESE UN MENSAGE")
        MSG=input()
        if MSG=="exit":EXIT=True
        if MSG!="":
            encrypted_message = f.encrypt(MSG.encode())
            client.send(encrypted_message)
            response = client.recv(1024).decode()
            print("b>"+response)
            print(f.decrypt(response))
run_client()