import functools

def maiorMenorMedia():

    n = int(input("Digite um número: "))

    if n == 0:
        print("Não tem média")
        print("Não tem")
        print("Não tem")

    listaColaboradores = []
    listaSalarios = []

    for i in range(0, n):

        nome = input("Digite seu nome: ")
        salario = input("Digite seu salário: ")

        juncao_nome_salario = nome + ',' + salario
       
        listaColaboradores.append(juncao_nome_salario)
        listaSalarios.append(float(salario))
        # listaColaboradores.append(salario)
    if len(listaSalarios) > 0:
        soma_salarios = functools.reduce(lambda a, p: a + p, listaSalarios)

        media_salarial = soma_salarios / len(listaSalarios)

        media_salarial_float = float(media_salarial)

    if len(listaColaboradores) > 0:

        for maior_salario in listaColaboradores:

            # virgula = ',' in maior_salario

            virgula = maior_salario.find(",")
            
            tamanho_string = len(maior_salario)

            salario = int(maior_salario[virgula + 1:tamanho_string])

            colaborador_maior_salario = max(listaSalarios)
            colaborador_menor_salario = min(listaSalarios)

            if float(salario) == colaborador_maior_salario:
                
                ganha_mais = maior_salario

            if float(salario) == colaborador_menor_salario:

                ganha_menos = maior_salario
        
        print(f"%.2f {ganha_mais} {ganha_menos}" %(media_salarial_float), sep="\n")

maiorMenorMedia()