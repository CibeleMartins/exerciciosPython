def salarioMedioSatisfacaoGarantida():

    # colaborador = ''
    # salario = ''

    # colaborador, salario = map(str ,input("Digite o seu nome de colaborador e o seu salário separados por vírgula: ").split())

    # if(colaborador == "Fim" and salario):

    #     print(f"{colaborador}, {salario:.2f}")
    
    # salarioMedioSatisfacaoGarantida()

    colaborador_salario = input("Digite o seu nome e salário:  ").split()

    if("Fim" in colaborador_salario):
        
        map(lambda i: print(i), colaborador_salario)
    else:
        salarioMedioSatisfacaoGarantida()

  

    



   
salarioMedioSatisfacaoGarantida()
