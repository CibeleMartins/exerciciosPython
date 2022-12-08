def salarioMedioSatisfacaoGarantida():

    listaColaboradores = []

    for i in range(0, 10):
        nome, salario = input("Digite seu nome e salário: ").split()
        listaColaboradores.append(nome)
        listaColaboradores.append(salario)

        if nome == "Fim":
            break
            
    for salario in range(0, len(listaColaboradores), 2):
            
        print(listaColaboradores[salario])
    
    print(listaColaboradores)


  


   
salarioMedioSatisfacaoGarantida()
