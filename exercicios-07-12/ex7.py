# fibonacci sequencia de numeros inteiros
# comeca por 0
# cada termo subsequente corresponde a soma dos dois anteriores
# dois prmeiros valores da sequencia 0 e 1

def fibonacci(n):

    if n == 1:
        return 0

    if n == 2:
        return 1
    
    print(n)
    return fibonacci(n - 1) + fibonacci(n - 2) - 1

        

print(fibonacci(1))