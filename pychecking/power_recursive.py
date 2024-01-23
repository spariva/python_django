# ******************
# POTENCIA RECURSIVA
# ******************


def power(x:int , n:int) -> int:
    # TU CÓDIGO AQUÍ
    if n == 0:
        return 1
    if n == 1:
        return x
    
    return x * power(x, (n-1))

