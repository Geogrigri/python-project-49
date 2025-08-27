import random

rules = 'What is the result of the expression?'


def generate_round():
	a = random.randint(1, 100)
	b = random.randint(1, 100)
	operator = random.choice(['+', '-', '*'])

	exercise = f'{a} {operator} {b}'

	match operator:
		case '+':
			correct_answer = str(a + b)
		case '-':
			correct_answer = str(a - b)
		case '*':
			correct_answer = str(a * b)

	return exercise, correct_answer
