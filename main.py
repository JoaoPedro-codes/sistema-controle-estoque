from time import sleep
from interface import menu, titulo, detalhes_produto, mostrar_resultados
from consultas import escolher_filtros, filtrar_produtos
from dados import carregar_estoque, salvar_estoque, opcoes_filtro, opcoes_alteracao
from operacoes import inativar_produto, alterar_cadastro

filtros = {}

opcoes = [
    'Entrada de estoque',
    'Consultar produtos',
    'Saída de estoque',
    'Sair'
]
estoque = carregar_estoque()

while True:
    opcao = menu(opcoes, 'SISTEMA DE ESTOQUE')
    escolha = 0
    if opcao == 1:
        titulo(opcoes[0].upper())
    elif opcao == 2:
        while True:
            if escolha == 4:
                break
            else:
                filtros = escolher_filtros(opcoes_filtro, opcoes[1].upper(), 'Digite as numerações correnspondentes aos filtros desejados separando-as por vírgula:\nR: ')
                if filtros == 5:
                    break
                else:
                    codigos = filtrar_produtos(estoque, filtros)
                    if len(codigos) == 0:
                        print()
                        print('Nenhum produto encontrado')
                        sleep(2)
                    elif len(codigos) == 1:
                        while True:
                            escolha = detalhes_produto(estoque, codigos[0])
                            print()
                            if escolha == 1:
                                opcoes_alterar = alterar_cadastro(opcoes_alteracao, 'ALTERAR CADASTRO', 'Digite as numerações correnspondentes aos campos desejados separando-as por vírgula:\nR: ', estoque, codigos[0])
                                if opcoes_alterar == 5:
                                    continue
                                if opcoes_alterar == 0:
                                    salvar_estoque(estoque)
                            if escolha == 2:
                                inativo = inativar_produto(estoque, codigos[0])
                                if inativo == 0:
                                    print('Ir para saída de estoque')
                                elif inativo == 1:
                                    salvar_estoque(estoque)
                                    continue
                                elif inativo == 2:
                                    continue
                            elif escolha == 3:
                                break
                            elif escolha == 4:
                                break
                    else:
                        while True:
                            if escolha == 4:
                                break
                            retorno = mostrar_resultados(estoque, codigos)
                            if retorno == 0:
                                break
                            else:
                                while True:
                                    escolha = detalhes_produto(estoque, retorno)
                                    print()
                                    if escolha == 1:
                                        opcoes_alterar = alterar_cadastro(opcoes_alteracao, 'ALTERAR CADASTRO', 'Digite as numerações correnspondentes aos campos desejados separando-as por vírgula:\nR: ', estoque, retorno)
                                        if opcoes_alterar == 5:
                                            continue
                                        if opcoes_alterar == 0:
                                            salvar_estoque(estoque)
                                    elif escolha == 2:
                                        inativo = inativar_produto(estoque, retorno)
                                        if inativo == 0:
                                            print('Ir para saída de estoque')
                                        elif inativo == 1:
                                            salvar_estoque(estoque)
                                            continue
                                        elif inativo == 2:
                                            continue
                                    elif escolha == 3:
                                        break
                                    elif escolha == 4:
                                        break
                            
    elif opcao == 3:
        titulo(opcoes[2].upper())
    elif opcao == 4:
        print('Finalizando o programa...')
        break
    