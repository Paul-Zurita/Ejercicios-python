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
print (variable + texto.upper())
#3. Muestre la cantidad de caracteres de la frase.
print (len(variable))
#4. Verifique si la palabra "Python" está dentro de la frase.

#5. Reemplace "Tecnología" por "Programación".
#6. Divida la frase en palabras usando split(). 

# ===== PARTE C =====
# Programa integrador
# ...