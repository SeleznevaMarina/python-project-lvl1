from random import randint
GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_answer():
    task = randint(1, 100)
    correct_answer = 'no'

    if is_prime(task):
        correct_answer = 'yes'

    return (task, correct_answer)


def is_prime(number):

    if number >= 1:
        for d in range(2, number):
            if number % d == 0:
                return False
        return True
    return False
