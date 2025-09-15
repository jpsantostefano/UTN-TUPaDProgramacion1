lista_productos = []
for i in range(5):
    producto = input("Ingrese un producto: ")
    lista_productos.append(producto)

print(sorted(lista_productos))

eliminar_producto = input("Que producto deseas eliminar de la lista?: ")
lista_productos.remove(eliminar_producto)

print(sorted(lista_productos))