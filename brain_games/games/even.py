from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task_answer():
    task = randint(1, 100)
    correct_answer = 'no'

    if task % 2 == 0:
        correct_answer = 'yes'

    return (task, correct_answer)
