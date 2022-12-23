# os numeros que estiver antes do pirmeiro caractere sao cores ok
# o caractere é o multiplicador ok
# o numero apos o espaco e a tolerancia

# parei na parte que eu estava tentando pegar o restante dos dígitos do resutlado da multiplicacao dos digitos pelo valor do sinal multiplicador e elevar a 10

def IEC60062(valorResistencia):

    cores_digito = {
        'Preto': '0',
        'Marrom': '1',
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

    caracteres_multiplicadores = {
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

    lista_cores_resistor = []

    for multiplicador, valor in caracteres_multiplicadores.items():
        # percorre uma lista de tuplas pegando chave e valor do dict caracteres_multiplicadores

        if multiplicador in valorResistencia:
            # verifica se tem algum sinal de multiplicador no valor da resistencia
            index_espaco = valorResistencia.index(' ') + 1
            tolerancia_string = valorResistencia[index_espaco:len(valorResistencia)]

            index_multiplicador = valorResistencia.index(multiplicador)
            # pega o indice desse sinal de multiplicador encontrado

            numeros_antes_multiplicador = valorResistencia[0:index_multiplicador]
            # faz um slicing e pega o valor da resistencia do indice 0 até o sinal multiplicador encontrado

            # multiplica digitos por valor do multiplicador
            multiplicacao = float(numeros_antes_multiplicador) * (valor)
            # transforma o resultado da multiplicacao em string
            multiplicacao_string = str(multiplicacao)

            multiplicacao_string_index_ponto = multiplicacao_string.index('.')
            # pega o indice do ponto no resultado da multiplicacao

            multiplicacao_string_sem_ponto = multiplicacao_string[0: multiplicacao_string_index_ponto]
            # faz um slicing do início da string até o indice do ponto

            if '.' in numeros_antes_multiplicador:
                # se nos dígitos antes do sinal multiplicador tiver ponto

                digitos_cores_sem_ponto = numeros_antes_multiplicador.translate(str.maketrans('', '', '.'))
                # retira o ponto
                digitos_restantes_multiplicacao = len(multiplicacao_string_sem_ponto) - len(digitos_cores_sem_ponto)
                # subtrai o tamanho da string do resultado da multiplicacao pelo tamanho/quantidade dos dígitos de cores
                multiplicador_encontrado = 10 ** digitos_restantes_multiplicacao
                # encontra o multiplicador elevando 10 a quantidade de digitos restantes do resultado da multiplicacao após
                # subtrai a quantidade de digitos de cores
                for cor, valor in cores_digito.items():
                    # transforma o dict de digito de cores em uma lista de tuplas, pega chave e o valor
                    if valor in digitos_cores_sem_ponto:
                        # verifica se tem algum valor do dicionario de digito de cores nos digitos da resistencia antes do sinal multiplicador
                        lista_cores_resistor.append(cor)
                        # envia a cor correspondente aos valore para um array
                for chave_multiplicador, valor_multiplicador in dict_multiplicador.items():

                    if valor_multiplicador == multiplicador_encontrado:

                        lista_cores_resistor.append(chave_multiplicador)

                for chave_tolerancia, valor_tolerancia in tolerancia.items():

                    if str(valor_tolerancia) == tolerancia_string:

                        lista_cores_resistor.append(chave_tolerancia)

            else:
                    # se nao tiver ponto nos dígitos antes do sinal multiplicador repete as mesmas intrucoes para esses dígitos
                for cor, valor in cores_digito.items():

                    if valor in numeros_antes_multiplicador:

                        lista_cores_resistor.append(cor)

                if int(multiplicacao_string_sem_ponto) > 0:

                    digitos_restantes_multiplicacao = len(multiplicacao_string_sem_ponto) - len(numeros_antes_multiplicador) 
                    multiplicador_encontrado = 10 ** digitos_restantes_multiplicacao

                else:
                    digitos_restantes_multiplicacao = len(multiplicacao_string_sem_ponto) - len(numeros_antes_multiplicador) + (-2)
                    multiplicador_encontrado = 10 ** digitos_restantes_multiplicacao


                for chave_multiplicador, valor_multiplicador in dict_multiplicador.items():

                    if valor_multiplicador == multiplicador_encontrado:

                        lista_cores_resistor.append(chave_multiplicador)

                for chave_tolerancia, valor_tolerancia in tolerancia.items():

                    if str(valor_tolerancia) == tolerancia_string:

                        lista_cores_resistor.append(chave_tolerancia)

    print(lista_cores_resistor)


IEC60062('13m 0.02')
IEC60062('13M 0.02')
IEC60062('2.70M 0.01')


