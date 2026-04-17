#Actividad 4
#17/04/2026
#%%
texto = "Programación Para Todos"

print("Texto:", texto)
print("Cantidad de caracteres:", len(texto))


#%%
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Title:", texto.title())
print("Capitalize:", texto.capitalize())


#%%
print("¿Empieza con 'Programación'?", texto.startswith("Programación"))
print("¿Termina con 'Todos'?", texto.endswith("Todos"))
print("Posición de 'Para':", texto.find("Para"))
print("¿Contiene 'Python'?", "Python" in texto)


#%%
reemplazo = texto.replace("Programación", "Python")
print("Reemplazo:", reemplazo)

palabras = texto.split()
print("Lista de palabras:", palabras)

unido = " - ".join(palabras)
print("Texto unido:", unido)


#%%
print("Primer carácter:", texto[0])
print("Último carácter:", texto[-1])
print("Carácter en posición 5:", texto[5])


# %%
nombre_completo = "Paúl Zurita"
print(f"Hola, mi nombre es {nombre_completo}")

#%%
iniciales = "".join([palabra[0].upper() for palabra in nombre_completo.split()])
print("Acrónimo:", iniciales)

