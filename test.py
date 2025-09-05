# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

suma = 0
num = int(input("Ingrese un numero entero positivo: "))

for i in range(0,num+1):
    suma = suma + i

print("La suma de todos los numeros comprendidos entre 0 y",num,"es igual a",suma)

