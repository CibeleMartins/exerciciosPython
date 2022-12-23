def IEC60062(valorResistencia):

    lista_cores_resistor = []

    cores_digito = {
        '0': 'Preto',
        '1': 'Marrom',
        '2': 'Vermelho',
        '3': 'Laranja',
        '4': 'Amarelo',
        '5': 'Verde',
        '6': 'Azul',
        '7': 'Violeta',
        '8': 'Cinza',
        '9': 'Branco'}

    dict_multiplicador = {
        10 ** -3: 'Rosa',
        10 ** -2: 'Prata',
        10 ** -1: 'Dourado',
        1: 'Preto',
        10: 'Marrom',
        10 ** 2: 'Vermelho',
        10 ** 3: 'Laranja',
        10 ** 4: 'Amarelo',
        10 ** 5: 'Verde',
        10 ** 6: 'Azul',
        10 ** 7: 'Violeta',
        10 ** 8: 'Cinza',
        10 ** 9: 'Branco'}

    sinais_multiplicadores = {
        'm': 10 ** -3,
        '-': 1,
        'K': 10 ** 3,
        'M': 10 ** 6,
        'G': 10 ** 9,
    }

    tolerancia = {
        0: 'Rosa',
        10:'Prata',
        1:'Marrom',
        0:'Preto',
        0.02: 'Amarelo',
        2:'Vermelho',
        0.5:'Verde',
        0.05:'Laranja',
        0.25:'Azul',
        0.1:'Violeta',
        5:'Dourado',
        20:'Nenhuma',
        0.01:'Cinza',
        0:'Branca', }

    for chave, valor in sinais_multiplicadores.items():

        if chave in valorResistencia:
            index_espaco_resistencia = valorResistencia.index(' ') + 1
            tolerancia_resistencia = valorResistencia[index_espaco_resistencia:len(
                valorResistencia)]

            index_multiplicador = valorResistencia.index(chave)
            valor_resistencia = valorResistencia[0:index_multiplicador]

    # pegou as partes do valor da resistencia, antes do sinal do multiplicador e depois do espaco

    for i in valor_resistencia.replace('.', ''):
        # percorre a string do valor da resistencia substituindo o '.' por ''
        lista_cores_resistor.append(cores_digito[i])
        # acessa o dict de cores p/ dígitos com base nos nos numeros da resistencia
        # manda para a lista de cores do resistor

    # pega cor do multiplicador
    multiplicador = sinais_multiplicadores[valorResistencia[index_multiplicador]]
    # print(multiplicador)

    tamanho = 3 if len(valor_resistencia.replace('.', '')) == 3 else 2

    if len(valor_resistencia) == 1:

        while float(valor_resistencia) < 10**(tamanho - 2):

            valor_resistencia = float(valor_resistencia) * 10
            multiplicador = multiplicador / 10

        multiplicador_encontrado = dict_multiplicador[multiplicador]

        lista_cores_resistor.append(multiplicador_encontrado)

        print(multiplicador_encontrado)


    while float(valor_resistencia) < 10**(tamanho-1):

        valor_resistencia = float(valor_resistencia) * 10
        multiplicador = multiplicador / 10

    multiplicador_encontrado = dict_multiplicador[multiplicador]

    lista_cores_resistor.append(multiplicador_encontrado)

    # pega cor da tolerancia
    tolerancia_encontrada = tolerancia[float(tolerancia_resistencia)]

    lista_cores_resistor.append(tolerancia_encontrada)

    print(lista_cores_resistor)


IEC60062('1- 10')
IEC60062('13m 0.02')
IEC60062('2.70M 0.01')
IEC60062('2.26K 0.05')
IEC60062('2.7M 1')
IEC60062('2.2K 2')
