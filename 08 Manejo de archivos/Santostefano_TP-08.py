# Ejercicio 1
with open("08 Manejo de archivos/productos.txt", "w") as productos:
    productos.write("carne,10000,3\n")
    productos.write("leche,1000,5\n")
    productos.write("arroz,750,1\n")

# Ejercicio 2
with open("08 Manejo de archivos/productos.txt", "r") as productos:
    for linea in productos:
        linea = linea.strip()
        nombre,precio,cantidad = linea.split(",")
        print(f"Productos: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Ejercicio 3
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto: ")
cantidad = input("Ingrese la cantidad del producto: ")

with open("08 Manejo de archivos/productos.txt", "a") as productos:
    productos.write(f"{nombre},{precio},{cantidad}\n")

# Ejercicio 4
productos = []

with open("08 Manejo de archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Ejercicio 5
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: {producto}")
        encontrado = True
        break

if not encontrado:
    print(f"El producto '{nombre_buscar}' no se encuentra en la lista")

# Ejercicio 6
with open("08 Manejo de archivos/productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo actualizado correctamente")
