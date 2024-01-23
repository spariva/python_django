# ****************
# CONTANDO VOCALES
# ****************


def run(text: str) -> int:
    num_vowels = 0
    for t in text:
        if t in 'AEIOUÁÉÍÓÚaeiouáéíóú':
            num_vowels = num_vowels + 1

    return num_vowels


if __name__ == '__main__':
    run('El camión chocó contra el árbol')