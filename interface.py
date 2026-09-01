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
        

def menu(lista, msg):
    titulo(msg)
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


def menu_dicio(dicio, msg, msg_opcao):
    titulo(msg)
    print()
    for chave, valor in dicio.items():
        print(f'[{chave}] {valor}')
    print()
    escolha = input(msg_opcao)
    escolha_com_espaco = escolha.replace(',', ' ')
    escolha_separada = escolha_com_espaco.split()
    return escolha_separada