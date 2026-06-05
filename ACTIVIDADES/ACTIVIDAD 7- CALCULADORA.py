def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
while True:
    print("------SELECCIONE UNA OPERACION------")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    opcion = int(input("Selecciona una de la opciones (1-5): "))
    if opcion == 1:
        resultado = suma(num1, num2)
        print("Resultado:", resultado)
    elif opcion == 2:
        resultado = resta(num1, num2)
        print("Resultado:", resultado)
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
        print("Resultado:", resultado)
    elif opcion == 4:
        resultado = division(num1, num2)
        print("Resultado:", resultado)
    elif opcion ==5:
        print("gracias por usa la calcu")
        break
    else:
        resultado = "Opción no válida"

