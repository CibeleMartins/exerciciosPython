def salarioMedioSatisfacaoGarantida():

    listaColaboradores = []

    for i in range(0, 10):
        nome, salario = input("Digite seu nome e salário: ").split()
        

        listaColaboradores.append(nome)
        listaColaboradores.append(salario)

    print(listaColaboradores)
  


   
salarioMedioSatisfacaoGarantida()
