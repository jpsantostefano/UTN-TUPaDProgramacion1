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

# Ejercicio 7
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

# Ejercicio 8

productos = {
    "banana": 10,
    "manzana": 5,
    "naranja": 3
    }

consulta = input("Ingrese un producto para saber su stock: ").lower()

if consulta in productos:
    print(f"{consulta}: {productos[consulta]} unidades")

    modificar = input("Deseas agregar unidades? (s/n): ").lower()
    if modificar == "s":
        unidades = int(input("Cuantas unidades deseas agregar al stock?: "))
        productos[consulta] += unidades
        print("Stock actualizado con exito!")
        print(f"{consulta}: {productos[consulta]} unidades")

else:
    print(f"No hay stock de {consulta}")
    agregar = input("Deseas agregar este producto? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input(f"Ingresa la cantidad que deseas agregar de {consulta} al stock: "))
        productos[consulta] = cantidad
        print("Producto agregado con exito!")

# Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de Ingles"
}

dia = input("Ingrese el dia que desea consultar: ").lower()
for x in agenda:
    if x[0] == dia:
        hora = input("Ingrese un horario (hh:mm): ")
        if x[1] == hora:
            print(f"Evento: {agenda[x]}")
            break
        else:
            print("No hay eventos para la hora ingresada")
            break
    else:
        print("No hay eventos para el dia ingresado")
        break

# Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)