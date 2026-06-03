def suma(a, b):
    print("Resultado:", a + b)
def resta(a, b):
    print("Resultado:", a - b)
def multiplicacion(a, b):
    print("Resultado:", a * b)
def division(a, b):
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: No se puede dividir entre cero")
def potencia(a, b):
    print("Resultado:", a ** b)
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("------SELECCIONE UNA OPERACION------")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")
print("5. Potencia (^)")
opcion = int(input("Ingrese una opción (1-5): "))
if opcion == 1:
    suma(num1, num2)
elif opcion == 2:
    resta(num1, num2)
elif opcion == 3:
    multiplicacion(num1, num2)
elif opcion == 4:
    division(num1, num2)
elif opcion == 5:
    potencia(num1, num2)
else:
    print("Opción no válida")