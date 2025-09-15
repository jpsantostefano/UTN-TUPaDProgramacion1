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


