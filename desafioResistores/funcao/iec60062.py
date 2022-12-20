def IEC60062(valorResistencia):

    cores_digito = {'Preto': '0',
                   'Marrom': '1',
                   'Vermelho': '2',
                   'Laranja': '3',
                   'Amarelo': '4',
                   'Verde': '5',
                   'Azul': '6',
                   'Violeta': '7',
                   'Cinza': '8',
                   'Branco': '9'}

    multiplicador = {'Preto': '1',
                  'Marrom': '10',
                  'Vermelho': '100',
                  'Laranja': '1k',
                  'Amarelo': '10k',
                  'Verde': '100k',
                  'Azul': '1M',
                  'Violeta': '10M',
                  'Cinza': '100M',
                  'Branco': '1G'}

    tolerancia = {'Marrom': '+/- 1 %',
                 'Vermelho': '+/- 2 %',
                 'Verde': "+/- 0.5 %",
                 'Azul': '+/- 0.25 %',
                 'Violeta': '+/- 0.1 %',
                 'Dourado': '+/- 5 %',
                 'Prata': '+/- 10 %',
                 'Nenhuma': '+/-20 %'}

    digitos = ''.join(v for v in valorResistencia if v.isdigit())
    # peguei os digitos

    qtd_digitos = len(str(digitos))
    # transformei em string para saber o tamanho/quantidade de digitos

    # if qtd_digitos == 3:


print(pow(5, 10))


# para um resistor de 5 faixas a 4 faixa colorida mostra o multiplicador
