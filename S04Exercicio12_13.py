n = int(input('Digite:'
              '\n[1] Converter de milhas para quilômetros;'
              '\n[2] Converter de quilôemtros para milhas. \n'))
distância = float(input('Digite a distância: \n'))

if n==1:
    distancia_convertida = 1.61*distancia
    unidade = 'km'
else:
    distancia_convertida = distancia/1.61
    unidade = 'milhas'


print(f'A conversão da distância digitada é: {distancia_convertida:,.2f} {unidade}')
