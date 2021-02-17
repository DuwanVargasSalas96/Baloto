# -*- coding: UTF-8 -*-

#Import
import os
from random import randint as rnd

#Crear balotas
def playBaloto():
	#Declarar
	baloto = []
	balota = 0

	#Primeras balotas
	while len(baloto) < 5:
		#Asignar
		balota = rnd(1, 43)
		#Busqueda duplicados
		if balota not in baloto:
			baloto.append(balota)

	#Ultima balota
	baloto.append(rnd(1,16))

	#Retorno
	return baloto

#Limpiar
def limpiar():
	#Condicional Clear
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")

#Menu
def main():
	#Loop
	while True:
		#Limpiar
		limpiar()
		
		#Menú
		print("Baloto\n")
		print("1. Generar número ganador.")
		print("2. Salir.")
		
		#Capturar
		option = str(input("Su opción es: "))
		
		if option == "1":
			#Limpiar
			limpiar()
			
			#Imprimir
			print("Baloto\n")
			
			#KeyGen
			print("Su número ganador: " + str(playBaloto()) + "\n")
			input("Presione la tecla Enter regresar al menú.")
			
			#Retorno
			main()
		elif option == "2":
			#Limpiar
			limpiar()
			
			#Salida
			quit()
		else:
			#Imprimir
			input("Opción incorrecta! Intente nuevamente.")

#Linea de ejecucion
main()
