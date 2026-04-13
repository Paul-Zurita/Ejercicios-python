"""
Nombre: Paúl Zurita
Fecha: 12/04/2026
Título: Ejercicios de Variables en Python
"""

# Nivel 1
# %%
nombre = "Paúl"
apellido = "Zurita"
nombreCompleto = "Paúl Zurita"
pais = "Ecuador"
ciudad = "Quito"
edad = 16
año = 2026
estaCasado = False
esVerdadero = True
luzEncendida = False

# Varias variables en una sola línea
a, b, c = 1, 2, 3
# %%
# Nivel 2

# 1. Tipos de datos
print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(estaCasado))
print(type(esVerdadero))
print(type(luzEncendida))
# %%
# 2. Longitud del nombre
print(len(nombre))
# %%
# 3. Comparación de longitudes
print(len(nombre) > len(apellido))
print(len(nombre) < len(apellido))
print(len(nombre) == len(apellido))
# %%
# 4. Números
numeroUno = 5
numeroDos = 4
# %%
# 5-11 Operaciones
total = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
residuo = numeroDos % numeroUno
potencia = numeroUno ** numeroDos
divisionEntera = numeroUno // numeroDos

print(total, diferencia, producto, division, residuo, potencia, divisionEntera)
# %%
# 12-14 Círculo
radio = 30
pi = 3.1416
# %%
areaCirculo = pi * radio ** 2
circunferenciaCirculo = 2 * pi * radio

print(areaCirculo)
print(circunferenciaCirculo)
# %%
# 15. Área con input
radioUsuario = float(input("Ingrese el radio: "))
areaUsuario = pi * radioUsuario ** 2
print("Área:", areaUsuario)
# %%
# 16. Datos del usuario
nombreUsuario = input("Nombre: ")
apellidoUsuario = input("Apellido: ")
paisUsuario = input("País: ")
edadUsuario = input("Edad: ")

print(nombreUsuario, apellidoUsuario, paisUsuario, edadUsuario)
#%%
# 17. Palabras reservadas
help('keywords')