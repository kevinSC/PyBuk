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
        book = line.split('-')
        for x, y in zip(book, range(len(book))):
            book[y] = x.strip()
        DB[book[0]] = (book[1], book[2], book[3])
    data.close()
    del DB['ISBN']
    return DB
