#1 Crear una lista con las notas de 10 estudiantes
# Mostrar la lista completa
# Calcular y mostrar el promedio
# Indicar la nota mas alta y la mas baja.
notas = [4,10,8,6,7,6,9,10,2,8]

print("La lista completa de notas es:",notas)

suma = 0
alta = float("-inf")
baja = float("inf")
for i in notas:
    suma = suma + i
    if alta < i:
        alta = i
    if baja > i:
        baja = i
promedio = suma / len(notas)
print("El promedio de todas las notas es",promedio)
print("La nota mas baja es:",baja)
print("La nota mas alta es:",alta)

#2 Pedir al usuario que cargue 5 productos en una lista
# Mostrar la lista ordenada alfabeticamente. Investigue el uso del metodo sorted*()
# Preguntar al usuario que producto desea eliminar y actualizar la lista.

lista_productos = []
for i in range(5):
    producto = input("Ingrese un producto: ")
    lista_productos.append(producto)

print(sorted(lista_productos))

eliminar_producto = input("Que producto deseas eliminar de la lista?")
lista_productos.remove(eliminar_producto)

print(sorted(lista_productos))

#3 Generar una lista con 15 numeros enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares
# Mostrar cuantos numeros tiene cada lista
import random

lista = []
pares = []
impares = []
for i in range(15):
    lista.append(random.randint(1,100))

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

cant_impar = len(impares)
cant_par = len(pares)
print("Los 15 numeros seleccionados al azar del 1 al 100 son:",lista)
print("La cantidad de numeros impares es:",cant_impar,".Estos son:",impares)
print("Los cantidad de numeros pares es:",cant_par,". Estos son: ",pares)

#4 Dada una lista con valores repetidos:
datos = [1,3,5,3,7,1,9,5,3]
# Crear una nueva lista sin elementos repetidos
# Mostrar el resultado
sin_repetir = []
for i in datos:
    if i not in sin_repetir:
        sin_repetir.append(i)

print(sin_repetir)

#5 Crear una lista con los nombres de 8 estudiantes presentes en clase.
# Preguntar al usuario si queire agregar un nuevo estudiante o eliminar uno existente
# Mostrar la lista final actualizada

nombres = ["Juan", "Fernanda", "Maria", "Pedro", "Martin", "Daira", "Zoe", "Lucas"]

print(nombres)
respuesta = input("Desea agregar (A) o eliminar (E) un alumno existente?: ")
if respuesta.upper() == "A":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    nombres.append(nuevo)
elif respuesta.upper() == "E":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    nombres.delete(eliminar)

print("La lista actualizada es:",nombres)

#6 Dada una lista con 7 numeros, rotar todos los elementos una posicion hacia la derecha (el ultimo pasa a ser el primero)
lista = [1,2,3,4,5,6,7]

lista_rotada = [lista[-1]] + lista[:-1]
print(lista_rotada)

#7 Crear una matriz (lista anidada) de 7x2 con las temperaturas minimas y maximas de una semana.
# Calcular el promedio de las minimas y el de las maximas
# Mostrar en que dia se registro la mayor amplitud termica.

temperaturas = [
    [15, 25],
    [14, 24],
    [16, 26],
    [13, 23],
    [17, 27],
    [15, 25],
    [16, 28]
]

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
minima = 0
maxima = 0
amplitud = 0
amplitud_max = 0
dia_amplitud = 0

for i in range(len(temperaturas)):
    minima = minima + temperaturas[i][0]
    maxima = maxima + temperaturas[i][1]
    amplitud = temperaturas[i][1] - temperaturas[i][0]

    if amplitud > amplitud_max:
        amplitud_max = amplitud
        dia_amplitud = i

promedio_min = minima / len(temperaturas)
promedio_max = maxima / len(temperaturas)
print(f"El promedio de las temperaturas minimas es de: {promedio_min:.1f} grados")
print(f"El promedio de las temperaturas maximas es de: {promedio_max:.1f} grados")
print(f"La amplitud maxima fue de {amplitud_max} grados el dia {dias[dia_amplitud]}")

# 8 Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia

# Lengua, Matematica, Historia

notas = [
    [7, 8, 6],
    [9, 7, 8],
    [6, 5, 7],
    [8, 9, 9],
    [7, 6, 8]
]

suma_lengua = 0
suma_matematica = 0
suma_historia = 0

for i in range(len(notas)):
    promedio_estudiante = (notas[i][0] + notas[i][1] + notas[i][2]) / 3
    print(f"El promedio del estudiante {i+1} es de {promedio_estudiante:.2f}")
    suma_lengua += notas[i][0]
    suma_matematica += notas[i][0]
    suma_historia += notas[i][0]

promedio_lengua = suma_lengua /5
promedio_matematica = suma_matematica / 5
promedio_historia = suma_historia / 5

print(f"El promedio de Lengua es de {promedio_lengua:.2f}")
print(f"El promedio de Matematica es de {promedio_matematica:.2f}")
print(f"El promedio de Historia es de {promedio_historia:.2f}")

# 9 Representar un tablero de Ta-Te-Ti como una lista de listas (3x3)
# Inicializarlo con guinoes "-" representando casillas vacias.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O"
# Mostrar el tablero despues de cada jugada.

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

print("***Tablero Inicial***")
for f in tablero:
        print(" ".join(f))
print()

jugador = "X"
jugadas = 0

while jugadas < 9:
    print("Turno del jugador:", jugador)
    fila = int(input("Ingrese numero de fila (1-3): ")) -1
    columna = int(input("Ingrese numero de columna (1-3): ")) -1

    tablero[fila][columna] = jugador
    jugadas += 1

    for f in tablero:
        print(" ".join(f))
    print()

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

print("Juego terminado!")

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