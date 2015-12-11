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
