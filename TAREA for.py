notas = [8.5, 6.0, 9.0, 7.0, 5.5]

suma = 0
aprobados = 0
reprobados = 0
cantidad = 0

for nota in notas:
    suma = suma + nota
    cantidad = cantidad + 1

    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

promedio = suma / cantidad

print("Suma total:", suma)
print("Promedio:", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("------------------------------------")
contrasena = "Python2026"

letras = 0
numeros = 0
contador_o = 0

for caracter in contrasena:

    if caracter.isalpha():
        letras = letras + 1

    if caracter.isdigit():
        numeros = numeros + 1

    if caracter == "o":
        contador_o = contador_o + 1

print("Cantidad de letras:", letras)
print("Cantidad de números:", numeros)
print("Cantidad de o:", contador_o)
print("------------------------------------")
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}

productos_unicos = 0
mas_de_6 = 0

for producto in productos:
    productos_unicos = productos_unicos + 1

    contador = 0

    for letra in producto:
        contador = contador + 1

    if contador > 6:
        mas_de_6 = mas_de_6 + 1

print("Productos únicos:", productos_unicos)
print("Productos con más de 6 letras:", mas_de_6)
print("------------------------------------")
correo = input("Ingrese su correo: ")

usuario = ""

for caracter in correo:

    if caracter == "@":
        break

    usuario = usuario + caracter

print("Usuario:", usuario)
print("------------------------------------")
telefono = input("Ingrese el número de teléfono: ")

telefono_limpio = ""

for caracter in telefono:

    if caracter == " " or caracter == "-":
        continue

    telefono_limpio = telefono_limpio + caracter

print("Teléfono limpio:", telefono_limpio)