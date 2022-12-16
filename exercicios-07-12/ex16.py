# criar substrings com a ordem de caracteres invertidos
# q consultas
# cada consulta tem 2 numeros inteiros


# 1 entrada: q um numero inteiro -> qtd consultas
# q linhas -> consutlas
# cada consulta -> l e r -> inteiros


q = int(input("Digite a quantidade de consultas: "))

string_resultado = ''

for i in range(0, q):

    l, r = input("Digite dois numeros: ").split()

    l = int(l)
    r = int(r)

    s = input("Insira uma string: ")

    string_final = s[l:r+1]

    string_invertida = string_final[::-1]

    string_resultado = string_resultado + " " + string_invertida + "\n"

print(string_resultado)

