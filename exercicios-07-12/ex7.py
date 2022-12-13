# fibonacci sequencia de numeros inteiros ok
# comeca por 0 ok
# dois prmeiros valores da sequencia 0 e 1
# cada termo subsequente corresponde a soma dos dois anteriores


# def fibonacci(n):

#     if n == 1:
#         return 0

#     if n == 2:
#         return 1

#     print(n)
#     return fibonacci(n - 1) + fibonacci(n - 2) - 1


# print(fibonacci(1))

def fibonacci(n):

    for i in range(0, n):

        if i == 0:
            print(0)
        if i == 1:
            print(1)

        if i > 1:

            fibo = i - 1
            nacci = i - 2

            termo = fibo + nacci

            print(termo)
 


fibonacci(10)
