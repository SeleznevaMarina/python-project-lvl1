from random import randint
from math import gcd
import prompt
from brain_games.games.utils import welcome_user, response_comparison, is_answer_correct
from brain_games.games.utils import COUNT_OF_ROUNDS


def common_divisor():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i <= COUNT_OF_ROUNDS:
        a = randint(1, 100)
        b = randint(1, 50)
        question = f'Question: {a} {b}'
        print(question)
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(a, b)

        print(response_comparison(answer, correct_answer, name))
        if not is_answer_correct(answer, correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break
