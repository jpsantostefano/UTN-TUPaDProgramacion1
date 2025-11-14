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

# Ejercicio 5
def es_palindrome(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindrome(palabra[1:-1])

palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()

resultado = es_palindrome(palabra)
print(f"¿'{palabra}' es un palíndromo? {resultado}")

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))

resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques_base = int(input("Ingrese el número de bloques en el nivel base: "))

resultado = contar_bloques(bloques_base)
print(f"El total de bloques necesarios para la pirámide es: {resultado}")

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}")