# Ejercicio 1
with open("productos.txt", "w") as productos:
    productos.write("carne,10000,3\n")
    productos.write("leche,1000,5\n")
    productos.write("arroz,750,1\n")

# Ejercicio 2
with open("productos.txt", "r") as productos:
    for linea in productos:
        linea = linea.strip()
        nombre,precio,cantidad = linea.split(",")
        print(f"Productos: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Ejercicio 3
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto: ")
cantidad = input("Ingrese la cantidad del producto: ")

with open("productos.txt", "a") as productos:
    productos.write(f"{nombre},{precio},{cantidad}\n")