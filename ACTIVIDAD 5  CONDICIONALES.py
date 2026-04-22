a = int(input("dame un numero: "))
if a > 0:
    print ("a es positivo")
    if a % 2 == 0:
        print("Par positivo")
    elif a % 2 != 0:
        print ("par negativo")
elif a < 0:
    print ("a es negativo")
else:
    print('a es cero')

