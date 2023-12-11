def calculating(number):
    if number % 2 == 0:
        print('Even!')
    else:
        print('Odd')
    if input("Continue? Type 'no' to stop!\n") == 'no':
        exit()
    else:
        main()


def main():
    try:
        number = int(input('Enter number in range 1 - 1000\n'))
        assert 1 <= number <= 1000
        calculating(number)
    except (TypeError, AssertionError):
        main()


if __name__ == '__main__':
    main()
