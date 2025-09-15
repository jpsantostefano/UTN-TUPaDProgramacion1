nombres = ["Juan", "Fernanda", "Maria", "Pedro", "Martin", "Daira", "Zoe", "Lucas"]

print(nombres)
respuesta = input("Desea agregar (A) o eliminar (E) un alumno existente?: ")
if respuesta.upper() == "A":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    nombres.append(nuevo)
elif respuesta.upper() == "E":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    nombres.remove(eliminar)

print("La lista actualizada es:",nombres)