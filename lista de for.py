notas = [10,8,9,7,6,5,4,3,2,1]
cuantas = int(input("Di el numero de notas que salgan: "))
if cuantas> 0 and cuantas < 11:
    for nota in range(cuantas):
        print(f"Nota registrada{notas[cuantas]}")