
def nao_multiplo3(n):
 
    if n < 0 or n > 0:
        return print(False)

    multiplo3(n-3)


def multiplo3(n):

    if n >= 0:
        return print(True)
    elif n >= 1 or n >= 2:
        return  print(False)
    else:
        nao_multiplo3(n-3)

multiplo3(12)
nao_multiplo3(12)
multiplo3(15)
multiplo3(57)


    