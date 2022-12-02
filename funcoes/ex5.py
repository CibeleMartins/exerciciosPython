def areas(A, B, C):
    retangulo = A * B
    triangulo = (B * C) / 2
    trapezio = (1/2)*A*(B + C)
    print(int(retangulo))
    print(int(triangulo))
    print(int(trapezio))
    print("\n")


areas(1, 2, 3)
areas(7, 3, 13)
areas(0, 12, 24)