def calculaMedia():

    n1, n2, n3 = map(int,input("Digite 3 números positivos: ").split(" "))

    caractere = input("Digite um caractere: ")

    listaNotas = []
    listaNotas.append(n1)
    listaNotas.append(n2)
    listaNotas.append(n3)

    quantidade_vezes_nota1 = listaNotas.count(n1)
    quantidade_vezes_nota2 = listaNotas.count(n2)
    quantidade_vezes_nota3 = listaNotas.count(n3)

    # print(n1, n2, n3, listaNotas, quantidade_vezes_nota)

    if(caractere == "A" or caractere == "a"):

        soma = n1 + n2 + n3
        mediaAritmetica = soma / 3
        return print(f"A média aritmética é: {mediaAritmetica}")

    elif(caractere == "P" or caractere == "p"):

        somaNotaVezesPeso = (n1 * quantidade_vezes_nota1) + (n2 * quantidade_vezes_nota2) + (n3 * quantidade_vezes_nota3)
        somaPesos = quantidade_vezes_nota1 + quantidade_vezes_nota2 + quantidade_vezes_nota3

        mediaPonderada = somaNotaVezesPeso / somaPesos
        return print(f"A média aritmética ponderada é: {mediaPonderada}")




calculaMedia()