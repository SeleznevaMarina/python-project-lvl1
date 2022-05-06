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


def response_comparison(answer, correct_answer, name):
    if is_answer_correct(answer, correct_answer):
        return 'Correct!'

    return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"


def ans(number):
    if number % 2 == 0:
        return 'yes'

    return 'no'


def is_answer_correct(answer, correct_answer):
    return answer.lower() == str(correct_answer)


def is_prime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    return d * d > number
