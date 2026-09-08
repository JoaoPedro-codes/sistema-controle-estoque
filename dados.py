def carregar_estoque():
    estoque = {}

    try:
        with open('estoque.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                termos = linha.strip().split(';')
                
                codigo = int(termos[0])
                quantidade = int(termos[4])
                preco = float(termos[5])

                estoque[codigo] = {
                    'Tipo': termos[1],
                    'Marca': termos[2],
                    'Categoria': termos[3],
                    'Quantidade': quantidade,
                    'Preço': preco,
                    'Status': termos[6]
                }

    except FileNotFoundError:
        pass

    return estoque


def salvar_estoque(estoque):
    with open('estoque.txt', 'w', encoding='utf-8') as arquivo:
        for codigo, produto in estoque.items():
            arquivo.write(
                f"{codigo};{produto['Tipo']};{produto['Marca']};"
                f"{produto['Categoria']};{produto['Quantidade']};"
                f"{produto['Preço']};{produto['Status']}\n"
            )


opcoes_filtro = {
    1: 'Tipo',
    2: 'Marca',
    3: 'Categoria',
    4: 'Status'
}


opcoes_alteracao = {
    1: 'Tipo',
    2: 'Marca',
    3: 'Categoria',
    4: 'Preço'
}


opcoes_status = [
    'DISPONÍVEL', 
    'ESGOTADO', 
    'INATIVO'
]