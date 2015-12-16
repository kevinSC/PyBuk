def findCharacter(word, letter):
    lugar = -1
    characters = []
    place = word[lugar + 1:].find(letter)
    while place != -1:
        lugar += place + 1
        place = (word[lugar + 1:].find(letter)) 
        characters.append(lugar)
    return tuple(characters)


def printIntro(movie, stop=False, number=0):
    ''' 
        recibe un archivo .txt con imagenes en codigo ascii y lo despliega
        en la pantalla de la consola mediante diapositivas
        
        NOTA: El archivo debe ser una imagenes en codi ascii y cada diapositiva
        y es separada por la palabra NEXT
    '''
    import time
    import os
    file = open(movie)
    if not stop:
        for line in file:
            if line == 'NEXT\n':
                time.sleep(0.0625)
                os.system('clear')
            else:
                print(line, end = '')
        file.close()
    else:
        pos = [0]
        lines = file.readlines()
        for x,y in zip(lines,range(0,len(lines))):
            if x == 'NEXT\n':
                pos.append(y)
        number = (len(pos)-1) - number
        print(pos)
        for linea in lines[pos[number-1]+1:pos[number]]:
            print(linea, end='')

def showMenu(menu, message=""):
    '''
        Esta funcion imprime un menu con con sus respectivas opcines.
        recibe como paramentros un diccionario de opciones deseadas a desplegar
        y un string como mensaje
    '''
    print(message)
    print('----------------------------------------------------------------')
    for key, value in menu.items():
        print(value + ':', key, end=" | ")
    print('\n----------------------------------------------------------------')


def showInstructions(instructions='./instructions.txt'):
    import os
    os.system('more ' + instructions)


def dirFiles(path='./Palabras'):
    '''
    	Firma:

			(string) -> (directory)

		Sinopsis:

        	Esta funcion recibe la direccion de un directorio y
        	retorna sus archivos en un diccionario enumerado

        Entradas y salidas:

        	- path: String con la ruta de una carpeta
        	- returns: Un directorio enumerado con todos los ficheros dentro de este

        Ejemplos de uso:
         	>>> ahorcado.dirFiles('./')
         	{1: '.gitignore', 2: 'Palabras', 3: 'README.md', 4: 'ahorcado.py', 5: 'main.py', 6: 'movie.txt', 7: '.pro', 8: '.git', 9: 'i
         	ntro.txt', 10: '__pycache__'}
    '''
    from os import listdir
    temas = listdir(path)
    numbes = range(1,len(temas)+1)
    return dict(zip(numbes, temas))
def loadWords(path):
    '''
        Firma:
            (string) -> (string)
        Sinopsis:
            Función que solicita el nombre de un archivo cualquiera y devuelve una cadena 
            de caracteres con su contenido
    
        Entradas y salidas:
            - filename: string que contiene el nombre del archivo con las palabras secretas
            - returns: string con todas las palabras secretas
    
        Ejemplos de uso:
            >>> loadWords("superHeroes.txt")
            'capitan centella, capitan planeta, batman, superman, robin, mujer maravilla, aquaman, flash,
            cyborg, capitan marciano, linterna verde,flash gordon, liga de la justicia, defensores de la 
            tierra, el fantasma, spider man, hulk, thor, iron man, los vengadores, robocop, terminator, 
            capitan america, hombre hormiga, la avispa, goku, vegeta, gohan, piccolo, trunks, spawn, 
            tintin, ghost rider, blade, tortugas ninja, soldado del invierno, el castigador, 
            el predicador, leonidas, kick ass, el comediante, el chapulin colorado, wolverine,
            flecha verde, el profesor super o, los autobots, robin hood\n'
    '''
    file = open(path)
    words=''
    for line in file:
        words += line
    file.close()
    return words.lower()
def pickWord(words, separador=','):
    '''
        Firma:
            (string,string) -> (string)
    
        Sinopsis:
            Función que permite seleccionar una palabra o frase secreta correspondiente a una posicion 
            dada de un conjunto de palabras separadas por un delimitador.  
    
        Entradas y salidas:
            - palabras: Conjunto de palabras o frases secretas separadas por un delimitador
            - separador: Delimitador que separa una palabra o frase secreta de otra
            - returns: Palabra o frase de la posiciónon elegida
    
        Ejemplos de uso:
            >>> x = 'homero_marge_bart_lisa_maggie' 
            >>> pickWord(x,'_')
            'homero'
    
            >>> palabra = pickWord('marcos, lucas, mateo, juan',',')
            >>> print(palabra)
            'mateo'      
    '''
    import random 
    words = words.split(separador)
    words = words[random.randint(0,len(words)-1)]
    words = words.strip()
    words = words.lower()
    return words
def obtenerParteAdivinada(palabraSecreta, letrasIntentadas):
    '''
    	Firma:
        	(string,list) -> (string)
	
    	Sinopsis:
        	Imprime la parte de la cadena que ha sido adivinada.  
	
    	Entradas y salidas:
        	- palabraSecreta: string, palabra que el usuario esta adivinando
        	- letrasIntentadas: list, letras intentadas por el usuario para adivinar la palabra
        	- returns: string, compuesto de letras y caracteres raya bajo que representan las letras aun no adivinadas.
    	Ejemplos de uso:
        	>>> palabraSecreta = 'perro'
        	>>> letrasIntentadas = ['a', 'e', 'i', 'o', 'u', 's', 'p']
        	>>> print obtenerParteAdivinada(palabraSecreta, letrasIntentadas)
        	'p e _ _ o'
        	>>> obtenerParteAdivinada('frodo', [])
        	'_ _ _ _ _'  
    '''
    if not (letrasIntentadas[0] == ' '):
        letrasIntentadas.insert(0, ' ')
    spaces = '_ ' * len(palabraSecreta)
    for letra in letrasIntentadas:
    	for lugar in findCharacter(palabraSecreta, letra):
    		spaces = spaces[: 2 * lugar] + letra + spaces[( 2 * lugar) + 1:]
    return spaces[:-1]


def obtenerLetrasDisponibles(letrasIntentadas):
    '''
    	Firma:
        	(list) -> (string)
    	Sinopsis:
        	Devuelve las palabras que no se han empleado en los turnos.
    	Entradas y salidas:
        	- letrasIntentadas: list, letras intentadas por el usuario para adivinar la palabra
        	- returns: string, compuesto de letras que no han sido ingresado
    	Ejemplos de uso:
        	>>> letrasIntentadas = ['a', 'b', 'f', 's']
        	>>> print obtenerLetrasDisponibles(letrasIntentadas)
        	cdeghijklmnopqrtuvwxyz
    '''
    import string
    alfabeto = string.ascii_lowercase
    resto= ""
    for x in alfabeto:
        if x in letrasIntentadas:
            resto = resto
        else:
            resto = resto +  x
    return resto
def verificarLetraIngresada(letra,letrasIntentadas):
    '''
    	Firma:
        	(string,list) -> (bool)
	
    	Sinopsis:
        	Devuelve True si la letra ingresada se encuentra dentro de la lista de palabras intentadas.  
	
    	Entradas y salidas:
        	- letra: Letra a verificar
        	- letrasIntentadas: Lista con las letras a comparar
        	- returns: La función devuelve False si ninguna la letra no se encuentra en ninguna de la 
                   	lista. En caso contrario, devuelve True.
	
    	Ejemplos de uso:
        	>>> letrasIntentadas = ['a', 'b', 'f', 's']
        	>>> verificarLetraIngresada('z',letrasIntentadas)
        	False
	
        	>>> verificarLetraIngresada('x',['v', 'w', 'x', 'y', 'z'])
        	True
    '''  
    if letra in letrasIntentadas:
    	return True
    else:
    	return False
def palabraAdivinada(palabra,letrasIntentadas):
    '''
    	Firma:
        	(string,list) -> (bool)
	
    	Sinopsis:
        	Devuelve True si algunas o todas las letras de la lista pueden formar la palabra.  
	
    	Entradas y salidas:
        	- palabra: Palabra o frase a verificar
        	- letrasIntentadas: Lista con las letras a comparar
        	- returns: Devuelve True si con las letras de la lista pueden formar la palabra y False, en 
             	caso contrario.
	
    	Ejemplos de uso:
        	>>> palabraAdivinada('bilbo',['b','s','n','l','i','o'])
        	True
	
        	>>> palabraAdivinada('karman',['c','a','m',])
        	False
    '''
    adivino = False
    limit = len(palabra)
    for letra in letrasIntentadas:
    	limit -= len(findCharacter(palabra,letra))
    	if limit == 0:
    		adivino = True
    		break
    return adivino
def wrongImput(menu):
	import os
	wrong = True
	while wrong:
		try:
			option = int(input(': '))
			wrong = False
		except ValueError:
			os.system('clear')
			printIntro('intro.txt')
			showMenu(menu,'Por favor ingresa el numero de la opción que deseas:')
			print('¿Quieres romper mi codigo?\nPiensa antes de digitar amig@')
	return option
def selctDir(file_number,path='./Palabras'):
	directorio = dirFiles(path)
	direccion = path+'/'+directorio[file_number]
	return direccion
