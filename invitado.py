def cargarArchivo(filename):
    '''
        (str) -> (dict)
        Sinopsis:
            Carga un archivo de texto y lo lleva a un diccionario. Para el caso el elemento
            de la primera columna siempre será la clave (key) del diccionario, mientras que los demás elementos
            formarán una lista la cual será el valor asociado.
        Entradas:
            - filename: string, Nombre (con ruta completa de ser necesario) del archivo de texto a leer
        Retorna:
            Diccionario (dict) que contiene cada uno de los ítems del archivo leído.
    '''
    DB = {}
    data = open(filename, 'r')
    for line in data:
        book = line.split(' - ')
        for x, y in zip(book, range(len(book))):
            book[y] = x.strip()
        DB[book[0]] = (book[1], book[2], book[3])
    data.close()
    del DB['ISBN']
    return DB


def guardarLibros(filename, dic):
    '''
        (str, dict) -> None
            Sinopsis:
                Almacena los ítems del diccionario dic en el archivo de texto de nombre filename siguiendo el formato para la base de datos tal y como se muestra a continuacion:
                ------------------------------------------------------------------------------------------    
            ISBN - TITULO - AUTORES - AÑO
            ID1 -  Titulo libro 1 - Autores libro 1 (separados por coma) - Año de publicacion libro 1
            ID2 -  Titulo libro 2 - Autores libro 2 (separados por coma) - Año de publicacion libro 2
            IDN -  Titulo libro N - Autores libro N (separados por coma) - Año de publicacion libro N
        ------------------------------------------------------------------------------------------   
        Entradas:
            - filename: string, Nombre del archivo de texto en el que se almacenará el inventario.
            - dic: dict, Diccionario que contiene la estructura de datos asociada al inventario de la biblioteca
        Retorna:
            None.
    '''
    data = open(filename, 'w')
    data.write('ISBN - TITULO - AUTORES - AÑO\n')
    for key, value in dic.items():
        data.write(key + ' - ' + value[0] + ' - ' + value[1] + ' - ' + value[2] + '\n')
    data.close()


def getIDsPorAutor(autor, dataBase):
    '''
        (str,dict) -> (list)
        Sinopsis:
            Función que devuelve una lista con los IDs de los libros del autor pasado como argumrento contenidos en el diccionario asociado al inventario de la biblioteca.
        Entradas:
            - autor: str, Nombre del autor
            - dataBase: dict, Diccionario que contiene la base de datos asociada al inventario de la biblioteca.
        Retorna:
            IDs de los libros que tienen por autor el valor asignado al parámetro de la función autor.
    '''
    IDs = []
    for ID, book in dataBase.items():
        escritores = book[1].split(',')
        for escritor in escritores:
            if escritor.lower().find(autor.lower().strip()) != -1:
                IDs.append(ID)
    return tuple(IDs)


def getIDsPorTitulo(titulo, dataBase):
    '''
    (str,dict) -> (list)
    Sinopsis:
        Función que devuelve los IDs de los libros contenidos en el diccionario dataBase
        y cuyo titulo es pasado como argumento al parametro título.
    Entradas:
        - autor: str, Nombre del titulo
        - dataBase: dict, Diccionario que contiene la base de datos asociada al inventario de la biblioteca.
    Retorna:
        Lista de los ISBN de los libros que tienen por título el valor asignado al parámetro título de la función.
    '''
    IDs = []
    for ID, Book in dataBase.items():
        if Book[0].lower().find(titulo.lower().strip()) != -1:
            IDs.append(ID)
    return tuple(IDs)


def imprimirMaterial(ISBNs, DB):
    '''
    (list,dict) -> (None)
    Sinopsis:
        Función que muestra una tabla con la informacion de los libros cuya ISBN se paso como argumento.
    Entradas:
        - ISBN: Lista que contiente las ISBN de los libros que se desean desplegar.
        - DB: Diccionario que contiene la base de datos asociada al inventario de la biblioteca.
    Retorna:
        Esta funcion no retorna nada.
    '''
    for ISBN in ISBNs:
        base = DB[ISBN]
        print('ISBN: {}, Titulo: {}, Autor: {}, Año: {}'.format(ISBN, base[0], base[1], base[2]))

def testimprimirMaterial():
    Libros = {
                '9702604486': [' Introduccion al analisis de circuitos', 'Robert L. Boylestad', '2011'], 
                '978970686544': ['Calculo diferencial e integral', 'James Stewart', '2007'], 
                '9586001148': ['Algebra y trigonometria', 'Dennis G. Zill, Jacqueline M. Dewar', '1992'], 
                '9789504926979': ['Caballo de guerra', 'Michael Morpurgo', '2012'], 
                '9786071507150': ['Precalculo con avances de calculo', 'Dennis G. Zill, Jacqueline M. Dewar', '2012']
             }

    print("Busqueda 1...")
    ID = ['978970686544','9786071507150']
    imprimirMaterial(ID,Libros)
    print("\nBusqueda 2...")
    imprimirMaterial(['9586001148'],Libros)
    print("\nBusqueda 3...")
    imprimirMaterial([],Libros)
testimprimirMaterial()