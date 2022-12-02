""""

Menescraft é um popular jogo virtual de exploração e aventura. Nele seu objetivo é coletar recursos das mais diversas raridades para posterior 
comercialização com os aldeões encontrados pelo mapa.
No entanto, o sistema de trocas e vendas deste jogo é bastante desenvolvido de modo que até mesmo os aldeões controlados pelo computador 
não aceitarão trocas injustas, onde seja cobrado um valor exorbitante. Sabendo disso, imagine que em uma jogatina você foi capaz de reunir 
uma determinada quantidade de minérios de ferro, ouro, pó vermelho e diamantes. Ao pesquisar profundamente nos fóruns online você descobriu 
que o valor justo de uma remessa de minérios é calculada da seguinte forma: 

 Para cada minério de ferro o valor da remessa é acrescido em uma esmeralda. 
 Para cada minério de ouro o valor da remessa é duplicado. 
 Para cada pó vermelho o valor da remessa é acrescido em duas esmeraldas. 
 Para cada diamante o valor da remessa é quadruplicado. 
 É garantido que sempre haverá ao menos uma unidade de cada minério e que as quantidades encontradas de cada minério sempre serão números 
 inteiros positivos. Desta forma, o valor da remessa é sempre em número de esmeraldas. Como apresentado, ferro e pó vermelho fornecem ao jogador 
 o número inicial de esmeraldas.

A Entrada consiste de:
4 inteiros F, O, P e D que representam respectivamente as quantidades de minério de ferro, ouro, pó vermelho e diamantes encontrados.

A Saída deve apresentar:
O valor total em esmeraldas que deverá ser cobrado pela remessa de minérios, considerando o cálculo para um preço justo.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos."""


f, o, p, d = map(int, input().split())
esmeraldas = 0
esmeraldas += f
esmeraldas += 2 * p
esmeraldas = (esmeraldas * 2) * o
esmeraldas = (esmeraldas * 4) * d

print(esmeraldas)
