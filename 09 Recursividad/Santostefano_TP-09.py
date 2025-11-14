# Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    resultado = factorial(i)
    print(f"Factorial de {i} es: {resultado}")