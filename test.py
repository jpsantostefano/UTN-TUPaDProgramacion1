#4 Dada una lista con valores repetidos:
datos = [1,3,5,3,7,1,9,5,3]
# Crear una nueva lista sin elementos repetidos
# Mostrar el resultado
sin_repetir = []
for i in datos:
    if i not in sin_repetir:
        sin_repetir.append(i)

print(sin_repetir)