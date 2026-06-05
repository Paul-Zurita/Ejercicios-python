#%%

def mostrar_estudiante(nombre, curso):
    print("=== DATOS DEL ESTUDIANTE ===")
    print(f"Nombre: {nombre}")
    print(f"Curso: {curso}")

i = 0
cantidad = int(input("¿Cuántos alumnos deseas ingresar?: "))

while i < cantidad:
    nombre_usuario = input("Ingrese el nombre del estudiante: ")
    curso_usuario = input("Ingrese el curso del estudiante: ")

    mostrar_estudiante(nombre_usuario, curso_usuario)

    i += 1