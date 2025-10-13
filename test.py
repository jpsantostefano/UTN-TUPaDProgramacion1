parcial1 = {"Juan", "Maria", "Pedro", "Gabriel"}
parcial2 = {"Josefina", "Taylor", "Juan", "Gabriel"}

ambos_aprobados = []
uno_aprobado = []

for nombre1 in parcial1:
    for nombre2 in parcial2:
        if nombre1 in parcial2:
            ambos_aprobados.append(nombre1)
        if nombre2 not in parcial1:
            uno_aprobado.append(nombre2)

total = list(set(list(parcial1) + uno_aprobado))

print(f"Alumnos que aprboaron ambos parciales: {ambos_aprobados}")
print(f"Alumnos que aprobaron al menos un parcial: {uno_aprobado}")
print(f"Total de estudiantes que aprobaron al menos un parcial: {total}")