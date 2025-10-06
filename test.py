def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)