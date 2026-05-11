#%%
variableControl = 1
while variableControl < 5:
    print (variableControl)
    variableControl = variableControl + 1
else:
    print (f"el ciclo se repitio: {variableControl}")
#%%
clave = str(input("ingrese la clave: "))
while clave != "python":
    clave = str(input("ingrese la clave: "))
print ("acesso permitido")
#%%
opcion = " "
while opcion != "3":
    print ("=====MENU=====")
    print ("1. Saludar")
    print ("2. Mostrar mensaje")
    print ("3. Salir")
    opcion = str(input("Seleccione una opcion: "))
    if opcion == "1":
        print ("hola")
    elif opcion == "2":
        print ("Estamos aprendiendo ")
    elif opcion == "3":
        print("bye")
    else:
        print ("opcion no valida")
#%%
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count ==3:
        break
print ("se detuvo")
#%%
clave_correcta = "python123"
intentos = 0
while intentos < 3:
    clave_intento = str(input ("Coloque la calve: "))
    if clave_intento != clave_correcta:
        print("intento fallido")
        intentos = intentos + 1
    else:
        print("acceso correcto")
        break
if intentos == 3:
    print ("bloqueado")
#%%
n = 0
while n <5:
    n=n+1
    if n ==4:
        continue
    print (n)
# %%
act1 = 0
while act1 <11:
    print (act1)
    act1 = act1 + 1
# %%
act2 = " "
while act2 != "python123":
    act2 = str(input("ingrese la clave: "))
print ("acesso permitido")
# %%
opcion = " "
while opcion != "3":
    print ("=====MENU=====")
    print ("1. Saludar")
    print ("2. Mostrar mensaje")
    print ("3. Salir")
    opcion = str(input("Seleccione una opcion: "))
    if opcion == "1":
        print ("Buenos dias/tardes/noches")
    elif opcion == "2":
        print ("Estamos aprendiendo y mejorando cada dia ")
    elif opcion == "3":
        print("bye")
    else:
        print ("opcion no valida")