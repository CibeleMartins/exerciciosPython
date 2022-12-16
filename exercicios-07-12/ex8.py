qtd_alunos, pares_amizade = map(int, input("Digite o número de amigos e os pares de amizades: ").split())

alunos = input("Digite o nome do aluno: ").split()

amizades = {}


for aluno in alunos:

    print(aluno)

    amizades[aluno] = dict({aluno: None})

for amizade in range(pares_amizade):

    amigo1, amigo2 = input("Digite o nome de dois amigos: ").split()

    amizades[amigo1].update(amizades[amigo2])

    for aluno in amizades[amigo1]:

        amizades[aluno].update(amizades[aluno])
    
    for aluno in amizades[amigo1]:

        amizades[aluno] = amizades[amigo1]

    for i in sorted(alunos):

        print(aluno + f'possui {len(amizades[aluno])} amigos')
