from random import randint
from math import gcd


def get_var_gcd():
    a = randint(1, 100)
    b = randint(1, 50)
    task = f'{a} {b}'
    correct_answer = gcd(a, b)
    return (task, correct_answer)
