class Catalogo:
    peliculas = [] # Esta de objetos de la clase Pelicula
# Constructor de clase
    def __init__(self, peliculas=[]):
     Catalogo.peliculas = peliculas
    
    def agregar(self, p): # p es un objeto Pelicula
     Catalogo.peliculas.append(p)
     
    def mostrar(self):
      for p in Catalogo.peliculas:
       print(p) # Print toma por defecto str(p)