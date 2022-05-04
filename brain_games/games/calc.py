from random import randint, choice
import prompt
from brain_games.games.utils import welcome_user, response_comparison, is_answer_correct
from brain_games.games.utils import COUNT_OF_ROUNDS


a = 0
b = 0
list_of_operations = ['+', '-', '*']


def calculation():
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i <= COUNT_OF_ROUNDS:
        operation = choice(list_of_operations)
        a = randint(1, 100)
        b = randint(1, 10)
        question = f'Question: {a} {operation} {b}'
        print(question)
        answer = prompt.string('Your answer: ')

        if operation == '+':
            correct_answer = a + b

        elif operation == '-':
            correct_answer = a - b
        else:
            correct_answer = a * b

        print(response_comparison(answer, correct_answer, name))
        if not is_answer_correct(answer, correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break
