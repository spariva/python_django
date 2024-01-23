# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    #recibe un string con dos números separados por coma
    #el primer número es el exponente de x
    #el segundo número es el coeficiente de x
    #separamos el string en dos números
    coeficiente, exponente = symbol.split(',')
    exponente = int(exponente) + 1
    coeficiente = int(int(coeficiente) / exponente)
    integral = f'{coeficiente}x^{exponente}'
    
    return integral


if __name__ == '__main__':
    run('3,2')