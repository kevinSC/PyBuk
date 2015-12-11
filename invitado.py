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
guardarLibros('sdffddfs', {'9681643615': ('La nueva mente del emperador', 'Roger Penrose', '2002'), '9586001148': ('Algebra y trigonometria', 'Dennis G. Zill, Jacqueline M. Dewar', '1992'), '958951250X': ('El testamento del paisa', 'Agustin Jaramillo Londoño', '2003'), '978970686544': ('Calculo diferencial e integral', 'James Stewart', '2007'), '9786071507150': ('Precalculo con avances de calculo', 'Dennis G. Zill, Jacqueline M. Dewar', '2012'), '9789504926979': ('Caballo de guerra', 'Michael Morpurgo', '2012'), '9702604486': ('Introduccion al analisis de circuitos', 'Robert L. Boylestad', '2011')})