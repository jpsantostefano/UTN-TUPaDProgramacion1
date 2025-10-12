recuento = {}
frase = input("Ingrese una frase: ")

for palabra in frase.split():
    if palabra not in recuento.keys():
        recuento[palabra] = 1
    else:
        recuento[palabra] += 1

palabras_unicas = set(frase.split())

print(f"Palabras unicas: {palabras_unicas}")
print(f"Recuento: {recuento}")
