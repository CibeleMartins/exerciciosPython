def classificaMatch():

    distancia = int(input("Qual a distancia entre vc e sua paquera, Carencio? "))

    if (distancia < 100):
       return print("É o amor da minha vida!")
    elif(100 < distancia < 200):
       return print("Talvez de certo!")
    elif(distancia > 200):
       return print("Não vale a pena investir.")


classificaMatch()