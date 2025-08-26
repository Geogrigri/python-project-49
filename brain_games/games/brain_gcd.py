import random
import math

rules = 'Find the greatest common divisor of given numbers.'

def generate_round():
	a = random.randint(1, 100)
	b = random.randint(1, 100)
	question = f"{a} {b}"
	correct_answer = str(math.gcd(a, b))
	return question, correct_answer
