import ahorcado
import invitado
import admin
import os


menuBook = {1: 'Codigo ISBN', 2: 'Titulo', 3: 'Autor', 4: 'regresar'}
ahorcado.printIntro('movie.txt')
DA = admin.cargarArchivo('administradores.txt')
DB = invitado.cargarArchivo('libros.txt')

while True:
	ahorcado.showMenu({1: 'invitado', 2: 'administrador', 3:'cerrar'}, 'por favor ingresa una opcion:')
	while True:
		try:
			option = int(input())
			if option < 1 or option > 3:
				print('ingrese 1, 2 o 3')
				continue
			break
		except ValueError:
			print('ingrese 1, 2 o 3')
	if option == 1:
		while True:
			ahorcado.showMenu(menuBook, 'por favor ingresa una opcion de busqueda:')
			while True:
				try:
					tipoS = int(input())
					if option < 1 or option > 4:
						print('ingrese 1, 2, 3 o 4:')
						continue
					break
				except ValueError:
						print('ingrese 1, 2, 3 o 4:')
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
			elif tipoS == 3:
				Autor = input('ingrese el nombre del Autor:\n').strip()
				invitado.imprimirMaterial(invitado.getIDsPorAutor(Autor, DB), DB)
			else:
				break
	elif option == 2:
		while True:
			findPassword = False
			findUser = False
			nickName = input('por favor ingrese nickName:')
			for ID, tupla in DA.items():
				if nickName == tupla[2]:
					intentos = 0
					while intentos < 3:
						password = input('por favor ingrese contraseña:')
						if admin.compare(password, tupla[3]):
							findPassword = True
							break
						else:
							intentos += 1
					findUser = True
					break
			if findUser and findPassword:
				break
		while True:
			ahorcado.showMenu({1: 'acceder a biblioteca', 2: 'Configuraciones de ususarios', 3:'regresar'})
			while True:
				try:
					option2 = int(input())
					if option2 < 1 or option2 > 3:
						print('ingrese 1, 2 o 3:')
						continue
					break
				except ValueError:
					print('ingrese 1, 2 o 3:')
			if option2 == 1:
				ahorcado.showMenu({1: 'Buscar Libros', 2: 'Borrar Libro', 3: 'Agregar Libro', 4: 'ver biblioteca', 5: 'Verificar Libro'})
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
					nbook = input('por favor ingrese el nuevo libro.\nen el siguiente orden separado por comas:\nISBN, Titulo, Autores, Año:\n').split(',')
					isbn, titulot, autorest, yeart = nbook
					while isbn in DB:
						print('El libro ya existe\n')
						nbook = input('por favor ingrese el nuevo libro.\nen el siguiente orden separado por comas:\nISBN, Titulo, Autores, Año:\n').split(',')
						isbn, titulot, autorest, yeart = nbook
					admin.agregarLibro(isbn, titulot, autorest, yeart, DB)
				elif libroOption == 4:
					os.system('less libros.txt')
				else:
					mensaje = 'si existe' if admin.libroDisponible(input('ingese el ISBN del Libro:\n'), DB) else 'no existe'
					print(mensaje)
			elif option2 == 2:
				while True:
					ahorcado.showMenu({1: 'verificar ususario', 2: 'Eliminar ususario', 3: 'Agregar ususario', 4: '\n  Cambiar Login', 5: 'Cambiar contraseña', 6: 'Ver usuario', 7: 'regresar'})
					while True:
						try:
							k = int(input())
							if k < 1 or k > 7:
								print('ingrese 1, 2, 3,4 ,5, 6 o 7:')
								continue
							break
						except ValueError:
								print('ingrese 1, 2, 3,4 ,5, 6 o 7:')
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
						while ID in DA:
							print('Este usuario ya existe')
							strin2 = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nID, Nombres, Apellidos, Login, Password:\n').split(',')
							ID, Nombres, Apellidos, Login, Password = strin2
						admin.agregarUser(ID, Nombres, Apellidos, Login, Password, DA)
					elif k == 4:
						strin3 = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nID, Login nuevo:\n').split(',')
						IDs, Logins = strin3
						admin.cambiarLogin(IDs, Logins, DA)
					elif k == 5:
						strin4 = input('por favor ingrese los datos de usuario.\nen el siguiente orden separado por comas:\nID, contraseña nueva:\n').split(',')
						IDd, contraseñad = strin4
						admin.cambiarPassword(IDd, contraseñad, DA)
					elif k == 6:
						IDw = input('por favor ingrese el ID del usuario')
						admin.verDatosUsuario(IDw, DA)
					else:
						break
			else:
				break
	else:
		break
invitado.guardarLibros('libros.txt', DB)
admin.guardarUsers('administradores.txt', DA)
