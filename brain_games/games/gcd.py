from random import randint
from math import gcd
QUESTION = 'Find the greatest common divisor of given numbers.'


def get_task_answer():
    a = randint(1, 100)
    b = randint(1, 50)
    task = f'{a} {b}'
    correct_answer = str(gcd(a, b))
    return (task, correct_answer)
