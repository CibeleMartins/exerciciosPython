
resultado = ""

s, w, n = input("Digite duas strings e um numero: ").split()

n = int(n)

resultado += s

while len(resultado) % n != 0:

    resultado += w

print(resultado)