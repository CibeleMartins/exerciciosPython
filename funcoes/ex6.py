def troco(cents):
    cinquenta = 0
    vinteECinco = 0
    dez = 0
    cinco = 0
    um = 0
    while cents >= 50:
        cents -= 50
        cinquenta += 1
    while cents >= 25:
        cents -= 25
        vinteECinco += 1
    while cents >= 10:
        cents -= 10
        dez += 1
    while cents >= 5:
        cents -= 5
        cinco += 1
    while cents >= 1:
        cents -= 1
        um += 1

    print(f"{cinquenta} moedas de R$ 0,50")
    print(f"{vinteECinco} moedas de R$ 0,25")
    print(f"{dez} moedas de R$ 0,10")
    print(f"{cinco} moedas de R$ 0,05")
    print(f"{um} moedas de R$ 0,01")
    print("\n")


troco(79)
troco(27)
troco(567)