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
        return "'yes' is wrong answer ;(."
        + f"\nCorrect answer was 'no'. Let's try again, {name}!"

    return "'no' is wrong answer ;(."
    + f"\nCorrect answer was 'yes'. Let's try again, {name}!"


def response_comparison(answer, correct_answer, name):
    if is_answer_correct(answer, correct_answer):
        return 'Correct!'

    return f"'{answer}' is wrong answer ;(. "
    + f"Correct answer was '{correct_answer}'.\nLet's try again, {name}!"


def ans(number):
    if number % 2 == 0:
        return 'yes'

    return 'no'


def is_answer_correct(answer, correct_answer):
    return answer.lower() == str(correct_answer)
