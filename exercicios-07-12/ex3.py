

def maiorSalario():

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
        # print(listaColaboradores[salario])

        listaSalarios.append(listaColaboradores[salario])
    

    salarios_float = map(lambda i: float(i), listaSalarios)
    
    for salario_numero in salarios_float:
        print(f"O maior salário é:", max(salarios_float))

maiorSalario()
