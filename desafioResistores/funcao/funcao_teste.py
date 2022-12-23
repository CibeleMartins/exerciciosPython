def funcao_teste(valorResistencia):

        cores_digito = {
        '0': 'Preto',
        '1': 'Marrom',
        'Vermelho': '2',
        'Laranja': '3',
        'Amarelo': '4',
        'Verde': '5',
        'Azul': '6',
        'Violeta': '7',
        'Cinza': '8',
        'Branco': '9'}

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
        'Branca': 0,}


        for chave, valor in sinais_multiplicadores.items():

            if chave in valorResistencia:
                index_espaco_resistencia = valorResistencia.index(' ') + 1
                tolerancia_resistencia = valorResistencia[index_espaco_resistencia:len(valorResistencia)]

                index_multiplicador = valorResistencia.index(chave)
                valor_resistencia = valorResistencia[0:index_multiplicador]

                print(valor_resistencia)
        # pegou as partes do valor da resistencia, antes do sinal do multiplicador e depois do espaco

        for i in valor_resistencia:

            print(cores_digito[i])



               
            
        


# funcao_teste('13m 0.02')
# IEC60062('13M 0.02')
funcao_teste('2.70M 0.01')
