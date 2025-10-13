alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese nombre de alumno {i+1}: ")
    notas = []
    
    for x in range(3):
        nota = float(input(f"Ingrese una nota {x+1}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")


