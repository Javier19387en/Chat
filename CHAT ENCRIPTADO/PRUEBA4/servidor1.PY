import socket
import threading
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")


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
        encrypted_data = client_socket.recv(2048)
        if not encrypted_data:
            break
        else:
            # Desencriptar los datos recibidos
            decrypted_data = f.decrypt(encrypted_data)
            respuesta=f"mensaje recivide {client_address[0]}:{client_address[1]}:",decrypted_data
            respuesta=bytes(respuesta,"utf-8")
            print(f"Mensaje recibido del cliente {client_address}: {decrypted_data.decode()}")
            for clientes in datos:
                clientes.sendall(f.encrypt(respuesta))
                clientes.close()
        
        

# Iniciar el servidor
start_server()