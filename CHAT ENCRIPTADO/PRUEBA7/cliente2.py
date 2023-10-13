import socket
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 55555

# Conectar al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("Cliente 2: ")
    client.send(f.encrypt(message.encode('utf-8')))
    respuesta = client.recv(4096)
    print(f"Respuesta del servidor: {(f.decrypt(respuesta)).decode('utf-8')}")