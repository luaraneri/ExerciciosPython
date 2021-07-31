numeros = []

for n in range(6):
    aux = (int)(input())
    if aux % 2 == 0:
        numeros.append(aux)
    else:
        print("Este número não é par, digite novamente:")
        n = n - 1

print(numeros[::-1])
