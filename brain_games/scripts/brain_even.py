import random
from brain_games.scripts.brain_games import name
print('Answer "yes" if the number is even, otherwise answer "no"')


def game():
	num = random.randint(1, 1000)
	if num % 2 == 0:
		parity = 'yes'
	else:
		parity = 'no'
	print('Question:', num)
	flag = False
	while not flag:
		answer = input('Your answer: ')
		if answer != parity:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{parity}'")
			print(f"Let's try again, {name!}")
		else:
			print('Correct!')
			flag = True


count = 0
while count < 3:
	result = game()
print(f'Congratulations, {name}!')

