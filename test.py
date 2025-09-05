import random

intentos = 0
random = random.randint(0,9)
num = ""

while random != num:
    print("El numero es incorrecto")
    num = int(input("Ingrese y adivine el numero del 0 al 9: "))
    intentos = intentos + 1

print("Adiviniaste! Tuviste",intentos,"intentos")

