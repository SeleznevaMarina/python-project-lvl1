from random import randint


def get_var_prime():
    task = randint(1, 100)

    if is_prime(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (task, correct_answer)


def is_prime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    return d * d > number
