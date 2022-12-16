def positivo(n):
    if n >= 0:
        return True
    else:
        return False


x = input()
acumulador = 0
count = 0
while x != "f":
    x = int(x)
    if not positivo(x):
        count += 1
        acumulador += x
    x = input()

if count > 0:
    media_negativo = acumulador/count
    print(media_negativo)
else:
    print("0.0")


positivo(10)
