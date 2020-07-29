import os
import sys
import time

def actualizar():

	confirmar = input("Desea actualizar esta herramienta? S/n: ")
	
	if confirmar == "S" or confirmar == "s":

		try:
			os.system("git clone https://github.com/ANONDOOR/ANONDOOR.git")
			os.system("rm -rf anondoor.py source/ README.md")
			os.system("cd ANONDOOR/")
			os.system("cp -r * ..")
			os.system("rm -rf ANONDOOR/")
			os.system("chmod +x anondoor.py requisitos.sh actualizar.py")
			os.sys.exit()
		except Exception as e:
			print("Hubo un error, usted tiene instalado git?")
	elif confirmar == "N" or confirmar == "n":
		sys.exit()

	else:
		print("por favor, indique un valor valido")
		return actualizar()


if __name__ == '__main__':
	actualizar()
		