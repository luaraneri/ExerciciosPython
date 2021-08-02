import math

x = float(input('Insira o valor de x: '))
y = float(input('Insira o valor de y: '))

if x<0:
    x=-x

if y<0:
    y=-y

distancia = math.sqrt((x**2)+(y**2))

print(f'A distancia da coordenada dada até a origem (0,0) é: {distancia:,.1f}')
