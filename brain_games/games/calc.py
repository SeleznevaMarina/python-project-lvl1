from random import randint, choice
QUESTION = 'What is the result of the expression?'


a = 0
b = 0
action_list = ['+', '-', '*']


def get_var():
    operation = choice(action_list)
    a = randint(1, 100)
    b = randint(1, 10)
    task = f'{a} {operation} {b}'

    if operation == '+':
        correct_answer = a + b

    elif operation == '-':
        correct_answer = a - b
    elif operation == '*':
        correct_answer = a * b

    return (task, correct_answer)
