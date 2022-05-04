from random import randint
import prompt
from brain_games.games.utils import welcome_user, get_message, ans, is_answer_correct
from brain_games.games.utils import COUNT_OF_ROUNDS


def even_odd():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= COUNT_OF_ROUNDS:
        random_number = randint(1, 100)
        question = f'Question: {random_number}'
        print(question)
        answer = prompt.string('Answer: ')
        correct_answer = ans(random_number)
        print(get_message(answer, correct_answer, name))
        if not is_answer_correct(answer, correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break
