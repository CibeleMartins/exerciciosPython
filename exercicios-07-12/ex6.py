# tamanho populacao
# taxa crescimento anual de 2 cidades A e B
# cidade menor A
# quando a cidade menor alcancara a B em populacao
# se for muito tempo n precisa saber o tempo

def aAlcancaraBEm():

    populacao_a, populacao_b = map(int, input("Digite a populacao da ciadade A e B: ").split())
    taxa_cresc_a, taxa_cresc_b = input("Digite a taxa -> \"%\" de crescimento anual de A e B: ").split()

    print(populacao_a, taxa_cresc_a, populacao_b, taxa_cresc_b)

aAlcancaraBEm()