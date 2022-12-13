def aAlcancaraBEm():

    populacao_a, populacao_b = map(int, input("Digite a populacao da ciadade A e B: ").split())
    taxa_cresc_a, taxa_cresc_b = map(float,input("Digite a taxa de crescimento anual de A e B: ").split())

    print(populacao_a, populacao_b, taxa_cresc_a, taxa_cresc_b)

    anos = 0

    while(populacao_b >= populacao_a):

        if taxa_cresc_a <= 0:
            print("A nunca alcancara B")

            break

        anos += 1

        populacao_a = (populacao_a + (populacao_a * (taxa_cresc_a / 100.0))) // 1
    
    if anos > 1000:
        print("Mais de um milenio.")
    else:
        print(f"Após {anos} ano(s) cidade A alcançará a B em população.")
        print(f"Cidade A: %.0f" %(populacao_a))
        print(f"Cidade B: %.0f" %(populacao_b))

aAlcancaraBEm()