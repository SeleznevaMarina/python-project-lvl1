from random import randint
import prompt
from brain_games.games.utils import welcome_user, response_comparison, is_answer_correct
from brain_games.games.utils import COUNT_OF_ROUNDS


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i <= COUNT_OF_ROUNDS:
        progress_length = randint(5, 11)
        progress_range = randint(2, 10)
        first_element = randint(1, 10)
        progress = []
        progress_str = ''
        x = randint(0, progress_length - 1)

        for j in range(0, progress_length + 1):
            progress.append(first_element + j * progress_range)
            if j == x:
                progress_str += '.. '
            else:
                progress_str += str(progress[j]) + ' '

        question = f'Question: {progress_str}'
        print(question)
        answer = prompt.string('Your answer: ')
        correct_answer = progress[x]

        print(response_comparison(answer, correct_answer, name))
        if not is_answer_correct(answer, correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break
