def corrigeFrase():

    frase = input("Digite uma frase: ")

    substituicao_numeros = frase.replace("9", "p").replace("6", "b").replace(
        "5", "s").replace("7", "t").replace("0", "o").replace("1", "i")

    frase_corrigida = substituicao_numeros.capitalize()

    if frase_corrigida.endswith('.'):
        print(True)
        print(frase_corrigida)
    else:
        print(frase_corrigida + '.')


corrigeFrase()
