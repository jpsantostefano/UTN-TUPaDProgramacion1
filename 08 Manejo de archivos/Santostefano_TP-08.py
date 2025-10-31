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