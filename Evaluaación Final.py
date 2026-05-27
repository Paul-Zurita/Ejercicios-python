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

for tema in temas:
    print(tema)

cantidad = int(input("\n¿Cuántos estudiantes serán revisados?: "))

for i in range(cantidad):

    print(f"\nEstudiante {i + 1}")

nombre = input("Nombre: ")
ejercicios = float(input("Nota de ejercicios básicos: "))
condicionales = float(input("Nota de condicionales: "))
ciclos = float(input("Nota de ciclos: "))
practicas = int(input("Cantidad de prácticas completadas: "))
