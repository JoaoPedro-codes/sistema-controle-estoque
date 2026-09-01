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


def filtrar_produtos(estoque, filtros):
    resultado = []

    if len(filtros) > 0:
        for codigo, produto in estoque.items():
            cont = 0
            if produto['Status'] == 'INATIVO':
                if 'Status' not in filtros or filtros['Status'] != 'INATIVO':
                    continue
            for c, v in filtros.items(): 
                if v == produto[c]:
                    cont += 1
            if cont == len(filtros):
                resultado.append(codigo)

    else:
        for codigo, produto in estoque.items():
            if produto['Status'] == 'INATIVO':
                continue
            resultado.append(codigo)

    return resultado

#programa principal

from time import sleep

estoque = {
    1: {
        'Tipo': 'Arroz',
        'Marca': 'Camil',
        'Categoria': 'Alimentos',
        'Quantidade': 20,
        'Preço': 25.90,
        'Status': 'DISPONÍVEL'
    },

    2: {
        'Tipo': 'Arroz',
        'Marca': 'Tio João',
        'Categoria': 'Alimentos',
        'Quantidade': 12,
        'Preço': 27.50,
        'Status': 'DISPONÍVEL'
    },

    3: {
        'Tipo': 'Feijão',
        'Marca': 'Camil',
        'Categoria': 'Alimentos',
        'Quantidade': 0,
        'Preço': 8.90,
        'Status': 'ESGOTADO'
    },

    4: {
        'Tipo': 'Detergente',
        'Marca': 'Ypê',
        'Categoria': 'Limpeza',
        'Quantidade': 15,
        'Preço': 3.49,
        'Status': 'DISPONÍVEL'
    },

    5: {
        'Tipo': 'Arroz',
        'Marca': 'Prato Fino',
        'Categoria': 'Alimentos',
        'Quantidade': 0,
        'Preço': 23.90,
        'Status': 'INATIVO'
    }
}

filtros = {}

opcoes = ['Entrada de estoque', 'Consultar produtos', 'Saída de estoque', 'Sair']

while True:
    opcao = menu(opcoes)
    if opcao == 1:
        titulo(opcoes[0].upper())
    elif opcao == 2:
        titulo(opcoes[1].upper())
        print(filtrar_produtos(estoque, filtros))
    elif opcao == 3:
        titulo(opcoes[2].upper())
    elif opcao == 4:
        print('Finalizando o programa...')
        break
    sleep(1)
