nome = input('\033[1;37mdigite seu nome:')
print('\033[0;molá {}!'.format(nome))
idade = int(input('\033[1;37m{}, digite sua idade: '.format(nome)))
if idade < 18:
    print("\033[1;31mSAIA DESSE LUGAR, ESSE LUGAR É PERIGOSO PARA VOCÊ!")
else:
    print('\033[0;32m continue por aqui, cidadão')
    print('\033[1;34;41m*atos libidinosos* *drogas* *loucuragem*\033[m')

