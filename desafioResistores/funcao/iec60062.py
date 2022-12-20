def IEC60062(valorResistencia):

    cores_digito = {
                   'Rosa': '',
                   'Prata': '',
                   'Dourada': '',
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
                  'Marrom':10,
                  'Vermelho':100,
                  'Laranja':1000,
                  'Amarelo':10000,
                  'Verde':100000,
                  'Azul':1000000,
                  'Violeta':10000000,
                  'Cinza':100000000,
                  'Branco':1000000000}

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

    if qtd_digitos == 3:
        # se tiver 3 digitos cada um será uma cor

        string_digitos = str(digitos)
        print(string_digitos)

        for i in range(0, len(cores_digito)):

               if string_digitos[i] == cores_digito[i]:
                    print('tem sim')



    # print(digitos)
# print(pow(10, 4))




# para um resistor de 5 faixas a 4 faixa colorida mostra o multiplicador
