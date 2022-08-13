import random
from brain_games.scripts.brain_games import name
print('Answer "yes" if the number is even, otherwise answer "no"')


def game():
    count = 0
    while count < 3:
        num = random.randint(1, 1000)
        if num % 2 == 0:
            parity = 'yes'
        else:
            parity = 'no'
        print('Question:', num)
        answer = input('Your answer: ')
        if answer != parity:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{parity}'")
            print(f"Let's try again, {name}!")
        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')


def main():
    game()


if __name__ == '__main__':
    main()
