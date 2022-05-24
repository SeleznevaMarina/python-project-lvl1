from random import randint, choice
QUESTION = 'What is the result of the expression?'


operators = ['+', '-', '*']


def get_task_answer():
    operation = choice(operators)
    a = randint(1, 100)
    b = randint(1, 10)
    task = f'{a} {operation} {b}'

    if operation == '+':
        correct_answer = str(a + b)
    elif operation == '-':
        correct_answer = str(a - b)
    elif operation == '*':
        correct_answer = str(a * b)

    return (task, correct_answer)
