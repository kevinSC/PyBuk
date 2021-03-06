def crypting(password):
    import bcrypt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
'sdfdsfsdf'

def compare(password, hashed):
    import bcrypt
    hashed = hashed.encode()
    return True if bcrypt.hashpw(password.encode(), hashed) == hashed else False


def cargarArchivo(filename):
    
    DB = {}
    data = open(filename, 'r')
    for line in data:
        user = line.split(' - ')
        for x, y in zip(user, range(len(user))):
            user[y] = x.strip()
        DB[user[0]] = (user[1], user[2], user[3], user[4])
    data.close()
    del DB['ID']
    return DB

def verificarUsuario(login, password, usuarios):
    '''
        (str,str,dict) -> (int)
        Sinopsis:
            Esta función retorna el ID del usuario que se logea si este se encuentra en la estructura asociada a los usuarios o None si no se encuentra o el usuario introduce mal la contraseña.
        Entradas:
            - login: Usuario almacenado en el sistema.
            - password: Contraseña asociada al usuario.
            - usuarios: Estructura que tiene almacenada la información de usuarios con capacidades de administracion.
        Retorna:
            ID del usuario administrador perteneciente a la estructura de datos asociada a los administradores.
    '''
    for x, y in usuarios.items():
        if login == y[2] and compare(password.strip(), y[3]):
            return x
            break


def verDatosUsuario(ID, usuarios):
    '''
        (int,dict) -> (None)
        Sinopsis:
        Imprime la información asociada (Nombres, identificación, login, clave) al  usuario administrador con identificacion ID.
        Entradas:
            - ID: Identificacion del usuario administrador.
        - usuarios: Estructura que tiene almacenada la información de usuarios con  capacidades de administracion.
        Retorna:
            Ninguno
    '''
    if ID in usuarios:
        user = usuarios[ID]
        print('ID{}\tNOMBRES{}\tAPELLIDOS{}\tLOGIN{}\tPASSWORD'.format(' ' * (len(ID) - 2), ' ' * (len(user[0]) - 7), ' ' * (len(user[1]) - 9), ' ' * (len(user[2]) - 5), ' ' * (len(user[3]) - 8)))
        print(ID + '\t{}\t{}\t{}\t{}'.format(*user))


def cambiarLogin(ID, login, U):
    '''
        (int, str, dict) -> (None)
        Sinopsis:
            Permite cambiar el login del usuario con identificacion ID perteneciente a la estructura de datos de usuarios
            administradores U, al valor pasado como argumento en el parámetro login cuando la función es invocada.
        Entradas:
            - ID: Identificacion del usuario administrador.
            - login: Valor del nuevo login.
            - U: Estructura que tiene almacenada la información de usuarios con capacidades de administracion.
        Retorna:
            Ninguno
    '''
    ID = ID.strip()
    data = list(U[ID])
    data[2] = login.strip()
    U[ID] = tuple(data)


def cambiarPassword(ID, password, U):
    '''
    (int, str, dict) -> (None)
    Sinopsis:
        Permite cambiar la clave del usuario con identificaion ID perteneciente a la estructura de datos de usuarios
        administradores al valor pasado como argumento la nueva clave en el parámetro password cuando
        la función es invocada.
    Entradas:
        - ID: Identificacion del usuario administrador.
        - password: Valor de la nueva clave que tendrá el usuario.
        - U: Estructura que tiene almacenada la información de usuarios con capacidades de administracion.
    Retorna:
        Ninguno
    '''
    data = list(U[ID])
    data[3] = crypting(password.strip())
    U[ID] = tuple(data)


def libroDisponible(ISBN, DB):
    '''
    (str, dict) -> (Bool)
    Sinopsis:
        Función que verifica si la ISBN del libro está disponible dentro de la base de datos de la biblioteca.
    Entradas:
        - ISBN: ISBN del libro que se esta buscando
        - DB: Estructura que tiene almacenada la información de los libros de la biblioteca.
    Retorna:
        Función que verifica si la ISBN del libro está disponible dentro de la base de datos de la biblioteca.
    '''
    return ISBN.strip() in DB


def agregarLibro(ISBN, titulo, autores, year, DB):
    '''
        (str, str, str, str, dict) -> (None)
        Sinopsis:
        Función que agrega un nuevo libro (item) al diccionario en el cual se encuentra     almacenado el inventario
            de libros de la biblioteca.
        Entradas:
        - ISBN (str): ID del libro que  se desea almacenar.
        - titulo (str): Cadena que contiene el título del libro     que se desea almacenar.
        - autores (str): Cadena que contiene cada uno de los    autores separados por coma.
        - DB (dic): Estructura que tiene almacenada la información de   los libros de la biblioteca.
        Retorna:
            Ninguno
    '''
    if not ISBN in DB:
        DB[ISBN.strip()] = (titulo.strip(), autores.strip(), year.strip())


def agregarUser(ID, Nombres, Apellidos, Login, password, DB):
    if not ID in DB:
        DB[ID.strip()] = (Nombres.strip(), Apellidos.strip(), Login.strip(), crypting(password.strip()))


def eliminarLibro(ISBN, DB):
    '''
        (str, dict) -> (None)
        Sinopsis:
        Función que el libro cuya ID es idB del diccionario asociado al inventario de   libros de la biblioteca.
        Entradas:
            - ISBN (str): ISBN del libro que se desea eliminar.
        - DB (dic): Estructura que tiene almacenada la información de los libros de la  biblioteca.
        Retorna:
            Ninguno
    '''
    del DB[ISBN.strip()]


def eliminarUser(ID, DB):
    del DB[ID.strip()]


def guardarUsers(filename, dic):
    data = open(filename, 'w')
    data.write('ID - NOMBRES - APELLIDOS - LOGIN - PASSWORD\n')
    for key, value in dic.items():
        data.write(key + ' - ' + value[0] + ' - ' + value[1] + ' - ' + value[2] + ' - ' + value[3] + '\n')
    data.close()
