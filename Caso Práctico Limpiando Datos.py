cedula = input("coloca tu cedula :) ")

cedula_limpia = ""

for caracter in cedula:
    if caracter == '-' or caracter == " ":
        continue
    
    cedula_limpia = cedula_limpia + caracter

print(cedula_limpia)
print(cedula)