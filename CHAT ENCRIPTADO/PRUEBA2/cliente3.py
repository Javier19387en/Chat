# Código del cliente 1
import socket

# Crear el socket del cliente 1
client_socket = socket.socket()

# Conectar el socket al servidor
server_address = "10.0.0.1" # La dirección IP del servidor
server_port = 8000 # El puerto del servidor
client_socket.connect((server_address, server_port))

# Enviar y recibir mensajes al servidor y al otro cliente
while True:
    message = input("Escribe un mensaje: ") # Pedir al usuario que escriba un mensaje
    if message == "salir": # Si el mensaje es "salir"
        break # Salir del bucle
    else: # Si no es "salir"
        client_socket.sendall(message.encode()) # Codificar el mensaje de texto a bytes y enviarlo al servidor
        response = client_socket.recv(1024) # Recibir la respuesta del servidor o del otro cliente (1024 es el tamaño máximo de bytes)
        print(f"Respuesta recibida: {response.decode()}") # Decodificar la respuesta de bytes a texto y mostrarla

# Cerrar el socket del cliente 1
client_socket.close()
