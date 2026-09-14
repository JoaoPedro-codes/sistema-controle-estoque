from time import sleep
from interface import limpar_tela, titulo, formatarMoeda, exibir_produto
from validacoes import leiaTexto, leiaFloat, leiaIntOpcional, leiaInt, leiaSimNao

def inativar_produto(estoque, codigo):
    if estoque[codigo]['Quantidade'] > 0:
        print(f'Não é possível inativar esse produto. Ainda existem {estoque[codigo]['Quantidade']} unidades em estoque!')
        return 0
    elif estoque[codigo]['Quantidade'] == 0:
        inativar = leiaSimNao('Deseja realmente inativar esse produto? [S/N]:\nR: ')
        if inativar == 'S':
            estoque[codigo]['Status'] = 'INATIVO'
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
        escolha_separada = escolha.replace(',', ' ').split()
        escolhaInt = []
        valido = True

        if not escolha_separada:
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
            valido = False

        if valido:
            for escolha in escolha_separada:
                try:
                    filtro = int(escolha)
                except (ValueError, TypeError):
                    print('\nERRO: Por favor, digite apenas opções válidas!\n')
                    valido = False
                    break
                else:
                    escolhaInt.append(filtro)

        if valido:
            for v in escolhaInt:
                if v not in (0, 1, 2, 3, 4, 5):
                    print('\nERRO: Por favor, digite apenas opções válidas!\n')
                    valido = False
                    break
            if len(escolhaInt) == 1 and escolhaInt[0] == 5:
                return 5
            
            if len(escolhaInt) > 1 and 5 in escolhaInt:
                print('\nERRO: Por favor, digite apenas opções válidas!\n')
                valido = False
                
            if len(escolhaInt) == 1 and escolhaInt[0] == 0:
                escolhaInt = [1, 2, 3, 4]
            
            if len(escolhaInt) > 1 and 0 in escolhaInt:
                print('\nERRO: Por favor, digite apenas opções válidas!\n')
                valido = False

        if valido:
            break

    mudancas = {}

    for num in escolhaInt:
        mudancas[possibilidades[num]] = ''
        
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
        if tipo_final.upper() == produto['Tipo'].upper() and marca_final.upper() == produto['Marca'].upper():
            print()
            print('A tentativa de alteração falhou. Já existe um produto com essas características no banco de dados!')
            sleep(4)
            return 5

    for campo, informacao in mudancas.items():
        estoque[codigo][campo] = informacao

    return 0


def entrada_estoque(estoque):
    limpar_tela()
    titulo('ENTRADA DE ESTOQUE')
    print()

    while True:
        codigo = leiaIntOpcional('Digite o código do produto [ENTER = NOVO CADASTRO | valor negativo = VOLTAR]: ')
        if codigo < 0:
            return -1

        if codigo == 0:
            cadastro = cadastrar_produto(estoque)
            return cadastro
        else:
            if codigo in estoque:
                if estoque[codigo]['Status'] == 'INATIVO':
                    print()
                    reativar = leiaSimNao('PRODUTO INATIVO! Deseja reativar esse produto? [S/N]:\nR: ')
                    if reativar == 'S':
                        exibir_produto(estoque, codigo)
                        entrada = operacao_entrada(estoque, codigo)
                        if entrada == -1:
                            limpar_tela()
                            titulo('ENTRADA DE ESTOQUE')
                            print()
                            continue
                        return entrada
                    else:
                        print('\nOperação cancelada.')
                        sleep(2)
                        continue
                else:
                    exibir_produto(estoque, codigo)
                    entrada = operacao_entrada(estoque, codigo)
                    if entrada == -1:
                        limpar_tela()
                        titulo('ENTRADA DE ESTOQUE')
                        print()
                        continue
                    return entrada
            else:
                print('\nERRO: Digite um identificador válido!\n')
                continue


def operacao_entrada(estoque, codigo, entrada=None, novo_preco=None):
    while True:
        if entrada is None:
            entrada = leiaInt('Quantidade de entrada [valor negativo = CANCELAR]: ', '\nERRO: Digite um valor numérico válido!\n')
        if entrada < 0:
            return -1
        if entrada == 0:
            print('\nERRO: O valor deve ser maior que zero!\n')
            entrada = None
            continue
        break
    print()

    print(f"Preço atual: {formatarMoeda(estoque[codigo]['Preço'])}")
    atualizar_preco = False
    print()

    mudar_preco = leiaSimNao('Deseja atualizar o preço? [S/N]:\nR: ')
    if mudar_preco == 'S':
        if novo_preco is None:
            novo_preco = leiaFloat('Digite o novo preço: R$')
        atualizar_preco = True

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
    
    if len(estoque) == 0:
        codigo = 1
    else:
        codigo = max(estoque.keys()) + 1

    novo_produto = {
    'Tipo': '',
    'Marca': '',
    'Categoria': '',
    'Quantidade': '',
    'Preço': '',
    'Status': ''
 }

    for campo in novo_produto:
        if campo == 'Quantidade':
            while True:
                novo_produto[campo] = leiaInt(f'{campo}: ')
                if novo_produto[campo] < 0:
                    print('\nERRO: O valor não pode ser negativo!\n')
                    continue
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
        if tipo_final.upper() == produto['Tipo'].upper() and marca_final.upper() == produto['Marca'].upper():
            print()
            print(f'Produto já cadastrado! Código: {cod}')
            cadastrado = True
            cod_existente = cod
            break

    if cadastrado:
        if estoque[cod_existente]['Status'] != 'INATIVO':
            print()
            realizar_entrada = leiaSimNao('Deseja realizar uma entrada de estoque? [S/N]:\nR: ')
            if realizar_entrada == 'S':
                exibir_produto(estoque, cod_existente)
                entrada = operacao_entrada(estoque, cod_existente, novo_produto['Quantidade'], novo_produto['Preço'])
                return entrada
            else:
                print('\nOperação encerrada.')
                sleep(2)
                return -1

        else:
            print()
            reativar = leiaSimNao('PRODUTO INATIVO! Deseja reativar esse produto? [S/N]:\nR: ')
            if reativar == 'S':
                exibir_produto(estoque, cod_existente)
                entrada = operacao_entrada(estoque, cod_existente, novo_produto['Quantidade'], novo_produto['Preço'])
                return entrada
            else:
                print('\nOperação cancelada.')
                sleep(2)
                return -1

    estoque[codigo] = novo_produto
    exibir_produto(estoque, codigo, 'CADASTRO REALIZADO COM SUCESSO!')
    input('Pressione ENTER para continuar...')
    return 0


def saida_estoque(estoque):
    while True:
        limpar_tela()
        titulo('SAÍDA DE ESTOQUE')
        print()

        while True:
            codigo = leiaInt('Digite o código do produto [valor negativo = VOLTAR]: ')
            if codigo < 0:
                return -1

            if codigo in estoque:
                if estoque[codigo]['Status'] == 'INATIVO':
                    exibir_produto(estoque, codigo)
                    print('PRODUTO INATIVO! Não é possível realizar saída desse produto.')
                    input('\nPressione ENTER para continuar...')
                    break
                elif estoque[codigo]['Status'] == 'ESGOTADO':
                    exibir_produto(estoque, codigo)
                    print('PRODUTO ESGOTADO! Mercadoria sem estoque.')
                    input('\nPressione ENTER para continuar...')
                    break
                else:
                    exibir_produto(estoque, codigo)
                    saida = operacao_saida(estoque, codigo)
                    if saida == -1:
                        break
                    return saida
            else:
                print('\nERRO: Digite um identificador válido!\n')
                continue


def operacao_saida(estoque, codigo):
    while True:
        saida = leiaInt('\nQuantidade de saída [valor negativo = CANCELAR]: ', '\nERRO: Digite um valor numérico válido!\n')
        if saida < 0:
            return -1
        if saida == 0:
            print('\nERRO: O valor deve ser maior que zero!\n')
            continue
        if saida > estoque[codigo]['Quantidade']:
            print('\nERRO: A quantidade solicitada é maior que a disponível em estoque!')
            print()
            realizar_saida = leiaSimNao('Deseja retirar toda a quantidade disponível? [S/N]:\nR: ')
            if realizar_saida == 'S':
                saida = estoque[codigo]['Quantidade']
                break
            else:
                print('\nInforme uma nova quantidade de saída.')
                continue
        else:
            break

    estoque[codigo]['Quantidade'] -= saida
    if estoque[codigo]['Quantidade'] == 0:
        estoque[codigo]['Status'] = 'ESGOTADO'

    limpar_tela()
    titulo('SAÍDA REALIZADA COM SUCESSO!')
    print()
    print(f'{"Saída realizada:":<20} -{saida}')
    print(f'{"Quantidade atual:":<20} {estoque[codigo]['Quantidade']}')
    print(f'{"Status:":<20} {estoque[codigo]['Status']}')
    
    input('\nPressione ENTER para continuar...')

    return 0


def zerar_para_inativar(estoque, codigo):
    realizar_saida = leiaSimNao('\nDeseja realizar a saída de toda quantidade disponível? [S/N]:\nR: ')
    if realizar_saida == 'S':
        saida = estoque[codigo]['Quantidade']
    else:
        print('\nOperação cancelada.')
        sleep(2)
        return -1

    estoque[codigo]['Quantidade'] -= saida
    estoque[codigo]['Status'] = 'ESGOTADO'

    limpar_tela()
    titulo('SAÍDA REALIZADA COM SUCESSO!')
    print()
    print(f'{"Saída realizada:":<20} -{saida}')
    print(f'{"Quantidade atual:":<20} {estoque[codigo]['Quantidade']}')
    print(f'{"Status:":<20} {estoque[codigo]['Status']}')
    print()

    return 0