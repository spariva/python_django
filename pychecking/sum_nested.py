# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(lista):
    # TU CÓDIGO AQUÍ
    for i in lista:
        if type(i) == list:
            for j in i:
                j += j
        j += i

    return j
