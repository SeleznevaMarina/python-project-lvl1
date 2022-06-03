from random import randint
RULE = 'What number is missing in the progression?'


def get_task_answer():
    progression_length = randint(5, 9)
    elements_difference = randint(2, 10)
    first_element = randint(1, 10)
    progress = []
    random_index = randint(0, progression_length - 1)

    for j in range(progression_length + 1):
        progress.append(str(first_element + j * elements_difference))

    correct_answer = progress[random_index]
    progress[random_index] = '..'

    task = " ".join(progress)
    return (task, correct_answer)
