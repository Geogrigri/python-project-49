import random

rules = 'What number is missing in the progression?'

def element(start, index, step):
	return start + index * step

def generate_round():

	start = random.randint(1, 20)
	step = random.randint(1, 10)
	progression = []
	many_elements = random.randint(7, 12)
	empty_element = random.randint(0, many_elements - 1)

	for i in range(many_elements):
		new_element = element(start, i, step)
		progression.append(new_element)

	correct_answer = str(progression[empty_element])
	progression[empty_element] = '..'

	return progression, correct_answer
