def soma_digitos(n):

    soma = 0

    for i in str(n):

        soma = soma + int(i)
    
    print(soma)


soma_digitos(467)