# # 1) Crear la superclase Vehiculo y las subclases Coche,
# # Bicicleta, Camioneta, Motocicleta


# # necesario para usar clases abstractas
# # from ABC import ABC, abstractmethod

# # declaración de clases


# class Vehiculo(ABC):
#     # Constructor
#     def __init__(self, color, ruedas):
#         self._color = color
#         self._ruedas = ruedas
#     def __str__(self):
# 	    print("Color:  {self._color}, ruedas: {self._ruedas}")



# class Coche(Vehiculo):
#     def __init__(self, velocidad, cilindrada):
#         self._velocidad = velocidad
#         self._cilindrada = cilindrada


# class Bicicleta(Vehiculo):
#     def _init__(self, tipo):
#         self._tipo = tipo
#     def __str__(self):
# 	    print("Tipo:  {self._tipo}")



# class Camioneta(Coche):
#     def __init__(self, carga):
#         self._carga = carga
#     def __str__(self):
# 	    print("Carga:  {self._carga}")



# class Motocicleta(Bicicleta):
#     def __init__(self, velocidad, cilindrada):
#         self._velocidad = velocidad
#         self._cilindrada = cilindrada
#     def __str__(self):
# 	    print("Velocidad:  {self._velocidad}, cilindrada: {self._cilindrada}")

# #### FUNCIONES

# # 2) Realizar una función llamada catalogar() que reciba
# # la lista de vehiculos y los recorra mostrando el nombre
# # de la clase y sus atributos
# def catalogar(lista):
#     for obj in lista:
#         print(type(obj).name)
#         print(obj.__str__())



# # programa principal
# # crear un objeto de cada subclase y agregarlos a una lista
# camioneta1 = Camioneta(4000)
# motocicleta1 = Motocicleta(30, 399)
# coche1 = Coche(200, 45)
# bicicleta1 = Bicicleta("Urbana")


# medios=[]
# medios.append(camioneta1)
# medios.append(motocicleta1)
# medios.append(coche1)
# medios.append(bicicleta1)
# catalogar(medios)