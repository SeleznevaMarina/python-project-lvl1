from random import randint
QUESTION = 'What number is missing in the progression?'


def get_task_answer():
    progress_length = randint(5, 9)
    progress_range = randint(2, 10)
    first_element = randint(1, 10)
    progress = []
    x = randint(0, progress_length - 1)

    for j in range(0, progress_length + 1):
        progress.append(str(first_element + j * progress_range))

    correct_answer = progress[x]
    progress[x] = '..'

    task = " ".join(progress)
    return (task, correct_answer)
