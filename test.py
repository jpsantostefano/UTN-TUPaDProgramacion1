def calcular_promedio(a,b,c):
    return (a+b+c) / 3

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = calcular_promedio(nota1, nota2, nota3)

print(f"El promedio total es de: {promedio}")