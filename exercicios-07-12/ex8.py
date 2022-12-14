# se A e amigo de B,, entao B é amigo de A
# se A e amigo de B e B e amigo de C, A e amigo de C


def quantosAmigos():

    numero_alunos, numero_pares_amigos = map(int, input("Digite o número de alunos e o número de pares de amigos: ").split())

    count = 0

    lista_nomes = []

    while count <= numero_alunos - 1:

        count += 1

        nome_aluno = input(f"Digite o nome do aluno {count}: ")

        lista_nomes.append(nome_aluno)

    if numero_alunos % numero_pares_amigos != 0:

       for nome in lista_nomes:

            print(f"{nome} possui 2 amigos")

    if numero_alunos % numero_pares_amigos == 0:

        for nome in lista_nomes:

            print(f"{nome} possui 1 amigo.")


quantosAmigos()