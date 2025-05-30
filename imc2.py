print('------------------------------------------')
print('imc do paciente')
print('------------------------------------------')
nome=input('nome do paciente: ')
altura=float(input('qual esua altura: '))
peso=float(input('quantos quilos voce tem: '))
IMC = peso / (altura ** 2)
total=round(IMC,2)
print('------------------------------------------')
if total >=40:
    print(f'{nome} voce esta com {total} de imc isso quer dizer que voce esta com obsidade do nivel 3')
    print('aviso: proucure um medico')
elif total>=35:
    print(f'{nome} voce esta com {total} de imc isso quer dizer que voce esta com obsidade do nivel 2')
    print('aviso: faca exames pra ver se sua saude esta em dia')
elif total >=30:
    print(f'{nome} voce esta com {total} de imc isso quer dizer que voce esta com obsidade do nivel 1')
    print('aviso: faca um dieda e treine')
elif total>=25:
    print(f'{nome} voce esta com {total} de imc isso quer dizer que voce esta com sobrepeso')
    print('aviso: faca um caminhada todo dia')
elif total>=18.5:
    print(f'{nome} voce esta com {total} de imc isso quer dizer que voce esta com peso normal')
    print('aviso: se mandenha em forma')
else:
    print(f'{nome} voce esta com {total} de imc isso quer dizer que voce esta com abaixo do peso ')
    print('aviso: pode comer de boa')
print('------------------------------------------')