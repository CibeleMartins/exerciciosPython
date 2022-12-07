def raizes(a, b, c):

    delta = (b**2) - (4 * a * c) 
 
    print(delta)
    if(delta < 0):
        print("Não há raízes reais!")

    elif (delta == 0):

       result = b / (2 * a)

       print(f"Há {result} raízes reais")
    else:
        print("Possui duas raízes reais!")



raizes(6,11,-35)
raizes(2,4,2)
raizes(-4,-7,-12)