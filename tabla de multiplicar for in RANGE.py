num = int(input("di un numero que quieres multiplicar: "))
ini = int(input("des que numero quieres multiplicar: "))
i = int(input("hasta que numero quieres multiplicar: "))
if ini < i:
    for i in range (ini+1,i,2):
        print (f"{i} x {num} = {i*num}")
else:
    print ("multiplicacion no valida")