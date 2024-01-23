# ****************
# TODO SON CARITAS
# ****************


def run(emoji_text: str) -> str:
    match emoji_text:
        case 'happy':
            emoji = '😀'
        case 'SAD':
            emoji = '😔'
        case 'Angry':
            emoji = '😡'
        case 'surpriseD':
            emoji = '😮'
        case 'peNsive':
            emoji = '🤔'
        case _:
            emoji = '😶'
        

    return emoji


if __name__ == '__main__':
    run('happy')