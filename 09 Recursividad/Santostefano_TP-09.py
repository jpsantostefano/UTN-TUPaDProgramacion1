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

#Ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

posicion = int(input("Ingrese la posición hasta la que quiera mostrar la serie Fibonacci: "))

print("Serie de Fibonacci completa:")
for i in range(posicion + 1):
    resultado = fibonacci(i)
    print(f"Posición {i}: {resultado}")

