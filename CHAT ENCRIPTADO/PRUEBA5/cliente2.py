import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 55555

# Conectar al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("Cliente 2: ")
    client.send(message.encode('utf-8'))
    respuesta = client.recv(4096)
    print(f"Respuesta del servidor: {respuesta.decode()}")