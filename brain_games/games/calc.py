from random import randint, choice
RULE = 'What is the result of the expression?'


def get_task_answer():
    operators = ['+', '-', '*']
    operation = choice(operators)
    a = randint(1, 100)
    b = randint(1, 10)
    task = f'{a} {operation} {b}'

    if operation == '+':
        correct_answer = a + b
    elif operation == '-':
        correct_answer = a - b
    elif operation == '*':
        correct_answer = a * b

    return (task, str(correct_answer))
