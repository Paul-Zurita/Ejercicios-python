#Actividad 3 
#14/04/2026
# # 1 y 2
#%%
edad = 20
estatura = 1.75
#%%
print("Edad:", edad)
print("Estatura:", estatura)
#%%
# 3. Área de triángulo
base = float(input("\nIngrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = 0.5 * base * altura
print("Área del triángulo:", area_triangulo)

# 5. Perímetro de triángulo
a = float(input("\nIngrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))
perimetro_triangulo = a + b + c
print("Perímetro del triángulo:", perimetro_triangulo)

# 6. Rectángulo
longitud = float(input("\nIngrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
area_rect = longitud * ancho
perimetro_rect = 2 * (longitud + ancho)
print("Área del rectángulo:", area_rect)
print("Perímetro del rectángulo:", perimetro_rect)

# 7. Círculo
radio = float(input("\nIngrese el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo:", area_circulo)
print("Circunferencia:", circunferencia)

# 9. Pendiente y distancia
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("\nPendiente:", pendiente)
print("Distancia:", distancia)

# 11. Función
print("\nValores de la función y = x^2 + 6x + 9")
for x in range(-10, 1):
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")
print("Cuando x = -3, y = 0")

# 12. Longitud palabras
print("\nComparación de longitudes:")
print(len("python") == len("dragon"))

# 13 y 15
print("\n'on' en ambas palabras:")
print("on" in "python" and "on" in "dragon")

# 14
oracion = "Espero que este curso no esté lleno de jerga."
print("\n¿'jerga' está en la oración?")
print("jerga" in oracion)

# 16
longitud = len("python")
valor = str(float(longitud))
print("\nConversión:", valor)

# 18
print("\nDivisión entera:")
print(7 // 3 == int(2.7))

# 19
print("\nComparación de tipos:")
print(type("10") == type(10))

# 20
print("\nConversión de '9.8':")
print(int(float('9.8')) == 10)

# 21. Pago
horas = float(input("\nHoras trabajadas: "))
tarifa = float(input("Tarifa por hora: "))
print("Pago total:", horas * tarifa)

# 22. Segundos vividos
años = int(input("\nAños vividos: "))
segundos = años * 365 * 24 * 60 * 60
print("Segundos vividos:", segundos)

# 23. Tabla
print("\nTabla:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)