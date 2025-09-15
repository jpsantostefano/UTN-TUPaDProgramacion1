import random

lista = []
pares = []
impares = []
for i in range(15):
    lista.append(random.randint(1,100))

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

cant_impar = len(impares)
cant_par = len(pares)
print("Los 15 numeros seleccionados al azar del 1 al 100 son:",lista)
print("La cantidad de numeros impares es:",cant_impar,".Estos son:",impares)
print("Los cantidad de numeros pares es:",cant_par,". Estos son: ",pares)