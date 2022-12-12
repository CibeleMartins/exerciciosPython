import functools

def maiorMenorMedia():

    n = int(input("Digite um número: "))

    listaColaboradores = []
    listaSalarios = []

    for i in range(0, n):

        # nome, salario = input("Digite seu nome e seu salário: ").split()

        nome = input("Digite seu nome: ")
        salario = input("Digite seu salário: ")

        juncao_nome_salario = nome + ',' + salario
       
        listaColaboradores.append(juncao_nome_salario)
        listaSalarios.append(float(salario))
        # listaColaboradores.append(salario)
    
    soma_salarios = functools.reduce(lambda a, p: a + p, listaSalarios)

    media_salarial = soma_salarios / len(listaSalarios)

    for maior_salario in listaColaboradores:

        # virgula = ',' in maior_salario

        virgula = maior_salario.find(",")
        
        tamanho_string = len(maior_salario)

        salario = int(maior_salario[virgula + 1:tamanho_string])

            
        colaborador_maior_salario = max(listaSalarios)
        colaborador_menor_salario = min(listaSalarios)

        ganha_mais = str(colaborador_maior_salario) in maior_salario

        ganha_menos = str(colaborador_menor_salario) in  maior_salario

        print(colaborador_maior_salario,ganha_mais, ganha_menos)

        if(ganha_mais):
            print(listaColaboradores[maior_salario])
        elif(ganha_menos):
            print(listaColaboradores[maior_salario])





        

    # print(*listaColaboradores, sep="\n")







maiorMenorMedia()