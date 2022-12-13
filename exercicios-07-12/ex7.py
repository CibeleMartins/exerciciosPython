# fibonacci sequencia de numeros inteiros ok
# comeca por 0 ok
# dois prmeiros valores da sequencia 0 e 1 ok
# cada termo subsequente corresponde a soma dos dois anteriores

def fibonacci(n):

    termo_1 = 0
    termo_2 = 1

    count = 3
    print(termo_1, termo_2, end=' ')

    while count <= n:

        termo_3 = termo_1 + termo_2
        print(termo_3, end=' ')
        termo_1 = termo_2
        termo_2 = termo_3

        count += 1

       
        

fibonacci(10)
