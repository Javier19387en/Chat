import socket
import threading
import hashlib
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")

def handle_client(client_socket, client_address,datos):
    while True:
        # Recibir datos del cliente
        encrypted_data = client_socket.recv(1024)
        if not encrypted_data:
            break
        
        # Desencriptar los datos recibidos
        decrypted_data = f.decrypt(encrypted_data)
        print(f"Mensaje recibido del cliente {client_address}: {decrypted_data.decode()}")
        for mensages in datos:
            #mensages[0][0].sendall(encrypted_data)
            print(type(mensages))
            mensages.sendall(encrypted_data)
        # Enviar una respuesta encriptada al cliente
        #response = "¡Mensaje recibido y procesado correctamente!"
        #encrypted_response = f.encrypt(response.encode())
        #client_socket.send(encrypted_data)
    
    # Cerrar la conexión con el cliente
    client_socket.close()
datos=[]
def start_server():
    # Configurar el servidor
    host = '0.0.0.0'
    port = 8000

    # Crear el socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor escuchando en {host}:{port}")
    while True:
        # Aceptar conexiones entrantes
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado desde {client_address[0]}:{client_address[1]}")
        datos.append(client_socket)
        # Iniciar un hilo para manejar al cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address,datos))
        client_thread.start()

# Iniciar el servidor
start_server()
