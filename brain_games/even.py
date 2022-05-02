from random import randint
import prompt
COUNT_OF_ROUNDS = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_message(answer, correct_answer, name):
    if is_answer_correct(answer, correct_answer):
        return 'Correct!'

    if correct_answer == 'no':
        return f"'yes' is wrong answer ;(.\nCorrect answer was 'no'. Let's try again, {name}!"

    return f"'no' is wrong answer ;(.\nCorrect answer was 'yes'. Let's try again, {name}!"


def ans(number):
    if number % 2 == 0:
        return 'yes'

    return 'no'


def is_answer_correct(answer, correct_answer):
    return answer.lower() == correct_answer


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
        if i == 3:
            print(f'Congratulations, {name}!')
            break
