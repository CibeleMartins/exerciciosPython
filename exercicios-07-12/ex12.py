
palavra = input("Digite uma palavra: ")

for i in palavra:

    qtd_letras_maiusculas = palavra.count(i.upper())
    qtd_letras_minusculas= palavra.count(i.lower())

if qtd_letras_maiusculas > qtd_letras_minusculas:

    print(palavra.upper())

else:
    print(palavra.lower())