clave_correcta = "python123"
clave = ""

while clave != clave_correcta:
    clave = input("Ingrese la clave: ")

    if clave != clave_correcta:
        print("Clave incorrecta")

print("Acceso permitido")
print("Bienvenido al sistema")
temas = ["variables","cálculos","input","print","f-string","condicionales","ciclos"]
print (temas)
cantidad = int(input("\n¿Cuántos estudiantes serán revisados?: "))

for i in range(cantidad):
    print(f"\nEstudiante {i + 1}")
    
    # Esto evita que se salte el Estudiante 1 si la consola tiene un 'Enter' guardado
    nombre = input("Nombre: ").strip()
    while not nombre:
        nombre = input("Nombre: ").strip()
        
    ejercicios = float(input("Nota de ejercicios básicos: "))
    condicionales = float(input("Nota de condicionales: "))
    ciclos = float(input("Nota de ciclos: "))
    practicas = int(input("Cantidad de prácticas completadas: "))
    promedio = (ejercicios + condicionales + ciclos) / 3

# Clasificación
    if promedio >= 9:
        if practicas >= 5:
            estado = "Habilitado con nivel alto"
        else:
            estado = "Pendiente por prácticas"
    elif promedio >= 7:
        if practicas >= 4:
            estado = "Habilitado"
        else:
            estado = "Pendiente por prácticas"
    else:
        estado = "Requiere refuerzo"

    # CORRECCIÓN: Estos prints ahora están fuera del 'else', alineados con el 'if'
    print("--- REPORTE ---")
    print(f"Nombre: {nombre}")
    print(f"Promedio final: {promedio}")
    print(f"Prácticas completadas: {practicas}")
    print(f"Estado académico: {estado}")