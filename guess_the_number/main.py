import random


def main():
    number = random.randint(0, 50)
    play(number)


def play(number):
    try:
        guess_number = int(input("Guess the number in range 1-50 \n"))
        while guess_number != number:
            assert 1 <= guess_number <= 50
            if guess_number < number:
                print('Larger number!')
            else:
                print('Less number!')
            guess_number = int(input("Guess the number in range 1-50 \n"))
        print('You won, Congrats!')
        play_again()
    except (TypeError, AssertionError):
        play(number)


def play_again():
    play_again_input = input('Do you want to play again?\nType "no" to end the game! \n')
    if play_again_input.lower() == 'no':
        print('Bye! See you next time!')
        exit()
    else:
        main()


if __name__ == '__main__':
    main()
