import math

def distancia(x1, y1, x2, y2):

    coord1 = x2 - x1
    coord2 = y2 - y1

    distancia_entre_coords = math.sqrt(math.pow(coord1, 2) + math.pow(coord2,2))

    return distancia_entre_coords 

print(distancia(0,0,10,10))