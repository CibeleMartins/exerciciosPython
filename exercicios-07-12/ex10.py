#  uma fra sem numeros
# com letr maiuscula apenas no inicio
# com ponto final

def corrigeFrase():

    frase = input("Digite uma frase: ")

    # index_9 = frase.index("9")

    # index_6 = frase.index("6")

    # index_5 = frase.index("5")

    # index_7 = frase.index("7")

    # index_0 = frase.index("0")

    # index_1 = frase.index("1")



    if "9" in frase:

        nova_frase = frase.replace("9", "p")

        print(nova_frase)

    if "6" in nova_frase:

        nova_frase2 = nova_frase.replace("6", "b")

        print(nova_frase2)

     
        
    



      

    # if "6" in frase:

    #     nova_frase = frase.replace("6", "b")

    #     print(nova_frase)

    # if "5" in frase:

    #     nova_frase = frase.replace("5", "s")

    #     print(nova_frase)

    # if "7" in frase:

    #     nova_frase = frase.replace("7", "t")

    #     print(nova_frase)

    # if "0" in frase:

    #     nova_frase = frase.replace("0", "o")

    #     print(nova_frase)
    
    # if "1" in frase:

    #     nova_frase = frase.replace("1", "i")

    #     print(nova_frase)

        
        
    # if "6" in frase:

    #     index_seis = frase.index("6")
    #     frase[index_seis] = "b"
   

corrigeFrase()