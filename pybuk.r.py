import ahorcado
import invitado
import admin
import os
DB = invitado.cargarArchivo('libros.txt')
menuBook = {1: 'Codigo ISBN', 2: 'Titulo', 3: 'Autor'}
#ahorcado.printIntro('movie.txt')
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
	if tipoS == 1:
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
		Autor = input('ingrese el nombre del Autor:\n').strip()
		invitado.imprimirMaterial(invitado.getIDsPorAutor(Autor, DB), DB)
else:
	DA = admin.cargarArchivo('administradores.txt')
	os.system('clear')
	while True:
		findPassword = False
		findUser = False
		nickName = input('por favor ingrese nickName:')
		for ID, tupla in DA.items():
			if nickName == tupla[2]:
				intentos = 0
				while intentos < 3:
					password = input('por favor ingrese contraseña:')
					if password == tupla[3]:
						findPassword = True
						break
					else:
						intentos += 1

				findUser = True
				break
		if findUser and findPassword:
			break
	os.system('clear')
	ahorcado.showMenu({1: 'acceder a biblioteca', 2: 'Configuraciones de ususarios'})
	while True:
		try:
			option2 = int(input())
			if option2 < 1 or option2 > 2:
				print('ingrese 1 o 2:')
				continue
			break
		except ValueError:
			print('ingrese 1 o 2:')
	if option2 == 1:
		ahorcado.showMenu({1: 'Buscar libros', 2: 'Borrar Libro', 3: 'agregar Libro', 4: 'ver biblioteca'})
		while True:
			try:
				libroOption = int(input())
				if libroOption < 1 or libroOption > 4:
					print('ingrese 1, 2, 3 o4:')
					continue
				break
			except ValueError:
				print('ingrese 1, 2, 3 o 4:')
		if libroOption == 1:
			ahorcado.showMenu(menuBook)
			while True:
				try:
					tipoSa = int(input())
					if option < 1 or option > 3:
						print('ingrese 1, 2 o 3:')
						continue
					break
				except ValueError:
					print('ingrese 1, 2 o 3:')
			if tipoSa == 1:
				print('ingrese los codigos ISBNs separados por una coma')
				while True:
					try:
						books2 = input()
						books2 = books2.split(',')
						for book, y in zip(books2, range(len(books2))):
							books2[y] = book.strip()
						invitado.imprimirMaterial(books2, DB)
						break
					except KeyError:
						print('por favor ingresa codigos ISBN validos:')
			elif tipoSa == 2:
				print('Por favor ingese el titulo de algun libro')
				titulo2 = input().strip()
				Dbooks2 = invitado.getIDsPorTitulo(titulo2, DB)
				invitado.imprimirMaterial(Dbooks2, DB)
			else:
				Autor2 = input('ingrese el nombre del Autor:\n').strip()
				invitado.imprimirMaterial(invitado.getIDsPorAutor(Autor2, DB), DB)
		elif libroOption == 2:
			while True:
				try:
					admin.eliminarLibro(input('por favor ingrese el ISBN del libro a eliminar:\n'), DB)
					break
				except KeyError:
					print('Este libro no existe')
		elif libroOption == 3:
			nbook = input('por favor ingrese el nuevo libro.\nen el siguiente orden separado por comas:\nISBN, Titulo, Autores, Año').split(',')
			isbn, titulot, autorest, yeart = nbook
			admin.agregarLibro(isbn, titulot, autorest, yeart, DB)
