#%%

#%%
i = 0
cantidad = int(input("Cuantos alumnos deseas ingresar: "))
while i < cantidad + 1:
    def mostrar_estudiante (nombre,curso):
    print ("=== DATOS DEL ESTUDIANTE ===")
    print (f"Nombre : {nombre}")
    print (f"curso: {curso}")
nombre_usuario= input("Ingrese el nombre del estudiante: ")
curso_usuario= input("Ingrese el curso del estudiante: ")
mostrar_estudiante (nombre_usuario, curso_usuario)