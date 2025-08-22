import random
import prompt

def is_even(number):
	return number % 2 == 0

def brain_even(name, rounds=3):
	print('Answer "yes" if the number is even, otherwise answer "no".')

	for _ in range(rounds):
		number = random.randint(1, 100)
		print(f'Question: {number}')
		answer = prompt.string('Your answer: ')

		correct_answer = 'yes' if is_even(number) else 'no'

		if answer != correct_answer:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. \n Let's try again, {name}!")
			return False

		print('Correct!')

	print(f'Congratulations, {name}!')
	return True
