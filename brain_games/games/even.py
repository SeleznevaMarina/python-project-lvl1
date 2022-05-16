from random import randint


def get_var_even():
    random_number = randint(1, 100)
    task = random_number
    correct_answer = ans(random_number)
    return (task, correct_answer)


def ans(number):
    if number % 2 == 0:
        return 'yes'

    return 'no'
