import socket
import threading

import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")

def handle_client(client_socket,serv):
    while True:
        # Recibir datos del cliente
        data = client_socket.recv(1024)
        if not data:
            break
        
        # Enviar los datos recibidos a todos los clientes conectados
        for client in clients:
            serv.send(data)
    
    # Cerrar la conexión con el cliente
    client_socket.close()

def start_server():
    # Configurar el servidor
    host = '127.0.0.1'
    port = 8000

    # Crear el socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        # Aceptar conexiones entrantes
        client_socket, addr = server_socket.accept()
        print(f"Cliente conectado desde {addr[0]}:{addr[1]}")

        # Iniciar un hilo para manejar al cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,server_socket))
        client_thread.start()

# Lista para almacenar los clientes conectados
clients = []

# Iniciar el servidor
start_server()
