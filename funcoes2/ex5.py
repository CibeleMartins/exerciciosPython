def n_termo(i, r, n):
 
    inicial = i
    razao = r
    numero_elementos = n 

    for pa in range(inicial, numero_elementos, razao): 

        result = pa + inicial

    return result

print(n_termo(1,1,100))