from colorama import Fore
import smtplib
import os
import time
try:
    import sendmail
except:
    print("hubo un error al importar el modulo sendmail")

# -*- coding: utf-8 -*-
def email_spammer(emisor, password, receptor, asunto, mensaje):
    cantidad = int(input("Cantidad de mensajes a enviar: "))
    numero = 0
    print("\npara cancelar el proceso: CTRL + Z\n")
    #asunto = "se te olvidaron las pastas"
    #mensaje = """Hola!<br/> <br/>
    #Este es un <b>e-mail</b> enviando desde <b>Python</b>
    #"""
    Email = """From: %s
    To: %s
    MIME-version: 1.0
    Content-type: text/html
    Subject: %s

    %s

    """ % (emisor, receptor, asunto, mensaje)
    while numero <= cantidad:
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(emisor, password)
            smtp.sendmail(emisor, receptor, Email)
            smtp.quit()
            print(Fore.RED + "[{0}]".format(numero) + Fore.RESET + "Correo Enviado") 
        except:
            print("correo no enviado") 
            request = input("intentando instalar sendmail/verifica que la contraseña sea correcta, Desea continuar con la instalacion? S/n: ")
            if request == "S" or request == "s":
                time.sleep(5)
                os.system("sudo apt-get install sendmail")
            elif request == "n" or request == "N":
                break
        numero = numero + 1
        if numero == cantidad:
            print("\nsecuencia completada!\n")