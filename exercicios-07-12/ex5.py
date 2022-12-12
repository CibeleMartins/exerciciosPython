import functools

def vamosAoShow():

    quantidade_amigos, preco_ingresso = map(int, input("Digite a quantidade de amigos e o valor do ingresso: ").split(" "))

    lista_dinheiro_amigos = []

    for i in range(0, quantidade_amigos):

        amigo = i + 1
        
        # dinheiro_amigo = int(input(f"Digite a quantidade de dinheiro que o amigo: {amigo} tem: "))

        lista_dinheiro_amigos.append(int(input(f"Digite a quantidade de dinheiro que o amigo: {amigo} tem: ")))

    soma_dinheiro_amigos = functools.reduce(lambda a, p: a + p, lista_dinheiro_amigos)

    media = soma_dinheiro_amigos / quantidade_amigos

    print(f"Média: %.0f" %(media))

    if media > preco_ingresso:
        print("O rock reinará mais uma vez!")
    else:
        print("Rockeiros trabalhando já!")

vamosAoShow()