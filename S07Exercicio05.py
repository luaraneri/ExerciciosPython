numeros = []
soma = 0

for n in range(10):
    numeros.append(int(input()))

for item in numeros:
    if item%2==0:
        soma = soma + 1

print(soma)
