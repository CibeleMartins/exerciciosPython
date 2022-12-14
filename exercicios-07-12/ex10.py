#  uma fra sem numeros
# com letr maiuscula apenas no inicio
# com ponto final

def corrigeFrase():

    frase = input("Digite uma frase: ")

    if "9" in frase:

        nova_frase = frase.replace("9", "p")

    print(nova_frase)

    if "6" in nova_frase:

        nova_frase2 = nova_frase.replace("6", "b")

    print(nova_frase2)

    if "5" in nova_frase2:

        nova_frase3 = nova_frase2.replace("5", "s")

    print(nova_frase3)

    if "7" in nova_frase3:

        nova_frase4 = nova_frase3.replace("7", "t")
    
    if "0" in nova_frase4:

        nova_frase5 = nova_frase4.replace("0", "o")

    if "1" in nova_frase5:

        nova_frase6 = nova_frase5.replace("1", "i")

    print(nova_frase6)

     
        
    



      


   

corrigeFrase()