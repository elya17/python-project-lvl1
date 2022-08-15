import random
from brain_games.scripts.brain_games import name
print('Answer "yes" if the number is even, otherwise answer "no"')


def calc():
    count = 0
    signs = {'+', '-', '*'}
    while count < 3:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        sign = random.choice(signs)
        if sign == '+':
            result = num1 + num2
        elif sign == '-':
            result = num1 - num2
        elif sign == '*':
            result = num1 * num2
        print('Question:', num1, sign, num2)
        answer = input('Your answer: ')
        if answer != result:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'")
            print(f"Let's try again, {name}!")
        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')


def main():
    calc()