# Drikinha gosta de bolos de vários sabores.
# Uma vez por semana ela vai em uma padaria perto de casa e pede x pedaços de bolo de algum sabor,
# o pedaço de bolo tem o valor fixo de 3.25 reais, independentemente do sabor.
# Escreva um programa que recebe o sabor do bolo e a quantidade de pedaços que Drikinha irá comprar
# e retorne a frase do atendente: "Foram 𝑥 pedaços de bolo de 𝑠, então fica 𝑧 reais".
# Onde 𝑥 é a quantidade de pedaços, 𝑠 o sabor do bolo e 𝑧 o total da compra de Drikinha em reais.
# Imprima o valor da compra com apenas duas casas após a vírgula.

# s = input("Bom dia Drikinha, qual o sabor de bolo você vai querer? \n")
# x = input("E quantos pedaços? \n")
s, x = input("Bom dia Drikinha, qual o sabor de bolo você vai querer? E quantos pedaços? \n").split(" ")
x = int(x)
preco = 3.25

z = preco * x

print(f"Foram {𝑥} pedaços de bolo de {𝑠}, então fica {z:.2f} reais")