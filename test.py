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