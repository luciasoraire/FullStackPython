# 1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los 
# tres, sólo si éste es único(mayor estricto). En caso de no existir el mayor estricto 
# devolver - 1. No utilizar operadores lógicos ( and , or , not). Desarrollar también un
# programa para ingresar los tres valores, invocar a la función y mostrar el máximo 
# hallado, o un mensaje informativo si éste no existe.


#función
def hayarMayor(num1,num2,num3):

    return max

# programa principal
num1= int(input("Ingrese el primer número"))
num2= int(input("Ingrese el segundo número"))
num3= int(input("Ingrese el tercer número"))
maximo= hayarMayor(num1,num2,num3)
print("El numero mayor es {}").format(maximo)

 
# funcion
def mayor_estricto(num1, num2, num3):
    """
    Función que recibe tres números positivos y devuelve el mayor de los tres, 
    sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto, 
    devuelve -1. No utiliza operadores lógicos (and, or, not).
    """
    mayor = -1  # Inicializar el mayor como -1
    if num1 > num2:
        if num1 > num3:
            mayor = num1
    elif num2 > num1:
        if num2 > num3:
            mayor = num2
    if mayor != -1:  # Si se encontró un mayor estricto, verificar que sea único
        if mayor == num1 and mayor != num2 and mayor != num3:
            return mayor
        elif mayor == num2 and mayor != num1 and mayor != num3:
            return mayor
        elif mayor == num3 and mayor != num1 and mayor != num2:
            return mayor
    return -1  # No se encontró un mayor estricto


#programa principal

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

maximo = mayor_estricto(num1, num2, num3)

if maximo == -1:
    print("No existe un mayor estricto entre los tres números ingresados.")
else:
    print(f"El mayor estricto entre {num1}, {num2} y {num3} es: {maximo}")



# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden 
# a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. 
# Realizar también un programa para verificar el comportamiento de la función.

# función
def mayor_estricto(num1, num2, num3):
    """
    Función que recibe tres números positivos y devuelve el mayor de los tres, 
    sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto, 
    devuelve -1. No utiliza operadores lógicos (and, or, not).
    """
    mayor = -1  # Inicializar el mayor como -1
    if num1 > num2:
        if num1 > num3:
            mayor = num1
    elif num2 > num1:
        if num2 > num3:
            mayor = num2
    if mayor != -1:  # Si se encontró un mayor estricto, verificar que sea único
        if mayor == num1 and mayor != num2 and mayor != num3:
            return mayor
        elif mayor == num2 and mayor != num1 and mayor != num3:
            return mayor
        elif mayor == num3 and mayor != num1 and mayor != num2:
            return mayor
    return -1  # No se encontró un mayor estricto

# programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

maximo = mayor_estricto(num1, num2, num3)

if maximo == -1:
    print("No existe un mayor estricto entre los tres números ingresados.")
else:
    print(f"El mayor estricto entre {num1}, {num2} y {num3} es: {maximo}")



# 3) Un comercio de electrodomésticos necesida para su línea de cajas un programa
# que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
# dos números enteros, # correspondientes al total de la compra y al dinero recibido. 
# Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto,
# de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
# de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido 
# fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto 
# debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3
# billetes de $1

def calcular_vuelto(total_compra, dinero_recibido):
    # Calcula el vuelto y los billetes necesarios para cada denominación
    vuelto = dinero_recibido - total_compra
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    billetes = []

    # Verifica si el dinero recibido es suficiente
    if vuelto < 0:
        return "Error: el dinero recibido es insuficiente"

    # Calcula la cantidad de billetes necesarios para cada denominación
    for denominacion in denominaciones:
        cant_billetes = vuelto // denominacion
        vuelto -= cant_billetes * denominacion
        billetes.append(cant_billetes)

    # Devuelve la cantidad de billetes para cada denominación
    return billetes


# Ejemplo de uso
denominaciones = int
total_compra = 317
dinero_recibido = 500
billetes = calcular_vuelto(total_compra, dinero_recibido)
if isinstance(billetes, str):
    print(billetes)
else:
    print(f"El vuelto es: {dinero_recibido - total_compra}")
    for i in range(len(denominaciones)):
        if billetes[i] > 0:
            print(f"  {billetes[i]} billetes de ${denominaciones[i]}")

# 5) Crear una función lambda que devuelva el cuadrado de un valor recibido como 
# parámetro 
def cuadrado(num):
    return num*num

value= int(input("Ingrese un número"))
input(cuadrado(value)) 

# 6) Crear una función lambda para comprobar si un número es par o impar
es_par = lambda x: x % 2 == 0

# Ejemplo de uso
numero = 5
if es_par(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")


# 7) Crear una lista con los cuadrados de los números entre 1 y N, donde N se ingresa
# desde el teclado, luego imprimir los últimos 10 valores de la lista

# función
def valoresN(n):
    lista=[]
    for i in range(n):
        lista.append(i*i)
    ultimos_10_elementos = lista[-10:]
    print(ultimos_10_elementos) 
# programa ppal 
valorN= int(input("Ingrese valor de N "))
valoresN(valorN)



# 8) Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir 
# lista original, la lista de palabras a eliminar y la lista resultante

# Definir las listas original y de palabras a eliminar
lista_original = ["perro", "gato", "loro", "pez", "ratón"]
palabras_a_eliminar = ["gato", "pez", "ratón"]

# Crear una nueva lista que contenga las palabras de la lista original que no se encuentren en la lista de palabras a eliminar
lista_resultante = [palabra for palabra in lista_original if palabra not in palabras_a_eliminar]

# Imprimir las listas original, de palabras a eliminar y resultante
print("Lista original:", lista_original)
print("Palabras a eliminar:", palabras_a_eliminar)
print("Lista resultante:", lista_resultante)




# 9) Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
# está ordenada en # forma ascendente o False en caso contrario. Por ejemplo, 
# ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False
def ordenada(lista):
    # Recorrer la lista y verificar si cada elemento es mayor o igual que el elemento anterior
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            return False
    return True


# 10) Desarrollar una función que determine si una cadena de caracteres es capicúa,
# sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que
# permita verificar su funcionamiento

def es_capicua(cadena):
    """
    Función que determina si una cadena de caracteres es capicúa sin utilizar cadenas auxiliares ni rebanadas.
    """
    for i in range(len(cadena)//2):
        if cadena[i] != cadena[-i-1]:
            return False
    return True

# 11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que
# la misma tiene 80 columnas
cadena = input("Introduce una cadena: ")
ancho_pantalla = 80
ancho_cadena = len(cadena)

# Si la cadena es más ancha que la pantalla, se imprime sin centrar
if ancho_cadena >= ancho_pantalla:
    print(cadena)
else:
    margen_izquierdo = (ancho_pantalla - ancho_cadena) // 2
    margen_derecho = ancho_pantalla - margen_izquierdo - ancho_cadena
    print(" "*margen_izquierdo + cadena + " "*margen_derecho)


# 12) Escribir una función que reciba como parámetro una tupla conteniendo una
# fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha
# expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de
# Octubre de 2017”. Escribir también un programa para verificar su
# comportamiento.
def fecha_extendida(fecha):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dia, mes, anio = fecha
    fecha_str = "{} de {} de {}".format(dia, meses[mes-1], anio)
    return fecha_str
fecha = (12, 10, 2017)
fecha_str = fecha_extendida(fecha)
print(fecha_str)    

# 13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las
# palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar
# las palabras ordenadas según su longitud
frase = input("Ingrese una frase: ")
palabras = frase.split()
unicas = set(palabras)
ordenadas = sorted(unicas, key=len)
print(ordenadas)



# 14) Desarrollar una función eliminar_claves() que reciba como parámetros un
# diccionario y una lista de claves. La función debe eliminar del diccionario todas
# las claves contenidas en la lista, devolviendo el diccionario modificado y un
# valor de verdad que indique si la operación fue exitosa. Desarrollar también un
# programa para verificar su comportamiento.
def eliminar_claves(diccionario, lista_claves):
    """
    Elimina las claves contenidas en la lista del diccionario.
    Retorna el diccionario modificado y True si la operación fue exitosa,
    o False si alguna clave de la lista no está presente en el diccionario.
    """
    for clave in lista_claves:
        if clave in diccionario:
            del diccionario[clave]
        else:
            return diccionario, False
    return diccionario, True


# 15) Escribir una función para eliminar una subcadena de una cadena de
# caracteres, a partir de una posición y cantidad de caracteres dados,
# devolviendo la cadena resultante. Escribir también un programa para verificar
# el comportamiento de la misma. Escribir una función utilizando rebanadas
def eliminar_subcadena_rebanadas(cadena, inicio, cantidad):
    return cadena[:inicio] + cadena[inicio+cantidad:]

