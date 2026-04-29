nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
puntaje = float(input("Ingrese su puntaje: "))
asistencia = float(input("Ingrese su asistencia: "))
codigo = input("Ingrese el código de invitación: ")
nombre_mayus = nombre.upper()
caracteres = len(nombre.replace(" ", ""))
promedio = (puntaje + asistencia) / 2
if edad >= 14:
    if promedio >= 80:
        if codigo == "PYTHON2026":
            resultado = "Acceso VIP"
        else:
            resultado = "Acceso general"
    elif promedio >= 60:
        resultado = "Acceso con observación"
    else:
        resultado = "No puede ingresar por bajo rendimiento"
else:
    if codigo == "PYTHON2026":
        resultado = "Acceso especial con acompañante"
    else:
        resultado = "No cumple la edad mínima"

if puntaje >= 90 and asistencia >= 90:
    mensaje = "Candidato destacado"
elif puntaje < 50 or asistencia < 50:
    mensaje = "Requiere refuerzo previo"
else:
    mensaje = "Sin observaciones adicionales"

print("--- RESUMEN ---")
print("Participante:", nombre_mayus)
print("Caracteres del nombre:", caracteres)
print("Promedio general:", promedio)
print("Resultado:", resultado)
print("Mensaje adicional:", mensaje)