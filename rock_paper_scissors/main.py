from random import randint


def user_interface(options):
    for index, option in enumerate(options):
        print(f'{index} = {option}')

    user_input = input('What do you choose? ')

    while user_input not in ("1", "2", "0"):
        print("Choose the number 0,1 or 2")
        user_input = input('What do you choose? ')
    user_input = int()
    return user_input


def computer_choice(content):
    computer_chose = randint(0, len(content) - 1)
    return computer_chose


def check_results(choices, player, computer):
    if player == computer:
        return 'It\'s a tie'
    elif (player == 0 and computer == len(choices) - 1) or (
            player > computer and not (player == len(choices) - 1 and computer == 0)):
        return 'Player Won'
    return 'Player Lost'


def play():
    print("Welcome to the game 'Rock paper or scissors'")
    options_list = ['Rock', 'Paper', 'Scissors']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)

    print(f'  player chose: {options_list[player_result]}')
    print(f'computer chose: {options_list[computer_result]}')

    results = check_results(options_list, player_result, computer_result)
    print(f'\n{results}')


def main():
    play_again = ''
    while play_again.lower() != 'no':
        play()
        print(f'Do you want to play again? ')
        play_again = input('Type "no" to end the game!')


main()
