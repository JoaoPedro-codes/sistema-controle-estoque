from interface import limpar_tela, titulo
from validacoes import leiaInt
from dados import opcoes_status

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


def escolher_filtros(possibilidades, msg, msg_opcao):
    limpar_tela()
    titulo(msg)
    print()
    print('Campos de filtragem:')
    print()
    print(f'[0] Consultar Todos')
    for chave, valor in possibilidades.items():
        print(f'[{chave}] {valor}')
    print(f'[5] Voltar ao menu principal')
    print()
    while True:
        escolha = input(msg_opcao)
        escolha_com_espaco = escolha.replace(',', ' ')
        escolha_separada = escolha_com_espaco.split()
        escolhaInt = []
        escolhas_lista = []
        escolhas = {}
        valido = True

        if not escolha_separada:
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
            valido = False

        if valido:
            for i in range(0, len(escolha_separada)):
                try:
                    filtro = int(escolha_separada[i])
                except (ValueError, TypeError):
                    print('\nERRO: Por favor, digite apenas opções válidas!\n')
                    valido = False
                    break
                else:  
                    escolhaInt.append(filtro)

        if valido:
                for v in escolhaInt:
                    if v not in [0, 1, 2, 3, 4, 5]:
                        print('\nERRO: Por favor, digite apenas opções válidas!\n')
                        valido = False
                        break
                if len(escolhaInt) == 1 and escolhaInt[0] == 5:
                    return 5
                else:
                    if len(escolhaInt) > 1 and 5 in escolhaInt:
                        print('\nERRO: Por favor, digite apenas opções válidas!\n')
                        valido = False
                if len(escolhaInt) == 1 and escolhaInt[0] == 0:
                    return {}
                else:
                    if len(escolhaInt) > 1 and 0 in escolhaInt:
                        print('\nERRO: Por favor, digite apenas opções válidas!\n')
                        valido = False
        
        if valido:
            break

    for num in escolhaInt:
        escolhas_lista.append(possibilidades[num])
       
    for valor in escolhas_lista:
        escolhas[valor] = ''

    limpar_tela()

    for campo in escolhas:
        if campo == 'Status':
            print()
            escolhas[campo] = escolher_status(opcoes_status)
        else:
            print()
            escolhas[campo] = input(f'{campo}: ')

    return escolhas


def escolher_status(lista):
    print('Escolha o Status:')
    print()
    c = 1
    for item in lista:
        print(f'[{c}] {item}')
        c += 1
    print()
    opcao = leiaInt('Status: ')
    while True:
        if opcao < 1 or opcao > len(lista):
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
            opcao = leiaInt('Status: ')
        else:
            return lista[opcao-1]