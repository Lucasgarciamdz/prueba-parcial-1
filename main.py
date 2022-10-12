from ahorcado import Ahorcado


def main():
    game = Ahorcado()
    while not game.is_over:
        print('Pistas:')
        print(game.board)
        print('Letras usadas: ')
        print(game.used_letters)
        print('Vidas: ')
        print(game.lifes_left)
        letter = input('diga una letra de la A a la Z: ')
        game.play(letter)

    if game.win:
        print('Usted gano!')
    else:
        print('Lo lamento, la palabra era: {}'.format(game.secret_word))


if __name__ == '__main__':
    main()
