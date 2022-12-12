import functools
def maiorMenorMedia():

    n = int(input("Digite um número: "))

    listaColaboradores = []
    listaSalarios = []

    for i in range(0, n):

        # nome, salario = input("Digite seu nome e seu salário: ").split()

        nome = input("Digite seu nome: ")
        salario = input("Digite seu salário: ")

        juncao_nome_salario = nome + ', ' + salario
       
        listaColaboradores.append(juncao_nome_salario)
        listaSalarios.append(float(salario))
        # listaColaboradores.append(salario)
    
    soma_salarios = functools.reduce(lambda a, p: a + p)

    media_salarial = soma_salarios / len(listaSalarios)

    print(*listaColaboradores, sep="\n")







maiorMenorMedia()