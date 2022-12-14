from functools import lru_cache

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



