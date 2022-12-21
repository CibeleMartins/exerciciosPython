# os numeros que estiver antes do pirmeiro caractere sao cores
# o caractere é o multiplicador
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

    multiplicador = {'Preto': 1,
                     'Marrom': 10,
                     'Vermelho': 100,
                     'Laranja': 1000,
                     'Amarelo': 10000,
                     'Verde': 100000,
                     'Azul': 1000000,
                     'Violeta': 10000000,
                     'Cinza': 100000000,
                     'Branco': 1000000000}

    caracteres_multiplicadores = {
        'm': '10 ** -3',
        '-': '1',
        'K': '10**3',
        'M': '10**6',
        'G': '10**9'
    }

    tolerancia = {'Marrom': '+/- 1 %',
                  'Vermelho': '+/- 2 %',
                  'Verde': "+/- 0.5 %",
                  'Azul': '+/- 0.25 %',
                  'Violeta': '+/- 0.1 %',
                  'Dourado': '+/- 5 %',
                  'Prata': '+/- 10 %',
                  'Nenhuma': '+/-20 %'}

    for multiplicador, valor in caracteres_multiplicadores.items():

        if multiplicador in valorResistencia:

            print(multiplicador)