suma = 0
num_nota = 1
promedio = int(input("di el numero de notas: "))
if promedio < 0 and promedio> 2:
    for num in range (promedio):
        nota = float(input(f"nota numero {num_nota+1}, coloque su nota: "))
        suma += nota
promedio_total = suma/promedio
print(f"tu promedio de notas es {promedio_total}")