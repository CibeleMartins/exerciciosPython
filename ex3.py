""""Cebolinha e Cascão acabaram de ler todos os gibis da Turma da Mônica. Como eles não tem mais nada pra fazer, já que a Mônica viajou, 
decidiram fazer uma brincadeira: os dois procuraram todas as onomatopeias dos gibis e formam novas a partir de três existentes. 
Para formar uma nova onomatopeia eles juntam a primeira string com três ocorrências da segunda e duas da terceira. Escreva um programa que dadas 
três onomatopeias, crie uma nova seguindo a lógica dos amigos do Bairro do Limoeiro.
A Entrada consiste de:
Três strings, as três onomatopéias.
A Saída deve apresentar:
Uma string representando a onomatopeia estendida.
Observações:
Não é necessário validar se os valores de entrada são do tipo definido.
Descrição dos Exemplos:
No primeiro exemplo, as três onomatopeias são "boom", "zap" e "bang", concatenando a primeira com três ocorrências da segunda e duas da 
terceira o resultado é "boomzapzapzapbangbang".
Dica:
Para ler mais de um valor por linha use a função split(), como mostrado a seguir, para ler 2 ou mais valores em uma mesma linha:
x, y, z = input().split()
Para quem quiser se aprofundar no funcionamento da função split() consulte a documentação de Python 3.x, em particular procure pelos métodos 
da classe str. """

ono1, ono2, ono3 = input().split()
ono2 = 3 * ono2
ono3 = 2 * ono3

print(ono1 + ono2 + ono3)