# os numeros que estiver antes do pirmeiro caractere sao cores ok
# o caractere é o multiplicador ok
# o numero apos o espaco e a tolerancia

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
                    'Rosa':'10 ** -3',
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

    tolerancia = {'Marrom': '+/- 1 %',
                  'Vermelho': '+/- 2 %',
                  'Verde': "+/- 0.5 %",
                  'Azul': '+/- 0.25 %',
                  'Violeta': '+/- 0.1 %',
                  'Dourado': '+/- 5 %',
                  'Prata': '+/- 10 %',
                  'Nenhuma': '+/-20 %'}

    lista_cores_resistor = []

    for multiplicador, valor in caracteres_multiplicadores.items():
        # percorre uma lista de tuplas pegando chave e valor do dict caracteres_multiplicadores

        if multiplicador in valorResistencia:
            # verifica se tem algum sinal de multiplicador no valor da resistencia

            valor_encontrado = caracteres_multiplicadores[multiplicador]

            index_multiplicador = valorResistencia.index(multiplicador)
            # pega o indice desse sinal de multiplicador encontrado

            numeros_antes_multiplicador = valorResistencia[0:index_multiplicador]
            # faz um slicing e pega o valor da resistencia do indice 0 até o sinal multiplicador encontrado

            # multiplica digitos por valor do multiplicador 
            multiplicacao = float(numeros_antes_multiplicador) * (valor)
            multiplicacao_string = str(multiplicacao)

            print(multiplicacao, multiplicacao_string, type(numeros_antes_multiplicador))

            multiplicacao_string_index_ponto = multiplicacao_string.index('.')

            multiplicacao_string_sem_ponto = multiplicacao_string[0: multiplicacao_string_index_ponto]

            qtd_digitos_iguais = 0

            for i in range(0, len(numeros_antes_multiplicador) - 1):

                if multiplicacao_string_sem_ponto[i] in numeros_antes_multiplicador:

                    qtd_digitos_iguais +=1

            qtd_digitos_restantes = len(multiplicacao_string_sem_ponto) - qtd_digitos_iguais

            # print(qtd_digitos_restantes)

            valor_multiplicador = 10 ** qtd_digitos_restantes

            # for cor_dict_multiplicador, valor_dict_multiplicador in dict_multiplicador.items():

            #     if valor_dict_multiplicador == valor_multiplicador:

            #         print(cor_dict_multiplicador)
                
            

            # se o meu tamanho de digitos é 3/4/5
            # significa que só posso ter 3/4/5 digitos iguais no resultado da multiplicacao 
            # dos meus digitos pelo valor do sinal multiplicador

            if '.' in numeros_antes_multiplicador:
                # se nos dígitos antes do sinal multiplicador tiver ponto

               digitos_cores_sem_ponto = numeros_antes_multiplicador.translate(str.maketrans('', '', '.'))
                # retira o ponto
               for cor, valor in cores_digito.items():
                # transforma o dict de digito de cores em uma lista de tuplas, pega chave e o valor
                if valor in digitos_cores_sem_ponto:
                    # verifica se tem algum valor do dicionario de digito de cores nos digitos da resistencia antes do sinal multiplicador
                    lista_cores_resistor.append(cor)
                    # envia a cor correspondente aos valore para um array
                    # print(lista_cores_resistor)
            else:
                # se nao tiver ponto nos dígitos antes do sinal multiplicador repete as mesmas intrucoes para esses dígitos
                for cor, valor in cores_digito.items():

                    if valor in numeros_antes_multiplicador:

                        lista_cores_resistor.append(cor)
                        # print(lista_cores_resistor)
            

            # for chave_cor, valor_multiplicador in dict_multiplicador.items():

            #     if valor_multiplicador == valor_encontrado:
                    
            #         lista_cores_resistor.append(chave_cor)
            #         print(lista_cores_resistor)



# print(pow(10,-3))

# print(13 * 0.001)