#Actividad 1
print("Hola Mundo!")

#Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {lugar}")

#Actividad 4
pi = 3.14
radio = float(input("Ingresa el radio del circulo: "))
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"El area del circulo es de: {area}")
print(f"El perimetro del circulo es de: {perimetro}")

#Actividad 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivale a {horas} horas")

#Actividad 6
numero = int(input("Ingrese un número: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Actividad 7
num1 = int(input("Ingrese un numero distinto a 0: "))
num2 = int(input("Ingrese otro numero distinto a 0: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multi}")
print(f"{num1} / {num2} = {division}")

#Actividad 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura**2)

print(f"Tu indice de masa corporal es de: {imc}")

#Actividad 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
farenheit = (celsius * 9/5) + 32

print(f"{celsius} grados Celsius equivalen a {farenheit} grados Farenheit")

#Actividad 10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres numeros es de: {promedio}")