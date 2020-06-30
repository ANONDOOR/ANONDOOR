import sys
import os
import time
import shutil
import colorsys
from source import ftp, iplogger, payload, cybersendmail, bruteforceEmail
from colorama import Fore


def help():
        print("""

        exit (salir)
        
        salir (salir)

        -h --help (ayuda)
        
        cyberftp (Conectarse Via FTP a un HOST)

        keylogger (crea un keylogger escrito en python)

        iplogger (Ejecuta un iplogger escrito en python)

        payload (Crea un payload con msfvenom)

        spammail (Usa esto para diversion, herramienta de spam a Emails)

        brutemail (herramienta de fuerza bruta a Gmail)

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
                                          ░  Cyber Phantom                   """ + Fore.RESET
    
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
                    time.sleep(1)
                    os.system("cd source/")
                    time.sleep(1)
                    os.system("cp re242 ..")
                    time.sleep(1)
                    os.system("cd ..")
                    time.sleep(1)
                    os.system("mv re242 keylogger.py")
                    time.sleep(1)
                    print("Keylogger reescrito correctamente")
                    sys.exit()
                else:
                    os.system("cd source/")
                    time.sleep(1)
                    os.system("cp re242 ..")
                    time.sleep(1)
                    os.system("cd ..")
                    time.sleep(1)
                    os.system("mv re242 keylogger.py")
                    print("Keylogger creado satisfactoriamente")
                    sys.exit()
        if f == "spammail":
            a = input("Ingresa tu correo: ")
            b = input("Ingresa tu contraseña: ")
            c = input("Correo a Enviar mensajes: ")
            d = input("Asunto: ")
            e = input("Mensaje: ")
            cybersendmail.email_spammer(a, b, c, d, e)
        if f == "brutemail":
            bruteforceEmail.brute()

                    

        else:
            print(Fore.RED + "-->parametro incorrecto!")
            time.sleep(1)
            return Fore.YELLOW + menu()

menu()




     
     
            
     

