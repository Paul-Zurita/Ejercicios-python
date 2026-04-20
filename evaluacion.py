# ===== PARTE A =====
# Respuesta 1:
#1. Análisis de datos y código (15 puntos)
#Observa el siguiente código:
nombre = "Lucía"
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))
#a) Indica el tipo de dato de cada variable.
#Respuestas:
#nombre -> str
#edad -> int
#promedio -> float
#cursos-> lista e str

#b) Escribe qué mostraría el programa en pantalla.
#Respuesta: 
#mostraria el tipo de varible más no la variable en si

#c) Explica qué hace len(nombre).
#Respuesta:
#lee la cantidad e caracteres (Inlcuyendo espacios) de la variable asignada

#2. Comprensión conceptual (15 puntos)
#Responde con tus palabras:
#a) ¿Qué diferencia hay entre print() e input()?
#Respuesta:
#La función print unicamente muestra el caracter / variable deseados, mientras que input pide interaccion con el usuario 

#b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
#Respuesta:
#

#c) Explica la diferencia entre /, // y %.
#Respuesta:
# "/" se refiere a una division, "//" se refiere a una divsion que unicamente nos da la respuesta sin decimales, mientras que "%" se refiere al residuo que queda en una division 

#d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
#Respuesta:
#

#e) Escribe una instrucción que permita consultar las palabras reservadas de Python
#Respuesta:
#"help"

# ===== PARTE B =====
# Código corregido
#3. Corrección de código (15 puntos)
#El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione.

#REESCRITO:
ancho = int(input("Ingrese el ancho del terreno: "))
largo = int(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio del terreno: "))
area = ancho * largo 
costo = area * precio 
print (f"Área total: {area}")
print (f"Costo estimado: {costo}")
#Luego responde:
#a) ¿Cuáles eran los errores principales?
#Respuesta:
#No estaban declarado el tipo de dato de los inputs por lo que el sistema no sabria que hacer

#b) ¿Por qué tu corrección sí permite obtener resultados válidos?
#Respuesta:
#Porque le estoy dando instrucciones precisas y legibles para el computador que ejecute

#4. Construcción breve (15 puntos)
#Escribe un fragmento de código que haga lo siguiente:
#1. Cree la variable frase con el texto "Tecnología para todos".
variable = "Tecnología para todos"
#2. Muestre la frase en mayúscula
variable_mayusculas = variable.upper()
print (variable_mayusculas)
#3. Muestre la cantidad de caracteres de la frase.
print (len(variable))
#4. Verifique si la palabra "Python" está dentro de la frase.
if "Python" in variable.lower():
    print("La palabra 'Python' está presente.")
#5. Reemplace "Tecnología" por "Programación".
remplazo = variable.replace("tecnologia", "Programacion")
print (remplazo)
#6. Divida la frase en palabras usando split(). 
divido = variable.split()
print (divido)
#%%
# ===== PARTE C =====
# Programa integrador
# Una tienda desea generar un resumen de presupuesto para cubrir una pared rectangular con papel decorativo.
# 5. Desarrolla un programa (40 puntos)

nombre = str(input("Tu nombre porfavor: "))
apellido = str(input("Tu apellido porfavor: "))
pais = str(input("Tu pais porfavor: "))
ancho_pared = int(input("El ancho de la pared solicitada porfavor: "))
alto_pared = int(input("El alto de la pared solicitada porfavor: "))
precios = int(input("El precio por metro cuadrado porfavor"))
area_total = ancho_pared * alto_pared
costo_estimado = area_total * precios
nombre_completo = nombre+" "+apellido
mayusculas = nombre_completo.upper()
print (f"Reporte final: {mayusculas}, de {pais} ")
print (f"Area total: {area_total}")
print (f"Costos estimado: {costo_estimado}")
print ("la longitud de su nombre es igual a:"len(nombre_completo))
if "a" in nombre_completo.lower():
    print("La letra 'a' está presente.")
if costo_estimado >= 100:
    print ("El costo estimado supera los 100$")
#1. Solicite al usuario: Nombre, apellido, país, ancho de la pared, alto de la pared, precio por
#metro cuadrado o Calcule: área de la pared, costo total estimado
#2. Cree la variable nombre_completo.
#1. Muestre un reporte final que incluya:
#o nombre completo, país, área calculada, costo total (La impresión del reporte final debe
#realizarse usando f-strings.)
#3. Muestre además:
#o nombre_completo en mayúsculas
#o la longitud de nombre_completo
#o si la letra "a" está presente en nombre_completo
#o si el costo total es mayor que 100

# %%
