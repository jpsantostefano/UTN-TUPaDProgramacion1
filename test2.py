contador = 0
pares = 0
impares = 0
positivo = 0
negativo = 0

while contador < 100:
    num = int(input("Ingrese un numero (0 para terminar): "))
    if num == 0:
        break
    else:
        contador = contador + 1
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
        if num > 0:
            positivo = positivo + 1
        else:
            negativo = negativo + 1
    

print("Pares:",pares)
print("Impares:",impares)
print("Positivos:",positivo)
print("Negativos:",negativo)