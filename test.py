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