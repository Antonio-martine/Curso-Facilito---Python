
def Variables(curso = 'Curso de python'):
    print(curso)
    curso = 'Cursos únicamente de python'
    print(curso)

def Constantes(CURSO = 'curso de python'):
    print(CURSO)
    
def Comentarios(curso = 'Comentario ejecutado'):
    #Esto es un comentario
    print(curso)
    """
        Esto es otro 
            comentario"""
    print(curso)
    
def Numeros_enteros(a = -1):
    b = a + 2
    print(b)

def Numeros_Float(real = 1.1 + 2.2):
    print(real)
    print(f'{real:.2f}')
    
def Extra_enteros(diez = 10, diez_binario = 0b1010,
    diez_octal = 0o12, diez_hex = 0xa):
    print(diez) #Numero entero
    print(diez_binario) #Numero Binario
    print(diez_octal) # Numero Octal
    print(diez_hex) #Numero Hexadecimal

def Extra_float(un_real = 1.1, otro_real = 1/2, not_client = 1.23E3):
    print(un_real) #Primer dato
    print(otro_real) #Segudo dato
    print(not_client) #Tercer dato
    
def Numeros_complejos(complejo = 1+2j):
    print(complejo.real)
    print(complejo.imag)
    
def Cadena_caracteres(hola = 'Hola "Pythonista"',
    hola2 = 'Hola \'Pythonista\'', hola3 = "Hola 'Pythonista'"):
    print(hola)
    print(hola2)
    print(hola3)
    
def Caracter_extra(caracter_a = 'a'):
    print(caracter_a)
    
def Otro_tipos(lista = [1,2,3,8,9],
    tupla = (1,4,8,0,5),  conjunto = set([1,3,1,4]),
    diccionario = {'a': 1, 'b': 3, 'z': 8}):
    print(lista)
    print(tupla)
    print(conjunto)
    print(diccionario)

def Operador_relacional(numero1 = 10, numero2 = 20):
    #Menor que: -> True
    print(numero1 < numero2)
    
    #Mayor que: -> False
    print(numero1 > numero2)
    
    #Igual: -> False
    print(numero1 == numero2)
    
    #Menor igual a: -> True
    print(numero1 <= numero2)
    
    #Mayor igual a: -> False
    print(numero1 >= numero2)
    
    # Diferente: -> True
    print(numero1 != numero2)
    
def Operador_logico(
    #Ejemplo de uso and: 
    resultado1 = True and True,
    
    #Ejemplo de uso de or:
    resultado2 = False or False or 100 > 20,
    
    #Ejemplo de uso and y or:
    resultado3 = True and (False or 5>10),
    
    #Ejemplo de uso not:
    resultado4 = not False):
    print(resultado1) #-> True (se cumplen los requerimiento de comparaciones)
    print(resultado2) #-> True (una de las comparaciones da verdadero)
    print(resultado3) 
    print(resultado4) #-> El valor final sera true
    
def Funcion_type(
    a = ("Geeks","for","Geeks"),
    b = ["Geeks","for","Geeks"],
    c = {"Geeks": 1,"for": 2,"Geeks": 3},
    d = "Hello World",
    e = 10.23,
    f = 11):
    
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    
def Funcion_type2():

    print(type([]) is list) #-> True 
    print(type([]) is not list) #-> False
    print(type(()) is tuple) #-> True
    print(type({}) is dict) #-> True
    print(type({}) is not list) #-> True
    
def Funcion_input():
    #Ejemplo 1
    print("¿Cómo se llama?")
    nombre = input()
    print(f"Me alegro de conocerte, {nombre}")
    
    #Ejemplo 2 
    print("¿Cómo se llama? ", end = "")
    nombre = input()
    print(f"Me alegro de conocete, {nombre}")
    
    #Ejemplo 3 
    nombre = input("¿Como se llama? ")
    print(f"Me alegro de conocerte , {nombre}")
    
def ConversionDeTipos_input():
    """Error: 
    cantidad = input("Digame una cantidad en pesetas: ")
    print(f"{cantidad} pesetas son {round(cantidad / 166.386, 2)} euros") """
    
    #Ejemplo 1 
    cantidad = int(input("Digame una cantidad: en pesetas: "))
    print(f"{cantidad} pesetas son {round(cantidad / 166.386, 2)} euros")
    
    #Ejemplo 2
    cantidad = float(input("Digame una cantidad en euros: "))
    print(f"{cantidad} euros son {round(cantidad * 166.386, 2)} pesetas") 
    
def VariablesArgumento_input():
    #Ejemplo 1 
    nombre = input("Digame su nombre: ")
    apellido = input(f"Digame su apellido, {nombre}: ")
    print(f"Me alegro de conocerte, {nombre} {apellido}.")
    
    #Ejemplo 2
    numero1 = int(input("Digame un numero: "))
    numero2 = int(input(f"Digame un numero mayor que {numero1}: "))
    print(f"La diferencia entre ellos es: {numero1 - numero2} .")

def ConvertirDatos():   
    #Ejemplo: 
    numero1 = 6
    numero2 = 4.456734
    print("Definimos dos numeros")
    print("numero1 = " + str(numero1))
    print("numero2 = " + str(numero2)) 
    
def Multiples_variables():
    #Ejemplo tradicional: 
    nombre = "Antonio"
    apellido = "Martinez"
    sexo = "hombre"
    edad = 20
    print(f"Resultado de manera tradicional:  Nombre: {nombre}/ Apellido: {apellido}/ Sexo: {sexo}/ Edad: {edad}")
    
    #Ejemplo compacto
    nombre,apellido,sexo = "Antonio","Martinez","hombre"
    edad = 20
    print(f"Resultado de manera compacta:  Nombre: {nombre}/ Apellido: {apellido}/ Sexo: {sexo}/ Edad: {edad}")

def Listas():
    #Lista de numeros
    numeros = [1,2,3,4,5,6,7,8,9,10]
    print(f"Lista de numeros: {numeros}")
    
    #Lista de diferentes tipos
    diferentes_tipos = [3,"a",8,7.2,5<2]
    print(f"Lista de diferentes tipos: {diferentes_tipos}")
    
    #Lista en lista
    lista = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']
    print(f"Lista de lista: {lista}")
    
    #Uso de list
    vocales = list("aeiou")
    print(f"Lista de vocales: {vocales}")
    
    #Listas vacias
    lista_1 = []
    print(f"Lista vacia 1: {lista_1}")
    lista_2 = list()
    print(f"Lista vacia 2: {lista_2}")
    
    
def Index(): 
    #index(element, start(opcional), end(opcional))
    numeros = [1,2,3,4,5,6,7,8,9,10]
    print(f"Numero a buscar 3 encontrado en la posición : {numeros.index(3)}")
    print(f"Numero a buscar 4 encontrado en la posición : {numeros.index(4,3)}")
    print(f"Numero a buscar 6 encontrado en la posición : {numeros.index(6,2,7)}")
    
    #Posiciones
    Posiciones()
    #Mayores y menores: 
    Mayores_menores(numeros) 
    #Evitar errores
    Evitar_errores(numeros)
    
def Posiciones():
    #          0,1,2,3,4,5,6,7,8,9  -> Izquierda a derecha
    #        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1  -> Derecha a izquierda
    numeros = [1,2,3,4,5,6,7,8,9,10]
    print(f"Posicion 2 encontrado elemento: {numeros[2]}")
    print(f"Posicion -4 encontrado elemento: {numeros[-4]}")
    
def Mayores_menores(numeros):
    print(f"El numero menor se encuentra en la posicion: {numeros.index(min(numeros))}")
    print(f"El numero mayor se encuentra en la posicion: {numeros.index(max(numeros))}")
   
def Evitar_errores(numeros):
    if 12 in numeros: 
        arr.index(12)
    else: 
        print("Dato no encontrado")
        
def Enumerate():
    arr = [12, 23, 21, 66, 38, 49, 11, 38, 54]

    lista1 = [p for p, v in enumerate(arr) if v == 38] # [4, 7]
    print(f"Resultado de lista 1: {lista1}")

    lista2 = [p for p, v in enumerate(arr) if v == max(arr)] # [3]
    print(f"Resultado de lista 2: {lista2}")
    
    lista3 = [p for p, v in enumerate(arr) if v == 99] # []
    print(f"Resultado de lista 3: {lista3}")
    
def ModificarDatos_lista():
    letras = ["a","b","c","d"]
    numeros = [1,1,1,2,3,7]
    print(f"Lista de letras antes del cambio: {letras}")
    """ Remplazar un valor único en una lista
    La siguiente sintaxis muestra cómo reemplazar un solo valor en una lista en Python: 
    Reemplazamor el primer elemento, el cual tiene el espacio 0, para el segundo elemento seria 1. """
    letras[0] = "x"
    print(f"Lista de letras modificando un valor: {letras}")
    
    """ Reemplazar varios valores en una lista de python
    La siguiente sintaxis muestra cómo reemplazar varios valores  en una lista en Python: """
    letras[0:3] = ["x","y","z"]
    print(f"Lista de letras modificando valores desde la posicion 0 a 3: {letras}")
    
    """ Remplazar valores especificos en una lista
    En la lista numeros, reemplazaremos los numeros mayores a 1 por 0. """
    numeros = [0 if x>1 else x for x in numeros]
    print(f"Lista de numeros modificando valores mayores a 1 por 0: {numeros}")
    
    """ De la siguiente manera muestra como remplazar valores especificos en una lista en Python: 
    Reeemplazamos los valores iguales a 0 por 2 """
    numeros = [2 if x==0 else x for x in numeros]
    print(f"Lista de numeros modificando valores iguales a 2 por 0: {numeros}")
    
    """ De la misma manera se podría reemplazar valores que sean menores o iguales a algún umbral
    Remplazamos los valores menores o iguales a 2 por 7"""
    numeros = [7 if x <= 2 else x for x in numeros]
    print(f"Lista de numeros modificando valores menores o iguales a 2 por 7: {numeros}")
    
def Sublistas():
    curso = ["Ruby","Python","Django","Flask","Java","Rust"]
    print(f"Lista principal: {curso}")
    
    #Si queremos generar una sublista, colocamos entre corchetes  [start: end]
    #En el siguiente ejemplo, indicaremos que queremos generar una lista desde el indice 0 al 3 de nuestra lista principal
    sub_lista= curso[0:3]
    print(f"Datos extraidos de curso a sub_lista: {sub_lista}")
    
    #Si queremos obtener todos los elementos de una lista a una sublista podemos usar [:]
    sub_lista = curso[:]
    print(f"Todos los datos han sido extraidos de curso a sub_lista: {sub_lista}")
    
    #Si queremos obtener los ultimos elementos a partir de un indice de la lista utilizamos [start: ]
    sub_lista = curso[2:]
    print(f"Todos los datos desde la posicion 2 han sido extraidos de curso a sub_lista: {sub_lista}")
    
    #Si queremos obtener los primeros elementos a partir de un indice final de la lista utilizamos [ :end]
    sub_lista = curso[:4]
    print(f"Todos los datos antes la posicion 4 han sido extraidos de curso a sub_lista: {sub_lista}")
    
    #Si queremos obtener los datos de una lista con saltos podemos utilizar [start:end:skip]
    sub_lista = curso[1:5:2]
    print(f"Todos los datos desde la posicion 1 a 5 en saltos de 2 han sido extraidos de curso a sub_lista: {sub_lista}")
    
    #Si queremos obtener todos los datos de una lista con saltos podemos utilizar [ : :skip]
    sub_lista = curso[::2]
    print(f"Todos los datos en saltos de 2 han sido extraidos de curso a sub_lista: {sub_lista}")
    
    #Si queremos obtener todos los datos de una lista a la inversa utilizamos [ : :-1]
    sub_lista = curso[::-1]
    print(f"Todos los datos en inversa han sido extraidos de curso a sub_lista: {sub_lista}")
    
def MetodosListas():
    lista = ["Antonio","Martinez","Sofia","Diana","Ashley"]
    print(f"Lista sin modificar elementos: {lista}")
    
    #Metodo len()
    print(f"Uso del método len(): {len(lista)}")
    
    #Ordenar elementos de manera ascendente
    lista.sort()
    print(f"Uso del método sort(): {lista}")
    
    #Ordenar elementos de manera descendente
    lista.sort(reverse = True)
    print(f"Uso del método sort(reverse = True): {lista}")
    
    #Metodo append()
    lista.append("Lizbeth")
    print(f"Uso del método append(): {lista}")
    
    #Metodo extend()
    lista.extend("Yanet")
    print(f"Uso del método extend(): {lista}")
    
    #Metodo insert()
    lista.insert(2,"Angelica")
    print(f"Uso del método insert(): {lista}")
    
    #Metodo pop()
    lista.pop(2)
    print(f"Uso del método pop: {lista}")
    
    #Metodo remove()
    lista.remove("Lizbeth")
    print(f"Uso del método remove: {lista}")
    
    #Uso de del
    del lista[0]
    print(f"Uso de del: {lista}")
    
    #Metodo clear()
    lista.clear()
    print(f"Uso del método clear(): {lista}")

    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    



    
    
    

    




