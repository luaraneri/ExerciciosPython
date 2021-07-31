from num2words import num2words

total = 0

for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')
    num = num.replace(' ', '')
    total += len(num)

print(f'Entre 1 e 1000 temos {total} letras.')
