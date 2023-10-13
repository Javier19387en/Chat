import socket
from cryptography.fernet import Fernet

#PROCESO DE ENCRIPTACION DE LOS MENSAGES

def encriptar(texto, clave):
    # Generar una clave de encriptación a partir de la clave proporcionada
    clave_bytes = clave.encode()
    clave_encriptacion = Fernet.generate_key()
    f = Fernet(clave_encriptacion)

    # Encriptar el texto
    texto_encriptado = f.encrypt(texto.encode())

    return texto_encriptado, clave_encriptacion

def desencriptar(texto_encriptado, clave_encriptacion):
    f = Fernet(clave_encriptacion)

    # Desencriptar el texto
    texto_desencriptado = f.decrypt(texto_encriptado).decode()

    return texto_desencriptado


# Crea un objeto de socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Envía y recibe datos a través de la conexión
PERMANENCIA=True
EXIT=False
while PERMANENCIA:
    if EXIT==True:
        # Cierra la conexión
        client_socket.close()
        PERMANENCIA=False
    MSG=""
    print("INGRESE UN MENSAGE")
    MSG=input()
    asd=MSG
    print(encriptar(asd,"1234"))
    if MSG=="exit":EXIT=True
    if MSG!="":
        client_socket.send(encriptar(MSG,"1234"))
        response = client_socket.recv(1024).decode()
        print(">"+response)