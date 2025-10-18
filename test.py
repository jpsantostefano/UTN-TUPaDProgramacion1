agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de Ingles"
}

dia = input("Ingrese el dia que desea consultar: ").lower()
for x in agenda:
    if x[0] == dia:
        hora = input("Ingrese un horario (hh:mm): ")
        if x[1] == hora:
            print(f"Evento: {agenda[x]}")
            break
        else:
            print("No hay eventos para la hora ingresada")
            break
    else:
        print("No hay eventos para el dia ingresado")
        break
    
