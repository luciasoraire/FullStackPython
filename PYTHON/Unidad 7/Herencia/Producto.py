#harina, jabon para la ropa,leche,carne

class Producto:
    def __init__(self,cod,nom,precio,descripcion):
        self.codigo=cod
        self.nombre=nom
        self.precio=precio
        self.descripcion=descripcion
    
    def __str__(self):
        
        return f"Codigo de producto:\t{self.codigo}\n"\
               f"Nombre:\t{self.nombre}\n"\
               f"Precio:\t{self.precio}\n"\
               f"Descripción:\t{self.descripcion}\n"
               

producto1=Producto("45","Jabon","$250","Frutal")

print(producto1)