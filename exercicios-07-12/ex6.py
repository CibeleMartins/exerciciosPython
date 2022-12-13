# tamanho populacao
# taxa crescimento anual de 2 cidades A e B
# cidade menor A
# quando a cidade menor alcancara a B em populacao
# se for muito tempo n precisa saber o tempo

def aAlcancaraBEm():

    populacao_a, populacao_b = map(int, input("Digite a populacao da ciadade A e B: ").split())
    taxa_cresc_a, taxa_cresc_b = map(float,input("Digite a taxa de crescimento anual de A e B: ").split())

    print(populacao_a, populacao_b, taxa_cresc_a, taxa_cresc_b)

    anos = 0

    while(populacao_a <= populacao_b):

        anos += 1

        # print(anos)

        porcentagem_a = (taxa_cresc_a / 100) // 1
    

        populacao_a = populacao_a + (populacao_a * taxa_cresc_a / 100) // 1 
  
    
    print(f"Após {anos - 1} ano(s) cidade A alcançará a B em população.")
    print(f"Cidade A: %.0f" %(populacao_a - 1))
    print(f"Cidade B: %.0f" %(populacao_b))

aAlcancaraBEm()