import prompt
from brain_games.games.calc import get_var_calc
from brain_games.games.even import get_var_even
from brain_games.games.gcd import get_var_gcd
from brain_games.games.prime import get_var_prime
from brain_games.games.progress import get_var_progress
COUNT_OF_ROUNDS = 3
CALC = 'calculation'
EVEN = 'even'
GCD = 'gcd'
PRIME = 'prime'
PROGRESS = 'progression'


def game(game_name):
    name = welcome_user()
    question = get_question(game_name)
    print(question)
    i = 0
    while i <= COUNT_OF_ROUNDS:
        variables = get_game_variables(game_name)
        task = variables[0]
        correct_answer = variables[1]
        print(f'Question: {task}')
        answer = prompt.string('Answer: ')
        print(response_comparison(answer, correct_answer, name))
        if not is_answer_correct(answer, correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_question(game_name):
    if game_name == CALC:
        question = 'What is the result of the expression?'

    if game_name == EVEN:
        question = 'Answer "yes" if the number is even, otherwise answer "no".'

    if game_name == GCD:
        question = 'Find the greatest common divisor of given numbers.'

    if game_name == PRIME:
        a = 'Answer "yes" if given number is prime. '
        b = 'Otherwise answer "no".'
        question = a + b

    if game_name == PROGRESS:
        question = 'What number is missing in the progression?'

    return question


def get_game_variables(game_name):
    if game_name == CALC:
        return get_var_calc()

    if game_name == EVEN:
        return get_var_even()

    if game_name == GCD:
        return get_var_gcd()

    if game_name == PRIME:
        return get_var_prime()

    if game_name == PROGRESS:
        return get_var_progress()


def response_comparison(answer, correct_answer, name):
    if is_answer_correct(answer, correct_answer):
        return 'Correct!'

    a = f"'{answer}' is wrong answer ;(. "
    b = f"Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
    return a + b


def is_answer_correct(answer, correct_answer):
    return answer.lower() == str(correct_answer)
