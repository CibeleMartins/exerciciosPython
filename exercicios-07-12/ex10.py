#  uma fra sem numeros
# com letr maiuscula apenas no inicio
# com ponto final

def corrigeFrase():

    frase = input("Digite uma frase: ")

    if "9" in frase:

       nova_frase = frase.replace("9", "p")
       print(nova_frase)
    
    if "6" in nova_frase or "6" in frase:

        nova_frase2 = nova_frase.replace("6", "b") or frase.replace("6", "b")
        print(nova_frase2)  

    if "5" in nova_frase2 or "5" in frase or "5" in nova_frase:

        nova_frase3 = nova_frase2.replace("5", "s") or nova_frase.replace("5", "s") or frase.replace("5", "s")
        print(nova_frase3)
   
corrigeFrase()