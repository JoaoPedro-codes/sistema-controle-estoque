from time import sleep
from interface import limpar_tela, titulo
from consultas import escolher_status
from dados import opcoes_status
from validacoes import leiaTexto, leiaFloat

def inativar_produto(dicio, codigo):
    if dicio[codigo]['Quantidade'] > 0:
        print('Não é possível inativar esse produto.')
        print(f'Ainda existem {dicio[codigo]['Quantidade']} unidades em estoque.')
        print('\nRealize a saída  do estoque antes de inativá-lo.')
        input('\nPressione ENTER para continuar...')
        return 0
    elif dicio[codigo]['Quantidade'] == 0:
        while True:
            inativar = input('Deseja realmente inativar esse produto? [S/N]:\nR: ').strip().upper()
            if inativar not in ('S', 'N'):
                print('\nERRO: Digite apenas S ou N!\n')
                continue
            if inativar == 'S':
                dicio[codigo]['Status'] = 'INATIVO'
                print('\nProduto inativado com sucesso!')
                input('\nPressione ENTER para continuar...')
                return 1
            else:
                print('\nOperação cancelada.')
                sleep(2)
                return 2


def alterar_cadastro(possibilidades, msg, msg_opcao, estoque, codigo):
    limpar_tela()
    titulo(msg)
    print()
    print('Campos sujeitos à alteração:')
    print()
    print(f'[0] Alterar Todos')
    for chave, valor in possibilidades.items():
        print(f'[{chave}] {valor}')
    print(f'[5] Voltar')
    print()
    while True:
        escolha = input(msg_opcao)
        escolha_com_espaco = escolha.replace(',', ' ')
        escolha_separada = escolha_com_espaco.split()
        escolhaInt = []
        escolhas_lista = []
        validacao_mudanca = []
        mudancas = {}
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
                    escolhaInt = [1, 2, 3, 4]
                else:
                    if len(escolhaInt) > 1 and 0 in escolhaInt:
                        print('\nERRO: Por favor, digite apenas opções válidas!\n')
                        valido = False
        
        if valido:
            break

    for num in escolhaInt:
        escolhas_lista.append(possibilidades[num])
        
    for valor in escolhas_lista:
        mudancas[valor] = ''

    limpar_tela()

    for campo in mudancas:
        print()
        if campo == 'Preço':
            mudancas[campo] = leiaFloat(f'{campo}: ')
        else:
            mudancas[campo] = leiaTexto(f'{campo}: ')

    tipo_final = estoque[codigo]['Tipo']
    marca_final = estoque[codigo]['Marca']

    for campo, informacao in mudancas.items():
        if campo == 'Tipo':
            tipo_final = informacao
        elif campo == 'Marca':
            marca_final = informacao

    for cod, produto in estoque.items():
        if cod == codigo:
            continue
        elif tipo_final == produto['Tipo'] and marca_final == produto['Marca']:
            print()
            print('A tentativa de alteração falhou.')
            print('Já existe um produto com essas características no banco de dados!')
            sleep(3)
            return 5

    for campo, informacao in mudancas.items():
        estoque[codigo][campo] = informacao

    return 0