import functools

def salarioMedioSatisfacaoGarantida():

    listaColaboradores = []

    for i in range(0, 9999):
        nome, salario = input("Digite seu nome e salário: ").split()
        listaColaboradores.append(nome)
        listaColaboradores.append(salario)

        if nome == "Fim":
            break

    listaSalarios = []     

    for salario in range(0 + 1, len(listaColaboradores), 2):
        # print(salario)
        print(listaColaboradores[salario])

        listaSalarios.append(listaColaboradores[salario])

    
    soma_salarios = functools.reduce(lambda atual, proximo: float(atual) + float(proximo), listaSalarios )

    print(listaSalarios, soma_salarios)
    
    print(listaColaboradores)

    media_salarial = soma_salarios / (len(listaSalarios) - 1)

    print(f"A média salarial é de %.2f" %(media_salarial))




  


   
salarioMedioSatisfacaoGarantida()
