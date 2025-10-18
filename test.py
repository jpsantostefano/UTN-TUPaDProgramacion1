productos = {
    "banana": 10,
    "manzana": 5,
    "naranja": 3
    }

consulta = input("Ingrese un producto para saber su stock: ").lower()

if consulta in productos:
    print(f"{consulta}: {productos[consulta]} unidades")

    modificar = input("Deseas agregar unidades? (s/n): ").lower()
    if modificar == "s":
        unidades = int(input("Cuantas unidades deseas agregar al stock?: "))
        productos[consulta] += unidades
        print("Stock actualizado con exito!")
        print(f"{consulta}: {productos[consulta]} unidades")

else:
    print(f"No hay stock de {consulta}")
    agregar = input("Deseas agregar este producto? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input(f"Ingresa la cantidad que deseas agregar de {consulta} al stock: "))
        productos[consulta] = cantidad
        print("Producto agregado con exito!")

