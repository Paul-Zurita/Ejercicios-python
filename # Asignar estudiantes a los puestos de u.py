# Asignar estudiantes a los puestos de un laboratorio
# El laboratorio tiene 3 filas y 4 computadoras por cada fila

for fila in range(1, 4):
    for computadora in range(1, 5):
        nombre = input('Ingrese el nombre del estudiante: ')
        print(nombre, 'asignado a Fila', fila,'- Computadora', computadora)

    print('Fin de la fila', fila)