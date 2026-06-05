a = int(input("dame un numero: "))
if a > 0 and a % 2 == 0:
    print ("a es positivo y par")
elif a > 0:
        print ("impar positivo")
if a < 0 and a % 2 == 0:
    print ("a es negativo y par")
elif a < 0:
        print ("impar negativo")
else:
    print('a es cero')

b = 0
if b > 0:
    if b % 2 == 0:
        print('b es positivo par')
    else:
        print('b es positivo')
elif b == 0:
    print('b es cero')
else:
    print('b es negativo')
#%%
c = int(input("dame otro numero: "))
if c == 0:
    print ("es cero")
else:
    if c > 0:
        if c % 2 == 0:
            print("es positivo par")
        else : 
            print ("positivo impar")
            if c < 0:
                if c % 2 == 0:
                    print ("negativo par")
                else: 
                    print ("negativo impar")
#%%
edad = int(input("edad? "))
print ("Mayor de edad") if edad >=18 else print ("menor de edad :(")
# %%
