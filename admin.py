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
        if login == y[2] and password == y[3]:
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
        print(usuarios[ID])


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
    data = list(U[ID])
    data[2] = input('ingrese login nuevo:\n')
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
    data[3] = input('ingrese password nuevo:\n')
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
    return ISBN in DB

def testlibroDisponible():
    Libros = {
                '9702604486': [' Introduccion al analisis de circuitos', 'Robert L. Boylestad', '2011'], 
                '978970686544': ['Calculo diferencial e integral', 'James Stewart', '2007'], 
                '9586001148': ['Algebra y trigonometria', 'Dennis G. Zill, Jacqueline M. Dewar', '1992'], 
                '9789504926979': ['Caballo de guerra', 'Michael Morpurgo', '2012'], 
                '9786071507150': ['Precalculo con avances de calculo', 'Dennis G. Zill, Jacqueline M. Dewar', '2012']
             }


    print("Test 1. Buscando material que esta disponible...")
    print(libroDisponible('9786071507150',Libros))
    print("Test 2. Buscando material que no esta disponible...")
    print(libroDisponible('10092',Libros))

# Test de la funcion
testlibroDisponible() # Comente esta linea una vez verifique que la salida del programa coincide con la salida esperada a continuacion