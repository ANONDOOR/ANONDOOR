import sys
import os
import time
import shutil
import colorsys
from source import ftp, iplogger, payload
from colorama import Fore
from source import cybersendmail

def help():
        print("""

        exit (salir)
        
        salir (salir)

        -h --help (ayuda)
        
        cyberftp (Conectarse Via FTP a un HOST)

        keylogger (crea un keylogger escrito en python)

        iplogger (Ejecuta un iplogger escrito en python)

        payload (Crea un payload con msfvenom)

        spammail (Usa esto para diversion, herramienta de spmam a Emails)

        """)

def menu():
    logo = Fore.CYAN + """
 ▄▄▄       ███▄    █  ▒█████   ███▄    █ ▓█████▄  ▒█████   ▒█████   ██▀███  
▒████▄     ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒
▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒
░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██   ██░▒██▀▀█▄  
 ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░▒████▓ ░ ████▓▒░░ ████▓▒░░██▓ ▒██▒
 ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░
  ░   ▒      ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ 
      ░  ░         ░     ░ ░           ░    ░        ░ ░      ░ ░     ░     
                                          ░  Cyber Phantom                               
""" + Fore.RESET
    
    os.system("clear")
    print(logo,"Plataforma: " + str(sys.platform), "\n Version de python: " + str(sys.version))
    f = str(input(Fore.BLUE + "ANONDOOR~: " + Fore.YELLOW))
    while(True):
        if f == "exit" or f == "salir":
            sys.exit()
        if f == "-h" or f == "--help":
            help()
            sys.exit()
        if f == "cyberftp":    
            ft2 = Fore.CYAN + str(ftp.connect_ftp())
            sys.exit()
        if f == "iplogger":
            Fore.RESET + str(iplogger.ip())
        
        if f == "payload":
            host = input("LHOST: ")
            port = input("LPORT: ")
            ame = input("NOMBRE: ")
            Fore.RESET + str(payload.payload(host,port, ame))

        if f == "keylogger":
                if os.path.exists(path="keylogger.py"):
                    os.remove(path="keylogger.py")
                    shutil.copyfile(src="re242", dst=".. keylogger.py")
                    print("Keylogger reescrito correctamente")
                    sys.exit()
                else:
                    shutil.copyfile(src="re242", dst="keylogger.py")
                    print("Keylogger creado satisfactoriamente")
                    sys.exit()
        if f == "spammail":
            a = input("Ingresa tu correo: ")
            b = input("Ingresa tu contraseña: ")
            c = input("Correo a Enviar mensajes: ")
            d = input("Asunto: ")
            e = input("Mensaje: ")
            cybersendmail.email_spammer(a, b, c, d, e)

                    

        else:
            print(Fore.RED + "-->parametro incorrecto!")
            time.sleep(1)
            return Fore.YELLOW + menu()

menu()




     
     
            
     

