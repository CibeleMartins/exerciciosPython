"""Escreva um programa que recebe um número inteiro  de dois dígitos, mas representado como um número real com zeros após o ponto decimal. 
Retorne a parte inteira desse número multiplicado por 100 mais ele mesmo, isto é, um inteiro de quatro dígitos.
A Entrada consiste de:
Um número inteiro 𝑥, tal que 10.00≤𝑥<99.00
A Saída deve apresentar:
Um número inteiro 𝑦, tal que 1000≤𝑥<9999
Observações:
Não é necessário validar se os valores de entrada são do tipo definido.
Descrição dos Exemplos:
No primeiro exemplo a entrada é o número 51. Multiplicando este número uma vez por 100 e somando ele ao resultado da multiplicação a saída é 5151."""

num = input("Digite um numero inteiro maior que 10 e menor que 99: ")
num = float(num)

y = num * 100 + num

print(f"resultado: {int(y)}")