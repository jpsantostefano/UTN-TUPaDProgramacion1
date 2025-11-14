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

# Ejercicio 2
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

# Ejercicio 3
def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} = {resultado}")

# Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal: "))

resultado = decimal_a_binario(numero)
print(f"{numero} en binario es: {resultado}")

