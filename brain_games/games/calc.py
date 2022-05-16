from random import randint, choice


a = 0
b = 0
list_of_operations = ['+', '-', '*']


def get_var_calc():
    operation = choice(list_of_operations)
    a = randint(1, 100)
    b = randint(1, 10)
    task = f'{a} {operation} {b}'

    if operation == '+':
        correct_answer = a + b

    elif operation == '-':
        correct_answer = a - b
    else:
        correct_answer = a * b

    return (task, correct_answer)
