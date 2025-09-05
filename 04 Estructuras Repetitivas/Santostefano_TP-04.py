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


