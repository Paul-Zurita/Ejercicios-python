
def obtener_mensaje(mensaje_personalizado):
    return mensaje_personalizado

def generar_nombre_completo(nom, ape):
    espacio = ' '
    nombre_completo = nom + espacio + ape
    return nombre_completo

mensaje_usuario = input("Ingresa el mensaje de bienvenida que deseas mostrar: ")
nombre_usuario = input("Por favor, ingresa tu nombre: ")
apellido_usuario = input("Por favor, ingresa tu apellido: ")


bienvenida = obtener_mensaje(mensaje_usuario)
resultado_nombre = generar_nombre_completo(nombre_usuario, apellido_usuario)
print(bienvenida)
print(resultado_nombre)