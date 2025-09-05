# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

num = 0

while num < 101:
    print(num)
    num = num + 1

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = input("Ingrese un numero entero: ")

cantidad = len(num)

print("El numero",num,"tiene",cantidad,"digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

contador = 0

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

for i in range(num1,num2+1):
    contador = contador + i

print(contador)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = ""
contador = 0
while num != 0:
    num = int(input("Ingrese un numero: "))
    contador = contador + num

print("La suma de los numeros ingresados es de",contador)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random

intentos = 0
random = random.randint(0,9)
num = ""

while random != num:
    print("El numero es incorrecto")
    num = int(input("Ingrese y adivine el numero del 0 al 9: "))
    intentos = intentos + 1

print("Adiviniaste! Tuviste",intentos,"intentos")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100,0,-1):
    if i % 2 == 0:
        print(i)