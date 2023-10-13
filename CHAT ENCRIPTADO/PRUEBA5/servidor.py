import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 55555

# Lista de clientes conectados
clientes = []

# Función para manejar la comunicación con un cliente
def handle_client(client_socket,clientes):
    try:
        while True:
            # Recibir mensaje del cliente
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                break
            print(f'Mensaje recibido: {data}')

            # Reenviar el mensaje a todos los clientes conectados
            for client in clientes:
                #if client != client_socket:
                client.send(data.encode('utf-8'))
                client.close()
    except Exception as e:
        print(f"Error: {e}")
        clientes.remove(client_socket)
        client_socket.close()
def handle_client1(client_socket,clientes,addr):
    try:
        while True:
            # Recibir mensaje del cliente
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                break
            print(f'Mensaje recibido: {data}')

            # Reenviar el mensaje a todos los clientes conectados
            for client in clientes:
                if client[1] != addr:
                    d="prueba"
                    #client[0].connect(client[1])
                    client[0].send(data.encode('utf-8'))
                    #client[0].close()
    except Exception as e:
        print(f"Error: {e}")
        clientes.remove(client_socket)
        client_socket.close()

# Configurar el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f'Servidor escuchando en {HOST}:{PORT}')

# Esperar conexiones de clientes
while True:
    client_socket, addr = server.accept()
    clientes.append([client_socket, addr])
    print(f'Conexión establecida desde {addr[0]}:{addr[1]}')
    #client_socket.connect()
    # Iniciar un hilo para manejar la comunicación con el cliente
    client_thread = threading.Thread(target=handle_client1, args=(client_socket,clientes,addr))
    client_thread.start()
