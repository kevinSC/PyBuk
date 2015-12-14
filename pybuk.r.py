import ahorcado
import invitado
import admin
import os
DB = invitado.cargarArchivo('libros.txt')
menuBook = {1: 'Codigo ISBN', 2: 'Titulo', 3: 'Autor'}
ahorcado.printIntro('movie.txt')
ahorcado.showMenu({1: 'invitado', 2: 'administrador'}, 'por favor ingresa una opcion:')
while True:
	try:
		option = int(input())
		if option < 1 or option > 2:
			print('ingrese 1 o 2:')
			continue
		break
	except ValueError:
		print('ingrese 1 o 2:')
if option == 1:
	ahorcado.showMenu(menuBook, 'por favor ingresa una opcion de busqueda:')
	while True:
		try:
			tipoS = int(input())
			if option < 1 or option > 3:
				print('ingrese 1, 2 o 3:')
				continue
			break
		except ValueError:
				print('ingrese 1, 2 o 3:')
	if tipoS ==1:
		print('ingrese los codigos ISBNs separados por una coma')
		while True:
			try:
				books = input()
				books = books.split(',')
				for book, y in zip(books, range(len(books))):
					books[y] = book.strip()
				invitado.imprimirMaterial(books, DB)
				break
			except KeyError:
				print('por favor ingresa codigos ISBN validos:')
	elif tipoS == 2:
		print('Por favor ingese el titulo de algun libro')
		titulo = input().strip()
		Dbooks = invitado.getIDsPorTitulo(titulo, DB)
		invitado.imprimirMaterial(Dbooks, DB)
	else:
		print('ingrese el nombre del Autor:')
		Autor = input().strip()
		invitado.imprimirMaterial(invitado.getIDsPorAutor(Autor, DB), DB)
else:
	os.system('clear')
	print('por favor ingrese nombre:')
	print('por favor ingrese contraseñas:')
	#ahorcado.showMenu({1:'acceder a biblioteca', 2: 'Configuraciones de ususarios'})