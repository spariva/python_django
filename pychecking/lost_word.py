# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    # TU CÓDIGO AQUÍ
    if target_word in text:
        # mtext = text.replace(target_word, replace_word)

        # haz lo mismo pero sin usar replace
        # Encuentra la posición inicial de la palabra objetivo
        start_pos = text.find(target_word)

        # Encuentra la posición final de la palabra objetivo
        end_pos = start_pos + len(target_word)

        # Forma el nuevo texto concatenando la parte antes del objetivo,
        # la palabra de reemplazo, y la parte después de la palabra objetivo
        mtext = text[:start_pos] + replace_word + text[end_pos:]

        return mtext

    return mtext


if __name__ == "__main__":
    run("This is a beautiful night on the Atlantic", "beautiful", "terrible")
