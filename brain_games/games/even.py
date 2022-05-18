from random import randint
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_var():
    task = randint(1, 100)

    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (task, correct_answer)
