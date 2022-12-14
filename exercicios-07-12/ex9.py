def apelido():

    nome_amigo = input("Digite o nome do amigo de Luzinha: ")

    if len(nome_amigo) == 3:

        primeira_letra = nome_amigo[0]

        segunda_letra = nome_amigo[1]

        apelido = primeira_letra + segunda_letra

        print(apelido)

    if ' ' in nome_amigo:

        primeira_letra_nome = nome_amigo[0]
        segunda_letra_nome = nome_amigo[1]

        espaco = nome_amigo.index(" ")

        segundo_nome = nome_amigo[espaco + 1:13]

        primeira_letra_segundo_n = segundo_nome[0]

        segunda_letra_segundo_n = segundo_nome[1]

        apelido = primeira_letra_nome + segunda_letra_nome + \
            primeira_letra_segundo_n + segunda_letra_segundo_n

        print(apelido)

    if len(nome_amigo) > 3:

        primeira_letra = nome_amigo[0]
        segunda_letra = nome_amigo[1]
        terceira_letra = nome_amigo[2]

        apelido = primeira_letra + segunda_letra + terceira_letra

        print(apelido)


apelido()
