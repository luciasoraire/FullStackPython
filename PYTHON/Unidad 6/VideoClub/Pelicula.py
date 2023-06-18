class Pelicula:
# Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
     self.titulo = titulo
     self.duracion = duracion
     self.lanzamiento = lanzamiento
     print(f'Se ha creado la película: {self.titulo}')


    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'