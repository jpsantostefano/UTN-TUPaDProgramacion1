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
