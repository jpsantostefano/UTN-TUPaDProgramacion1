# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Ejercicio 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Ejercicio 3
frutas_sin_precio = list(precios_frutas.keys())

# Ejercicio 4
contactos = {}
print("Ingrese 5 contactos con su nombre y telefono")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    contactos[nombre] = None
    telefono = input("Numero telefonico: ")
    contactos[nombre] = telefono

nombre = input("Ingresa nombre de contacto para ver si existe: ")
if nombre in contactos.keys():
    print(f"El telefono de {nombre} es {contactos[nombre]}")
else:
    print("El contacto ingresado no existe")

# Ejercicio 5
recuento = {}
frase = input("Ingrese una frase: ")

for palabra in frase.split():
    if palabra not in recuento.keys():
        recuento[palabra] = 1
    else:
        recuento[palabra] += 1

palabras_unicas = set(frase.split())

print(f"Palabras unicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

# Ejercicio 6
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