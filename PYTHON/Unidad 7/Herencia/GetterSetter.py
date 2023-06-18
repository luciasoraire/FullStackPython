class Persona:
    def __init__(self,nombre,apellido,edad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre
        
        
persona1=Persona("Lola","Mora",34)
print(persona1.getNombre())
persona1.setNombre("Ana")
print(persona1.getNombre())
persona2=Persona("Pepe","Argento",65)
