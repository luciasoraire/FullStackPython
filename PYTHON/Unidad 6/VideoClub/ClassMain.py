from Catalogo import Catalogo
from Pelicula import Pelicula


#Instanciamos una película
peli1 = Pelicula("El Padrino", 175, 1972)
# Instanciamos un catálogo que contiene una pelicula
c = Catalogo([peli1])
c.mostrar()
# Añadimos una nueva película al catálogo:
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))
c.mostrar()