from ftplib import FTP_TLS, FTP
import ftplib
def connect_ftp():
    ftp=FTP()
    ftp.connect(host=input("ingresa el host/pagina: "), port=int(input("ingresa el puerto FTP: ")), timeout=-999)
    ftp.login(input("ingresa el usuario: "),input("ingresa la contraseña: "))
    print(ftp.getwelcome())
    ftp.cwd("..")
    print("""
rename(fromname, toname)

    Rename file fromname on the server to toname.

delete(filename)

    Remove the file named filename from the server. If successful, returns the text of the response, otherwise raises error_perm on permission errors or error_reply on other errors.

cwd(pathname)

    Set the current directory on the server.

mkd(pathname)

    Create a new directory on the server.

pwd

    Return the pathname of the current directory on the server.

rmd(dirname)

    Remove the directory named dirname on the server.""")
    
    while(True):
        a = ftp.sendcmd(cmd=input("ingresa tu comando ftp aqui: "))
        ftp.dir()
        print(a)
    
    



