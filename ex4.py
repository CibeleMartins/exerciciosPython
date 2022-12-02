"""Dado o seguinte programa copie-o no IDE Python para depurá-lo até funcionar corretamente:

S = input()
O = input()
P = input()
return = ( p + ( o + s ) )
print(Return)
A Entrada consiste de:
Entrada 1 - uma string com o sujeito da oração
Entrada 2 - uma string com o objeto da oração
Entrada 3 - uma string com o verbo da oração

A Saída deve apresentar:
Uma oração em língua portuguesa na ordem direta.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Procure por erros de sintaxe e de semântica.
"""

S, O, P = input().split()
retorno = (f"{S} {P} {O}")

print(retorno)