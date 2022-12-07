import statistics

def calculaMedia():

    n1, n2, n3 = map(int,input("Digite 3 números positivos: ").split(" "))

    caractere = input("Digite um caractere: ")

    listaNotas = []
    listaNotas.append(n1)
    listaNotas.append(n2)
    listaNotas.append(n3)

    # quantidade_vezes_nota1 = listaNotas.count(n1)
    # quantidade_vezes_nota2 = listaNotas.count(n2)
    # quantidade_vezes_nota3 = listaNotas.count(n3)

    if(caractere == "A" or caractere == "a"):

        soma = n1 + n2 + n3
        mediaAritmetica = soma / 3
        return print(f"A média aritmética é: {mediaAritmetica}")

    elif(caractere == "P" or caractere == "p"):

        peso1, peso2, peso3 = map(float, input("Digite um peso para cada nota: ").split(" "))

        somaNotaVezesPeso = (n1 * peso1) + (n2 * peso2) + (n3 * peso3)
        somaPesos = peso1 + peso2 + peso3

        mediaPonderada = somaNotaVezesPeso / somaPesos
        return print(f"A média aritmética ponderada é: {mediaPonderada}")

    elif (caractere == "H" or caractere == "h"):

        mediaHarmonica = statistics.harmonic_mean(listaNotas)
        print(f"A média harmonica é: {mediaHarmonica}")


calculaMedia()