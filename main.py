from time import sleep
from interface import menu, titulo, detalhes_produto, mostrar_resultados
from consultas import escolher_filtros, filtrar_produtos
from dados import estoque, opcoes_filtro

filtros = {}

opcoes = [
    'Entrada de estoque',
    'Consultar produtos',
    'Saída de estoque',
    'Sair'
]

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
                filtros = escolher_filtros(opcoes_filtro)
                codigos = filtrar_produtos(estoque, filtros)
                print()
                if len(codigos) == 0:
                    print('Nenhum produto encontrado')
                elif len(codigos) == 1:
                    escolha = detalhes_produto(estoque, codigos[0])
                    if escolha == 3:
                        continue
                    elif escolha == 4:
                        break
                else:
                    while True:
                        retorno = mostrar_resultados(estoque, codigos)
                        if retorno == 0:
                            break
                        else:
                            escolha = detalhes_produto(estoque, retorno)
                            if escolha == 3:
                                continue
                            elif escolha == 4:
                                break
                            
    elif opcao == 3:
        titulo(opcoes[2].upper())
    elif opcao == 4:
        print('Finalizando o programa...')
        break
    sleep(1)
    