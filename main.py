#!/usr/bin/env python
# -*- coding: utf-8 -*-

## LIBRERIAS
import os
from identificadorFacial import IdentificadorFacial


def display_title_bar():
	# Clears the terminal screen, and displays a title bar.
	os.system('cls' if os.name == 'nt' else 'clear')			  
	print("**********************************************")
	print("*** Identificador Facial - Carlos Barreiro ***")
	print("**********************************************")
	
def pantalla_inicial(opciones):
	# Titular
	peticion = opciones.pop(0)
	print('\n')
	# Opciones
	for i,opcion in enumerate(opciones):
		print( '[{0}] {1}'.format(i,opcion) )
	print('[q] Salir de la opcion.')
	# Tomamos la respuesta
	print('\n')
	return raw_input(peticion)

# def pantalla_personas(personas):
# 	display_title_bar()
# 	for persona in personas:
# 		print('{0} con id {1} con {2} fotos.'.format(persona['name'], persona['personId'], len(persona['persistedFaceIds'])))

# def pantalla_addFace():
# 	display_title_bar()
# 	idi = input('Introduzca el id: ')
# 	imgUrl = input('Introduzca nombre de la imagen: ')
# 	imgUrl = os.path.join('images', imgUrl)
# 	print('URL introducida: {0}'.format(imgUrl))
# 	return idi, imgUrl


def main():
	# Cargamos el identificador facial
	facial = IdentificadorFacial()
	# Limpiamos la terminal y mostramos el titulo
	os.system('cls' if os.name == 'nt' else 'clear')	
	display_title_bar()
	# Opciones disponibles
	opciones = ['Elija una opcion: ']
	opciones.append('Tomar caras con webcam.')
	opciones.append('Tomar caras por carpeta.')
	opciones.append('Entrenar el clasificador')
	opciones.append('Run identify por fichero')
	opciones.append('Run identify por webcam')
	# Mostramos las opciones disponibles
	modo = pantalla_inicial(opciones)
	modo = int(modo)
	### MENU
	### Aplicamos la opcion elegida
	if modo == 0:
		persona = raw_input('\nIntroduzca un id/nombre de referenecia: ')
		facial.input_camera(persona)


if __name__ == "__main__":
	main()