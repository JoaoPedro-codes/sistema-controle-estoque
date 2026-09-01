def escreveLinha(num=42):
    print('='*num)


def titulo(msg):
    escreveLinha()
    print(f'{msg:^42}')
    escreveLinha()


def leiaInt(opc):
    while True:
        try:
             opcao = int(input((opc))) 
        except (ValueError, TypeError):
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
        else:
            return opcao
        

def menu(lista):
    titulo('SISTEMA DE ESTOQUE')
    print()
    c = 1
    for item in lista:
        print(f'[{c}] {item}')
        c += 1
    print()
    opcao = leiaInt('Sua opção: ')
    while True:
        if opcao < 1 or opcao > len(lista):
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
            opcao = leiaInt('Sua opção: ')
        else:
            return opcao


#programa principal

from time import sleep

opcoes = ['Entrada de estoque', 'Consultar produtos', 'Saída de estoque', 'Sair']

while True:
    opcao = menu(opcoes)
    if opcao == 1:
        titulo(opcoes[0].upper())
    elif opcao == 2:
        titulo(opcoes[1].upper())
    elif opcao == 3:
        titulo(opcoes[2].upper())
    elif opcao == 4:
        print('Finalizando o programa...')
        break
    sleep(1)