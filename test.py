def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None
    return (suma, resta, multiplicacion, division)

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))

resultados = operaciones_basicas(num1,num2)

print(f"{num1} + {num2} = {resultados[0]}")
print(f"{num1} - {num2} = {resultados[1]}")
print(f"{num1} X {num2} = {resultados[2]}")
if resultados[3] is not None:
    print(f"{num1} / {num2} = {resultados[3]}")
else:
    print("No se puede dividir por cero")