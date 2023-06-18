# DICCIONARIOS matrices asociativas
# Ejemplos de diccionarios, clave, valor

{} 			                # diccionario vacío
{'Juan': 56}			    # diccionario de un elemento
{'Juan': 56, 'Ana': 15}     # diccionario de dos elementos

# # Creación: Por extensión
# diccionario  = {'Juan': 56, 'Ana': 15}
# # Creación: Por compresión
# diccionario  = {x: x ** 2 for x in (2, 4, 6)}
# print(diccionario)
# Acceso
diccionario = {1: 'uno', 2:'dos', 3:'tres'}
print(diccionario.keys())


# for i in diccionario.keys():
#     print(diccionario[i])    
# for clave, valor in diccionario.items():
#     print(clave, ':', valor, end= '; ')


d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)

d1['Nombre'] = "Laura"
print(d1)
