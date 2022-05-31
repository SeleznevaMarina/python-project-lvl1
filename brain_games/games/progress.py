from random import randint
GAME_RULES = 'What number is missing in the progression?'


def get_task_answer():
    progression_length = randint(5, 9)
    progression_range = randint(2, 10)
    first_element = randint(1, 10)
    progress = []
    encrypted_element = randint(0, progression_length - 1)

    for j in range(progression_length + 1):
        progress.append(str(first_element + j * progression_range))

    correct_answer = progress[encrypted_element]
    progress[encrypted_element] = '..'

    task = " ".join(progress)
    return (task, correct_answer)
