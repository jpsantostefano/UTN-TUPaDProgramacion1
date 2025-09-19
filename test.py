#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# - Mostrar el total vendido por cada producto.
# - Mostrar el día con mayores ventas totales.
# - Indicar cuál fue el producto más vendido en la semana.

productos = ["Carne", "Pollo", "Queso", "Pepsi"]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

ventas = [
    [5, 8, 6, 4, 7, 3, 9],   # Carne
    [2, 4, 3, 5, 6, 8, 7],   # Pollo
    [9, 7, 8, 6, 5, 4, 10],  # Queso
    [3, 6, 4, 7, 5, 9, 8]    # Pepsi
]

# 1. Total vendido por cada producto
totales_productos = []
print("Total vendido por cada producto:")
for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]
    totales_productos.append(total)
    print(f"{productos[i]}: {total}")

# 2. Día con mayores ventas totales
ventas_dias = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    ventas_dias.append(total_dia)

# Encontrar el día con mayor venta
max_ventas = ventas_dias[0]
indice_max = 0
for i in range(7):
    if ventas_dias[i] > max_ventas:
        max_ventas = ventas_dias[i]
        indice_max = i

print(f"Día con mayores ventas: {dias[indice_max]} con {max_ventas} ventas")

# 3. Producto más vendido en la semana
max_producto = totales_productos[0]
indice_max_producto = 0
for i in range(4):
    if totales_productos[i] > max_producto:
        max_producto = totales_productos[i]
        indice_max_producto = i

print(f"Producto más vendido en la semana: {productos[indice_max_producto]}")
