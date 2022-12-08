def salarioMedioSatisfacaoGarantida():

    colaborador = ''
    salario = ''

    colaborador, salario = input("Digite o seu nome de colaborador e o seu salário separados por vírgula: ").split()

    if(str(colaborador) == "cibele"):

        print(f"{colaborador}, {salario:.2f}")
    
    salarioMedioSatisfacaoGarantida()

  

    



   
salarioMedioSatisfacaoGarantida()
