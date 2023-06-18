x = 10
print(type(x))
print(id(x)) # 4349704528
def funcion(entrada):
    entrada=0
    print(id(x)) # 4349704208
funcion(x)
print(x)

#lista pasaje por referencia
x = [10, 20, 30]
print(id(x)) # 4422423560
def funcion(entrada):
    entrada.append(40)
    
    print(id(entrada)) # 4422423560

funcion(x)
print(x)