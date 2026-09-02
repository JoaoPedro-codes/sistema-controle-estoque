from time import sleep

def inativar_produto(dicio, codigo):
    if dicio[codigo]['Quantidade'] > 0:
        print('Não é possível inativar esse produto.')
        print(f'Ainda existem {dicio[codigo]['Quantidade']} unidades em estoque.')
        print('\nRealize a saída  do estoque antes de inativá-lo.')
        input('\n\nPressione ENTER para continuar...')
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
                input('\n\nPressione ENTER para continuar...')
                return 1
            else:
                print('\nOperação cancelada.')
                sleep(1)
                return 2