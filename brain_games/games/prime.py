from random import randint
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_answer():
    task = randint(1, 100)

    if is_prime(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (task, correct_answer)


def is_prime(number):

    if number >= 1:
        d = 2
        while d < number and number % d == 0:
            d += 1
            return False
        return True
    else:
        return False
