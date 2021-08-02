soma = 0

for n in range(1, 4):
    num = float(input(f'Insira o {n}º número: '))
    soma = soma+(num**2)

print(f'A soma dos quadrados dos números digitados é: {soma:,.2f}')
