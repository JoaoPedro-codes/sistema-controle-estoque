def leiaTexto(msg):
    while True:
        texto = input(msg).strip()
        if not texto:
            print('\nERRO: Esse campo não pode estar vazio ou conter apenas espaços!\n')
            continue
        if ';' in texto:
            print('\nERRO: O caractere ";" não é permitido!\n')
            continue

        return texto


def leiaFloat(valor):
    while True:
        try:
             quantia = float(input(valor)) 
        except (ValueError, TypeError):
            print('\nERRO: Digite um valor numérico válido!\n')
        else:
            if quantia <= 0:
                print('\nERRO: O valor deve ser maior que zero\n')
            else:
                return quantia


def leiaInt(opc, msg='\nERRO: Por favor, digite apenas opções válidas!\n'):
    while True:
        try:
             opcao = int(input(opc)) 
        except (ValueError, TypeError):
            print(msg)
        else:
            return opcao


def leiaIntOpcional(opc):
    while True:
        opcao = (input(opc)).strip()
        if opcao == "":
            opcao = 0
        try:
             opcao = int(opcao) 
        except ValueError:
            print('\nERRO: Por favor, digite apenas opções válidas!\n')
        else:
            return opcao


def leiaSimNao(msg):
    while True:
        resposta = input(msg).strip().upper()

        if resposta not in ('S', 'N'):
            print('\nERRO: Digite apenas S ou N!\n')
            continue

        return resposta