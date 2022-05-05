from random import randint
import prompt
from brain_games.games.utils import welcome_user, response_comparison, is_answer_correct, is_prime
from brain_games.games.utils import COUNT_OF_ROUNDS


def prime_number():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i <= COUNT_OF_ROUNDS:
        number = randint(1, 100)
        question = f'Question: {number}'
        print(question)
        answer = prompt.string('Your answer: ')

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(response_comparison(answer, correct_answer, name))
        if not is_answer_correct(answer, correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break
