# Funciones

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def nota_mayor(n1, n2, n3):
    return max(n1, n2, n3)

def nota_menor(n1, n2, n3):
    return min(n1, n2, n3)

def estado_estudiante(n1, n2, n3):
    promedio = calcular_promedio(n1, n2, n3)
    if promedio >= 7:
        return "Aprueba"
    else:
        return "Reprueba"

# Entrada de datos
nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))

# Menú
print("\nMENÚ DE OPCIONES")
print("1. Calcular el promedio")
print("2. Mostrar la nota mayor")
print("3. Mostrar la nota menor")
print("4. Determinar si aprueba o reprueba")

opcion = int(input("Seleccione una opción: "))

# Procesamiento
if opcion == 1:
    print("Promedio:", calcular_promedio(nota1, nota2, nota3))
elif opcion == 2:
    print("Nota mayor:", nota_mayor(nota1, nota2, nota3))
elif opcion == 3:
    print("Nota menor:", nota_menor(nota1, nota2, nota3))
elif opcion == 4:
    print("Estado:", estado_estudiante(nota1, nota2, nota3))
else:
    print("Opción no válida.")