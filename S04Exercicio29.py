soma = 0

for n in range(1, 5):
    nota = float(input(f'Insira a {n}º nota: '))
    soma = soma+nota

print(f'A média aritmética das notas digitadas é: {(soma/4):,.2f}')
