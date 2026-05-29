def mostrar_estudiante (nombre, curso):
    print ("=== DATOS DEL ESTUDIANTE ===")
    print (f"nombre: {nombre}")
    print (f"curso: {curso}")
nombre_usuario= input("Ingrese el nombre del estudiante: ")
curso_usuario= input("Ingrese el curso del estudiante: ")
mostrar_estudiante (nombre_usuario, curso_usuario)
def saludar(nombre):
    print(f"{nombre}")
saludar('Ana')