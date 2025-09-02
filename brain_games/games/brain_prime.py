import math
import random

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
	if number < 2:
		return False

	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	return True


def generate_round():
	number = random.randint(1, 100)
	question = str(number)
	correct_answer = 'yes' if is_prime(number) else 'no'

	return question, correct_answer
