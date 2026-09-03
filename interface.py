import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def escreveLinha(num=42):
    print('='*num)


def titulo(msg):
    escreveLinha()
    print(f'{msg:^42}')
    escreveLinha()


def leiaInt(opc):
    while True:
        try:
             opcao = int(input(opc)) 
        except (ValueError, TypeError):
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
        else:
            return opcao
        

def menu(lista, msg):
    limpar_tela()
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


def detalhes_produto(dicio, codigo):
    limpar_tela()
    titulo('DETALHES DO PRODUTO')
    print()
    print(f'{"Código:":<18}{codigo}')
    produto = dicio[codigo]
    for chave, valor in produto.items():
        print(f'{(chave + ":"):<18}{valor}')
    print()

    opcoes_tela = [
        'Alterar cadastro',
        'Inativar produto',
        'Voltar',
        'Menu principal'
    ]

    c = 1
    for item in opcoes_tela:
        print(f'[{c}] {item}')
        c += 1
    print()
    opcao = leiaInt('Sua opção: ')
    while True:
        if opcao < 1 or opcao > len(opcoes_tela):
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
            opcao = leiaInt('Sua opção: ')
        else:
            return opcao


def mostrar_resultados(dicio, lista):
    limpar_tela()
    titulo('PRODUTOS ENCONTRADOS')
    print()
    c = 1
    for codigo in lista:
        print(f'[{c}] Código {codigo} => ', end=' ')
        print(f'Tipo: {dicio[codigo]["Tipo"]}', end=' | ') 
        print(f'Marca: {dicio[codigo]["Marca"]}') 
        c += 1  
        print()

    opcao = leiaInt('Digite a númeração do produto para exibir detalhes [valor negativo = CANCELAR]: ')
    while True:
        if opcao < 0:
            return 0
        elif opcao > len(lista) or opcao == 0:
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
            opcao = leiaInt('Digite a númeração do produto para exibir detalhes [valor negativo = CANCELAR]: ')
        else:
            return lista[opcao-1]