def funcao_teste(valorResistencia):

    lista_cores_resistor = []

    cores_digito = {
        '0':'Preto',
        '1':'Marrom',
        '2':'Vermelho',
        '3':'Laranja',
        '4':'Amarelo',
        '5':'Verde',
        '6':'Azul',
        '7':'Violeta',
        '8':'Cinza',
        '9':'Branco'}

    dict_multiplicador = {
        'Rosa': 10 ** -3,
        'Prata': 10 ** -2,
        'Dourado': 10 ** -1,
        'Preto': 1,
        'Marrom': 10,
        'Vermelho': 10 ** 2,
        'Laranja': 10 ** 3,
        'Amarelo': 10 ** 4,
        'Verde': 10 ** 5,
        'Azul': 10 ** 6,
        'Violeta': 10 ** 7,
        'Cinza': 10 ** 8,
        'Branco': 10 ** 9}

    sinais_multiplicadores = {
        'm': 10 ** -3,
        '-': 1,
        'K': 10 ** 3,
        'M': 10 ** 6,
        'G': 10 ** 9,
    }

    tolerancia = {
        'Rosa': 0,
        'Prata': 10,
        'Marrom': 1,
        'Preto': 0,
        'Amarelo': 0.02,
        'Vermelho': 2,
        'Verde': 0.5,
        'Laranja': 0.05,
        'Azul': 0.25,
        'Violeta': 0.1,
        'Dourado': 5,
        'Nenhuma': 20,
        'Cinza': 0.01,
        'Branca': 0, }

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

    # pega o multiplicador
    sinal_multiplicador_resistencia = valorResistencia[index_multiplicador]
    valor_sinal_multiplicador = sinais_multiplicadores[sinal_multiplicador_resistencia]

    multiplicacao_sinal_resistencia = float(valor_resistencia) * (valor_sinal_multiplicador)

    digitos_restantes_resultado_multiplicacao = len(str(multiplicacao_sinal_resistencia)) - len(valor_resistencia)

    multiplicador_encontrado = 10 ** digitos_restantes_resultado_multiplicacao


    



funcao_teste('13m 0.02')
# IEC60062('13M 0.02')
funcao_teste('2.70M 0.01')
