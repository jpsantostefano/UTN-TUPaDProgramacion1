def caclular_imc(peso,altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros"))

imc = caclular_imc(peso,altura)
print(f"Tu indice de masa corporal es de: {imc:.2f}")