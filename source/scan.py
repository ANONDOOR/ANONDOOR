def requisitos(): 
    try:
        import nmap
        import os
        import sys
        scanmap()
    except ModuleNotFoundError as b:
        print(str(b)) 
        print("\nIntentado instalar requisitos...\n" )
        requisitos1()        

def ayuda():
    ayuda = """

Parametros:


"""
    if __name__ == "__main__":
        print(ayuda)

def scanmap():
    try:
        import nmap
        import os
        import sys
        from tabulate import tabulate
        try:
            print("Ingresa alguno de los parametros en 'Tipo de escaneo'.")
            tabla = [['-u','UDP Scan'],
            ['-s','SYNC Scan'],
            ['-f','Fragmented Scan'],
            ['-all','Todos los parametros de escaneo'],
            ['requisitos','Instalar requerimientos']]
            
            print(tabulate(tabla, tablefmt="fancy_grid"))

            argumento = input("Tipo de escaneo: ")
            if argumento == "requisitos":
                requisitos1()
                exit()
            argumento2 = input("Objetivo: ")
            os.system("clear")

            if argumento == "-u":
                argumento3 = input("Rango [0-100]: ")
                if argumento == "":
                    argumento3 == "0-100"
                scanmap1(argumento2, argumento3)
            if argumento == "-s":
                argumento3 = input("Rango [0-100]: ")
                if argumento == "":
                    argumento3 == "0-100"
                scanmap2(argumento2, argumento3)
            if argumento == "-f":
                argumento3 = input("Rango [0-100]: ")
                if argumento == "":
                    argumento3 == "0-100"
                scanmap3(argumento2, argumento3)
            if argumento == "-all":
                argumento3 = input("Rango [0-100]: ")
                if argumento == "":
                    argumento3 == "0-100"
                scanmap4(argumento2, argumento3)
            else:

                nm = nmap.PortScanner()
                nms = nm.scan(f"{argumento}", f"{argumento2}")

                for host in nm.all_hosts():
                    print('\nHost : %s (%s)' % (host, nm[host].hostname()))
                    print('Estado: %s' % (nm[host].state()))

                    for protocolo in nm[argumento].all_protocols():
                        print('Protocolo: %s' % (protocolo)) 

                        lport = nm[host][protocolo].keys()
                        
                        for puerto in lport:
                            print("\nPuerto: {0} | Nombre: {1} | Estado: {2} | Version: {3}\n".format(puerto, nm[host][protocolo][puerto]['name'], nm[host][protocolo][puerto]['state'], nm[host][protocolo][puerto]['version']))
            

        except IndexError:
            ayuda()
                          
            
    except KeyboardInterrupt:
        print("")
        sys.exit()

def scanmap1(argumento2, argumento3):
    try:
        import nmap
        import os
        import sys
        try:
            os.system("clear")
                
            nm = nmap.PortScanner()
            nms = nm.scan(f"{argumento2}", f"{argumento3}", arguments="-sU -sV")

            for host in nm.all_hosts():
                print('\nHost : %s (%s)' % (host, nm[host].hostname()))
                print('Estado: %s' % (nm[host].state()))

                for protocolo in nm[argumento2].all_protocols():
                    print('Protocolo: %s' % (protocolo)) 

                    lport = nm[host][protocolo].keys()
                     
                    for puerto in lport:
                        print("\nPuerto: {0} | Nombre: {1} | Estado: {2} | Version: {3}\n".format(puerto, nm[host][protocolo][puerto]['name'], nm[host][protocolo][puerto]['state'], nm[host][protocolo][puerto]['version']))
            

        except IndexError:
            ayuda()

            
    except KeyboardInterrupt:
        print("")
        sys.exit()

def scanmap2(argumento2, argumento3):
    try:
        import nmap
        import os
        import sys
        try:
            os.system("clear")
                
            nm = nmap.PortScanner()
            nms = nm.scan(f"{argumento2}", f"{argumento3}", arguments="-sS -sV")

            for host in nm.all_hosts():
                print('\nHost : %s (%s)' % (host, nm[host].hostname()))
                print('Estado: %s' % (nm[host].state()))

                for protocolo in nm[argumento2].all_protocols():
                    print('Protocolo: %s' % (protocolo)) 

                    lport = nm[host][protocolo].keys()
                     
                    for puerto in lport:
                        print("\nPuerto: {0} | Nombre: {1} | Estado: {2} | Version: {3}\n".format(puerto, nm[host][protocolo][puerto]['name'], nm[host][protocolo][puerto]['state'], nm[host][protocolo][puerto]['version']))
            

        except IndexError:
            ayuda()

            
    except KeyboardInterrupt:
        print("")
        sys.exit()

def scanmap3(argumento2, argumento3):
    try:
        import nmap
        import os
        import sys
        try:
            os.system("clear")
                
            nm = nmap.PortScanner()
            nms = nm.scan(f"{argumento2}", f"{argumento3}", arguments="-f --mtu 8")

            for host in nm.all_hosts():
                print('\nHost : %s (%s)' % (host, nm[host].hostname()))
                print('Estado: %s' % (nm[host].state()))

                for protocolo in nm[argumento2].all_protocols():
                    print('Protocolo: %s' % (protocolo)) 

                    lport = nm[host][protocolo].keys()
                     
                    for puerto in lport:
                        print("\nPuerto: {0} | Nombre: {1} | Estado: {2} | Version: {3}\n".format(puerto, nm[host][protocolo][puerto]['name'], nm[host][protocolo][puerto]['state'], nm[host][protocolo][puerto]['version']))
            

        except IndexError:
            ayuda()

            
    except KeyboardInterrupt:
        print("")
        sys.exit()

def scanmap4(argumento2, argumento3):
    try:
        import nmap
        import os
        import sys
        try:
            os.system("clear")
                
            nm = nmap.PortScanner()
            nms = nm.scan(f"{argumento2}", f"{argumento3}", arguments="-sU -sS -f --mtu 8")

            for host in nm.all_hosts():
                print('\nHost : %s (%s)' % (host, nm[host].hostname()))
                print('Estado: %s' % (nm[host].state()))

                for protocolo in nm[argumento2].all_protocols():
                    print('Protocolo: %s' % (protocolo)) 

                    lport = nm[host][protocolo].keys()
                     
                    for puerto in lport:
                        print("\nPuerto: {0} | Nombre: {1} | Estado: {2} | Version: {3}\n".format(puerto, nm[host][protocolo][puerto]['name'], nm[host][protocolo][puerto]['state'], nm[host][protocolo][puerto]['version']))
            

        except IndexError:
            ayuda()

            
    except KeyboardInterrupt:
        print("")
        sys.exit()

def requisitos1():
    import os
    os.system("apt-get install python3-pip")
    os.system("pip3 install nmap")
    os.system("pip3 install python-nmap")

if __name__ == "__main__":
    print("¿Què intentas hacer?")
else:
    requisitos()


    

