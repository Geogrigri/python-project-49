import random

rules = 'What number is missing in the progression?'


def element(start, index, step):
	return start + index * step


def generate_round():

	start = random.randint(1, 20)
	step = random.randint(1, 10)
	progression = []
	many_elements = random.randint(7, 12)
	hidden_element = random.randint(0, many_elements - 1)

	for i in range(many_elements):
		new_element = element(start, i, step)
		progression.append(str(new_element))

	correct_answer = str(progression[hidden_element])
	progression[hidden_element] = '..'

	question = ' '.join(progression)

	return question, correct_answer
