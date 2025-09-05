contador = 0

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

for i in range(num1,num2+1):
    contador = contador + i

print(contador)