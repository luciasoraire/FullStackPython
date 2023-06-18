from Producto import Producto

class Alimento(Producto):
      def __init__(self,cod,nombre,precio,descripcion,marca,categoria):
          super().__init__(cod,nombre,precio,descripcion)
          self.marca=marca
          self.categoria=categoria
          
      def __str__(self):
          
          return super().__str__() + f"Marca:\t {self.marca}\n"\
              f"Categoria:\t {self.categoria}\n"
          
          