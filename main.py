from time import sleep
from interface import menu, titulo
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
    if opcao == 1:
        titulo(opcoes[0].upper())
    elif opcao == 2:
        filtros = escolher_filtros(opcoes_filtro)
        print(filtros)
        print(filtrar_produtos(estoque, filtros))
    elif opcao == 3:
        titulo(opcoes[2].upper())
    elif opcao == 4:
        print('Finalizando o programa...')
        break
    sleep(1)
