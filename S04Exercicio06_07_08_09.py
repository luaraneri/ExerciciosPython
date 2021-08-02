n = int(input('Digite:'
              '\n[1] Converter de graus Celcius para Fahrenheit;'
              '\n[2] Converter de graus Fahrenheit para Celsius;'
              '\n[3] Converter de graus Celsius para Kelvin; ou'
              '\n[4] Converter de graus Kelvin para Celsius. \n'))
temperatura = float(input('Digite a temperatura: \n'))

if n==1:
    temp_convertida = (temperatura*(9/5))+32
    unidade = 'ºF'
elif n==2:
    temp_convertida = (temperatura-32)*(5/9)
    unidade = 'ºC'
elif n==3:
    temp_convertida = temperatura+273.15
    unidade = 'ºK'
else:
    temp_convertida = temperatura-273.15
    unidade = 'ºC'


print(f'A conversão da temperatura digitada é: {temp_convertida:,.2f}{unidade}')
