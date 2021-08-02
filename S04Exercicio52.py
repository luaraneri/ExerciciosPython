um = float(input('Quanto a pessoa 1 apostou? R$ ')))
dois = float(input('Quanto a pessoa 2 apostou? R$ ')))
tres = float(input('Quanto a pessoa 3 apostou? R$ ')))
premio = float(input("Valor do prêmio: R$ ")))

total_aposta = um+dois+tres

premio_um = (um/total_aposta)*premio
premio_dois = (dois/total_aposta)*premio
premio_tres = (tres/total_aposta)*premio

print('\nCom base no valor investido, o prêmio deve ser distribuído:'
      f'\n Jogador 1: {premio_um:,.2f}'
      f'\n Jogador 2: {premio_dois:,.2f}'
      f'\n Jogador 3: {premio_tres:,.2f}')
