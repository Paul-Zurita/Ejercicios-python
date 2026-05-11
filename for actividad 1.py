palabra = str(input("pon una palabra: "))
vocales = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o " or letra == "u":
        vocales = vocales + 1
print (f"El numero de vocales que hay es de {vocales}")