from time import sleep
from interface import menu, detalhes_produto, mostrar_resultados
from consultas import escolher_filtros, filtrar_produtos
from dados import carregar_estoque, salvar_estoque, opcoes_filtro, opcoes_alteracao
from operacoes import inativar_produto, alterar_cadastro, entrada_estoque, saida_estoque, zerar_para_inativar

def menu_produto(estoque, codigo):
    while True:
        escolha = detalhes_produto(estoque, codigo)
        print()
        if escolha == 1:
            opcoes_alterar = alterar_cadastro(opcoes_alteracao, 'ALTERAR CADASTRO', 'Digite as numerações correnspondentes aos campos desejados separando-as por vírgula:\nR: ', estoque, codigo)
            if opcoes_alterar == 5:
                continue
            if opcoes_alterar == 0:
                salvar_estoque(estoque)
        elif escolha == 2:
            while True:
                inativo = inativar_produto(estoque, codigo)
                if inativo == 0:
                    zerar = zerar_para_inativar(estoque, codigo)
                    if zerar == 0:
                        continue
                    elif zerar == -1:
                        break
                elif inativo == 1:
                    salvar_estoque(estoque)
                    break
                elif inativo == 2:
                    break
        elif escolha == 3:
            return 3
        elif escolha == 4:
            return 4


filtros = {}

opcoes = [
    'Entrada de estoque',
    'Consultar produtos',
    'Saída de estoque',
    'Sair'
]
estoque = carregar_estoque()
if estoque is None:
    print('Não foi possível carregar o estoque. Encerrando o programa...\n')
    exit()

while True:
    opcao = menu(opcoes, 'SISTEMA DE ESTOQUE')
    if opcao == 1:
        modificacao = entrada_estoque(estoque)
        if modificacao == 0:
            salvar_estoque(estoque)
        elif modificacao == -1:
            continue
    elif opcao == 2:
        while True:
            filtros = escolher_filtros(opcoes_filtro, opcoes[1].upper(), 'Digite as numerações correnspondentes aos filtros desejados separando-as por vírgula:\nR: ')
            if filtros == 5:
                break
            codigos = filtrar_produtos(estoque, filtros)
            if len(codigos) == 0:
                print()
                print('Nenhum produto encontrado')
                sleep(2)
            elif len(codigos) == 1:
                retorno_menu = menu_produto(estoque, codigos[0])
                if retorno_menu == 4:
                    break
            else:
                retorno_menu = 0
                while True:
                    retorno = mostrar_resultados(estoque, codigos)
                    if retorno == 0:
                        break
                    retorno_menu = menu_produto(estoque, retorno)
                    if retorno_menu == 4:
                        break
                if retorno_menu == 4:
                    break
    elif opcao == 3:
        modificacao = saida_estoque(estoque)
        if modificacao == 0:
            salvar_estoque(estoque)
        elif modificacao == -1:
            continue
    elif opcao == 4:
        print('\nFinalizando o programa...\n')
        break
    