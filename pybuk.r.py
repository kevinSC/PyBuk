import ahorcado
import invitado
import admin
import os
DA = admin.cargarArchivo('administradores.txt')
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
		ahorcado.showMenu({1: 'Buscar libros', 2: 'Borrar Libro', 3: 'agregar Libro', 4: 'ver biblioteca', 5: 'verificar libro'})
		while True:
			try:
				libroOption = int(input())
				if libroOption < 1 or libroOption > 5:
					print('ingrese 1, 2, 3, 4 o 5:')
					continue
				break
			except ValueError:
				print('ingrese 1, 2, 3, 4 o 5:')
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
		elif libroOption == 4:
			os.system('less libros.txt')
		else:
			mensaje = 'si existe' if admin.libroDisponible(input('ingese el ISBN del Libro:\n'), DB) else 'no existe'
			print(mensaje)
	else:
		ahorcado.showMenu({1: 'verificar ususario', 2: 'Eliminar ususario', 3: 'Agregar ususario', 4: '\n  Cambiar Login', 5: 'Cambiar contraseña', 6: 'Ver usuario'})
		while True:
			try:
				k = int(input())
				if k < 1 or k > 6:
					print('ingrese 1, 2, 3,4 ,5  o 6:')
					continue
				break
			except ValueError:
					print('ingrese 1, 2, 3,4 ,5  o 6:')
		if k == 1:
			while True:
				strin = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nlogin, password:\n').split(',')
				login, password = strin
				existe = admin.verificarUsuario(login, password, DA)
				if existe == None:
					print('el usuario no existe')
					continue
				else:
					print('el usuario le corresponde el ID:', existe)
					break
		elif k == 2:
			while True:
				try:
					identificacion = input('por favor ingresa el ID del usuario a eliminar:\n')
					admin.eliminarUser(identificacion, DA)
					break
				except KeyError:
					print('por favor ingresa un ID valido')
		elif k == 3:
			strin2 = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nID, Nombres, Apellidos, Login, Password:\n').split(',')
			ID, Nombres, Apellidos, Login, Password = strin2
			admin.agregarUser(ID, Nombres, Apellidos, Login, Password, DA)
		elif k == 4:
			strin3 = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nID, Login:\n').split(',')
			IDs, Logins = strin3
			admin.cambiarLogin(IDs, Logins, DA)
		elif k == 5:
			strin4 = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nID, contraseña:\n').split(',')
			IDd, contraseñad = strin4
			admin.cambiarPassword(IDd, contraseñad, DA)
		else:
			IDw = input('por favor ingrese el ID del usuario')
			admin.verDatosUsuario(IDw, DA)
invitado.guardarLibros('libros.txt', DB)
admin.guardarUsers('administradores.txt', DA)
