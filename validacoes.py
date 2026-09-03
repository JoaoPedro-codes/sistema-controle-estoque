def leiaTexto(msg):
    while True:
        texto = input(msg).strip()
        if not texto:
            print('\nERRO: Esse campo não pode estar vazio ou conter apenas espaços!\n')
            continue
        else:
            return texto


def leiaFloat(valor):
    while True:
        try:
             quantia = float(input(valor)) 
        except (ValueError, TypeError):
            print('\nERRO: Digite um valor numérico válido!\n')
        else:
            if quantia <= 0:
                print('\nERRO: O valor não pode ser zero \n')
            else:
                return quantia