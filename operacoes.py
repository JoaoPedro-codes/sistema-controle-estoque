from time import sleep
from interface import limpar_tela, titulo, formatarMoeda, exibir_produto
from validacoes import leiaTexto, leiaFloat, leiaIntOpcional, leiaInt

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


def entrada_estoque(estoque):
    limpar_tela()
    titulo('ENTRADA DE ESTOQUE')
    print()

    entrada = -1

    while True:
        codigo = leiaIntOpcional('Digite o código do produto [ENTER = NOVO CADASTRO | valor negativo = VOLTAR]: ')
        if codigo < 0:
            return -1

        if codigo == 0:
            cadastro = cadastrar_produto(estoque)
            return cadastro
        else:
            if codigo in estoque.keys():
                if estoque[codigo]['Status'] == 'INATIVO':
                    while True:
                        print()
                        reativar = input('PRODUTO INATIVO! Deseja reativar esse produto? [S/N]:\nR: ').strip().upper()
                        if reativar not in ('S', 'N'):
                            print('\nERRO: Digite apenas S ou N!\n')
                            continue
                        if reativar == 'S':
                            exibir_produto(estoque, codigo)
                            entrada = operacao_entrada(estoque, codigo)
                            return entrada
                        else:
                            print('\nOperação cancelada.')
                            sleep(2)
                            return entrada
                else:
                    exibir_produto(estoque, codigo)
                    entrada = operacao_entrada(estoque, codigo)
                    return entrada
            else:
                print('\nERRO: Digite um identificador válido!\n')
                continue


def operacao_entrada(estoque, codigo, entrada=None, novo_preco=None):
    if entrada is None:
        entrada = leiaInt('Quantidade de entrada: ', '\nERRO: Digite um valor numérico válido!\n')
    while entrada <= 0:
        print('\nERRO: O valor deve ser maior que zero!\n')
        entrada = leiaInt('Quantidade de entrada: ', '\nERRO: Digite um valor numérico válido!\n')
    print()

    print(f"Preço atual: {formatarMoeda(estoque[codigo]['Preço'])}")
    atualizar_preco = False

    while True:
        print()
        mudar_preco = input('Deseja atualizar o preço? [S/N]:\nR: ').strip().upper()
        if mudar_preco not in ('S', 'N'):
            print('\nERRO: Digite apenas S ou N!\n')
            continue
        if mudar_preco == 'S':
            if novo_preco is None:
                novo_preco = leiaFloat('Digite o novo preço: R$')
            atualizar_preco = True
            break
        elif mudar_preco == 'N':
            break

    reativacao = estoque[codigo]['Status'] == "INATIVO"
        
    estoque[codigo]['Quantidade'] += entrada
    estoque[codigo]['Status'] = 'DISPONÍVEL'
    if atualizar_preco:
        estoque[codigo]['Preço'] = novo_preco

    limpar_tela()
    titulo('ENTRADA REALIZADA COM SUCESSO!')
    print()
    print(f'{"Entrada realizada:":<20} +{entrada}')
    print(f'{"Quantidade atual:":<20} {estoque[codigo]['Quantidade']}')
    print(f'{"Preço atual:":<20} {formatarMoeda(estoque[codigo]['Preço'])}')
    print(f'{"Status:":<20} {estoque[codigo]['Status']}')
    print()
    if reativacao:
        print('Produto reativado com sucesso!')
    input('\nPressione ENTER para continuar...')

    return 0

    
def cadastrar_produto(estoque):
    limpar_tela()
    titulo('CADASTRO DE PRODUTO')
    print()

    entrada = -1
    codigo = len(estoque) + 1

    novo_produto = {
    'Tipo': '',
    'Marca': '',
    'Categoria': '',
    'Quantidade': '',
    'Preço': '',
    'Status': ''
 }

    for campo in novo_produto.keys():
        if campo == 'Quantidade':
            while True:
                novo_produto[campo] = leiaInt(f'{campo}: ')
                if novo_produto[campo] < 0:
                    print('\nERRO: O valor não pode ser negativo!\n')
                    continue
                else:
                    break
        elif campo == 'Preço':
            novo_produto[campo] = leiaFloat(f'{campo}: ')
        elif campo == 'Status':
            if novo_produto['Quantidade'] == 0:
                novo_produto[campo] = 'ESGOTADO'
            else:
                novo_produto[campo] = 'DISPONÍVEL'
        else:
            novo_produto[campo] = leiaTexto(f'{campo}: ')

    tipo_final = novo_produto['Tipo']
    marca_final = novo_produto['Marca']
    cadastrado = False
    cod_existente = 0
    
    for cod, produto in estoque.items():
        if tipo_final == produto['Tipo'] and marca_final == produto['Marca']:
            print()
            print(f'Produto já cadastrado! Código: {cod}')
            cadastrado = True
            cod_existente = cod
            break

    if cadastrado:
        if estoque[cod_existente]['Status'] != 'INATIVO':
            while True:
                print()
                realizar_entrada = input('Deseja realizar uma entrada de estoque? [S/N]:\nR: ').strip().upper()
                if realizar_entrada not in ('S', 'N'):
                    print('\nERRO: Digite apenas S ou N!\n')
                    continue
                if realizar_entrada == 'S':
                    exibir_produto(estoque, cod_existente)
                    entrada = operacao_entrada(estoque, cod_existente, novo_produto['Quantidade'], novo_produto['Preço'])
                    return entrada
                else:
                    print('\nOperação encerrada.')
                    sleep(2)
                    return entrada

        else:
            while True:
                print()
                reativar = input('PRODUTO INATIVO! Deseja reativar esse produto? [S/N]:\nR: ').strip().upper()
                if reativar not in ('S', 'N'):
                    print('\nERRO: Digite apenas S ou N!\n')
                    continue
                if reativar == 'S':
                    exibir_produto(estoque, cod_existente)
                    entrada = operacao_entrada(estoque, cod_existente, novo_produto['Quantidade'], novo_produto['Preço'])
                    return entrada
                else:
                    print('\nOperação cancelada.')
                    sleep(2)
                    return entrada

    if not cadastrado:
        estoque[codigo] = novo_produto
        print(f'\nProduto cadastrado com sucesso! Código: {codigo}')
        return 0
    

