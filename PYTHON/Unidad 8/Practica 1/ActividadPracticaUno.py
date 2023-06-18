'''
# 1) escribe un programa que muestre en pantalal "Hello World" #
print("Hello World")

# 2) Escriba un programa que escriba el resultado de sumar 3+5#
print(3+5)

# 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga
#"Hola nombreUsuario" 
nombreUsuario= input("Ingrese nombre de usuario ")
print("Hola " + nombreUsuario)

# 4) Escribe un programa que pida un número, otro número y escriba el resultado de sumarlos  para#
num1= input("Ingrese el primer número ")
num2= input("Ingrese un segundo número ")
rtdo=int(num1)+int(num2)

#print(" La suma de " + num1 + " y " + num2 + " es: " + str(rtdo))
# 2da opción #
mensaje="La suma de {} y {}  es {}".format(num1,num2,str(rtdo))
print(mensaje)

# 5) Escriba un programa que pida dos números y escriba en pantalla cuál es el mayor
num1=int(input("Ingrese el primer número "))
num2= int(input("Ingrese un segundo número "))
if num1 > num2:
    print(num1)
else:
    print(num2)

# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los 3
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "es el mayor de los tres números.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "es el mayor de los tres números.")
else:
    print(num3, "es el mayor de los tres números.")

# 7) Escribe un programa que pida un número y diga si es divisible por 2
num= int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es divisible por 2")
else:
    print("El número no es divisible por 2")

# 8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(numero, "es divisible por 2.")
if numero % 3 == 0:
    print(numero, "es divisible por 3.")
if numero % 5 == 0:
    print(numero, "es divisible por 5.")
if numero % 7 == 0:
    print(numero, "es divisible por 7.")

# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible
numero = int(input("Ingrese un número entero: "))
divisibles = ""

if numero % 2 == 0:
    divisibles += "2, "
if numero % 3 == 0:
    divisibles += "3, "
if numero % 5 == 0:
    divisibles += "5, "
if numero % 7 == 0:
    divisibles += "7, "

if divisibles == "":
    print(numero, "no es divisible por 2, 3, 5 o 7.")
else:
    print(numero, "es divisible por", divisibles[:-2] + ".")

# 10) Escribir un programa que nos diga en pantalla los divisores de un número dado
numero = int(input("Ingrese un número entero: "))

print("Los divisores de", numero, "son:")

for divisor in range(1, numero+1):
    if numero % divisor == 0:
        print(divisor)    

# 11) Escribir un programa que nos diga si un número dado es primo
def es_primo(num):
    if num <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    elif num == 2:
        return True  # 2 es un número primo
    else:
        # Verificamos si num es divisible por algún número menor que él mismo
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

# 12) Pide una nota. Muestra la calificación según la nota: 0-3 (muy deficiente), 3-5 (insuficiente), 5-6
# (suficiente), 6-7 (bien), 7-9 (notable), 10 (sobresaliente)

nota = float(input("Introduce la nota: "))
if nota >= 0 and nota <= 3:
    print("Muy deficiente")
else:
    if nota >= 4 and nota <=5:
        print("Insuficiente")
    if nota >= 6 and nota <= 7:
        print("Suficiente")
    if nota >= 8 and nota <= 9:
        print("Notable")
    if nota == 10:
        print("Sobresaliente")

        
'''