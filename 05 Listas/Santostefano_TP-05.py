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

