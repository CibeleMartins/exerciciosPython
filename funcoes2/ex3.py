def imprimeTermos(num):

  if num-2 >= 0:

    print(num)
    imprimeTermos(num-2)

  elif num == 1:
    print(num)
    imprimeTermos(num-1)

  else:
    print(0)

imprimeTermos(15)

