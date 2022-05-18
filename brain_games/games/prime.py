from random import randint
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_var():
    task = randint(1, 100)

    if is_prime(task) and task >= 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (task, correct_answer)


def is_prime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    return d * d > number
