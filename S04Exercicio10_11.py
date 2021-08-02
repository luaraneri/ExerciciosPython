n = int(input('Digite:'
              '\n[1] Converter de hm/h para m/s;'
              '\n[2] Converter de m/s para km/h. \n'))
velocidade = float(input('Digite a velocidade: \n'))

if n==1:
    velocidade_convertida = velocidade/3.6
    unidade = 'm/s'
else:
    valocidade_convertida = velocidade*3.6
    unidade = 'km/h'


print(f'A conversão da velocidade digitada é: {velocidade_convertida:,.2f} {unidade}')
