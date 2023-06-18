# 1) Crear una clase Persona con los métodos ¨set_nombre¨
# “get_nombre”, “get_edad” y  “print_persona”. Luego 
# crear dos objetos del tipo Persona e imprimirlos
# por consola
# 2) agregarle a la clase anterior un constructor que
# reciba nombre y edad
# 3) Agregarle a la clase anterior un método es_mayor_de_edad
# que devueva true o false
# 4) agregarle un método es_mayor_que el cual recibe un objeto
# persona y compara su edad con la del objeto actual
# 5) agregarle un método get_mayor que reciba dos objetos
# Persona y devuelva el de edad mayor


class Persona: 
    def constructor(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad   

    def get_nombre(self):
        print(self.nombre)

    def get_edad(self):
        print(self.edad)

    def print_persona(self):
        print(self.nombre +"  "+  str(self.edad))
    # ejercicio 3
    def es_mayor_de_edad(self):
        return self.edad > 18
    # ejercicio 4
    def es_mayor_que(self,persona):
        return self.edad > persona.get_edad
    
    # ejercicio 5
    @staticmethod
    def get_mayor(self,persona):
        if self.edad > persona.get_edad:
            return self
        else:
            return persona

# programa principal
sofia= Persona()
sofia.constructor("Sofia", 20)
rufina= Persona()
rufina.constructor("Rufina",3)
sofia.print_persona()
rufina.print_persona()

################################
# 6) Realizar un programa que conste de una clase llamada
# Alumno que tenga como atributos el nombre y la nota
# del alumno. Definir los métodos para inicializar sus 
# atributos, imprimirlos y mostrar un mensaje
# con el resultado de la nota y si ha aprobado o no

class Alumno:
    def constructor(self,nombre,edad, nota):
        self.nombre=nombre
        self.edad=edad
        self.nota= nota
    
    def print_info(self):
        print("Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Nota: " + self.nota)

    def get_nota(self):
        if self.nota >= 7:
            print("Aprobó. La nota es: "+ str(self.nota))
        else:
            print("Desaprobó. La nota es: "+ str(self.nota))

# programa principal
alumno1= Alumno()
alumno1.constructor("Sofia", 20, 9)
alumno1.get_nota()


##################
# 8) Realizar un programa en el cual se declaren dos 
# valores enteros por teclado usando el método init. 
# Calcular despuñes la suma, resta, multiplicación y 
# división. Usar un método para cada una e imprimir los
# resultados obtenidos. Llamar a la clase Calculadora

num1 = int
num2 = int
class Calculadora:
    def __init__(self,num1,num2):
        self.num1= num1
        self.num2= num2
    
    def sumar(self):
        return num1+ num2

    def restar(self):
        return num1-num2
    
    def multiplicar(self):
        return num1*num2
    
    def dividir(self):
        return num1/ num2



################

# 10) en un banco tienen clientes que pueden hacer
# depósitos y extracciones de dinero. El banco requiere
# también al final del día calcular la cantidad de dinero
# que se ha depositado. Se deberán crear dos clases, la
# clase cliente y la clase banco. La clase cliente
# tendrá los atributos nombre y cantidad y los métodos
# init depositar, extraer, mostrar_total. La clase banco
# tendrá como atributo 3 obejtos de clase clase cliente
# y los métodos init, operar y deposito_total

class Cliente:
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad

    def depositar(self,monto):
        self.monto+=monto
    
    def extraer(self,monto):
        if self.monto >= monto:
            self.monto-= monto
        else:
            print("Fondos insuficientes para la extracción")

    def mostrar_total(self):
        print("El saldo en la cuenta es "+ self.monto)