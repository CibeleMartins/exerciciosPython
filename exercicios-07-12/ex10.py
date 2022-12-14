#  uma fra sem numeros
# com letr maiuscula apenas no inicio
# com ponto final

def corrigeFrase():

    frase = input("Digite uma frase: ")

    if "9" in frase:

        nova_frase = frase.replace("9", "p")

        print(nova_frase)

        
        
    # if "6" in frase:

    #     index_seis = frase.index("6")
    #     frase[index_seis] = "b"
    
    print(frase)

corrigeFrase()