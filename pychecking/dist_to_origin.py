# Distancia al origen de un punto dando unas coordenadas, xy o xyz

def dist_to_origin(point):
    match point:
        case (int(x), int(y)):
            dist_to_origin = (x ** 2 + y ** 2) ** (1 / 2)
        case (int(x), int(y), int(z)):
            dist_to_origin = (x ** 2 + y ** 2 + z ** 2) ** (1 / 2)
        case _:
            dist_to_origin = None
            print('Unknown!')

    return dist_to_origin

if __name__ == '__main__':
    print(dist_to_origin((1, 2, 3)))
    print(dist_to_origin((5, 5)))
    print(dist_to_origin((1, 2, 3, 4)))