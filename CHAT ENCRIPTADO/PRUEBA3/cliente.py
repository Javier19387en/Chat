import socket
import hashlib
import cryptography.fernet

# Generate a key for encryption and decryption
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(b"r5BkBHhmTScN2ioU6hZ93LfO0qm2KaleMarCHep2X_c=")

def start_client():
    # Configurar el cliente
    #host = '192.168.54.121'
    host = 'localhost'
    port = 8000

    # Crear el socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        # Leer el mensaje del usuario
        message = input("Ingrese un mensaje: ")

        # Encriptar el mensaje
        encrypted_message = f.encrypt(message.encode())

        # Enviar el mensaje encriptado al servidor
        client_socket.send(encrypted_message)

        # Recibir la respuesta del servidor
        encrypted_response = client_socket.recv(1024)
        decrypted_response = f.decrypt(encrypted_response)
        print(f"Respuesta del servidor: {decrypted_response.decode()}")

    # Cerrar la conexión con el servidor
    client_socket.close()

# Clave de encriptación
#encryption_key = hashlib.sha256(b"clave_secreta").digest()

# Iniciar el cliente
start_client()
