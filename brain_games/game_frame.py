import prompt
COUNT_OF_ROUNDS = 3


def run_game(game_name):
    name = welcome_user()
    question = game_name.QUESTION
    print(question)
    i = 0
    while i <= COUNT_OF_ROUNDS:
        variables = game_name.get_var()
        task = variables[0]
        correct_answer = variables[1]
        print(f'Question: {task}')
        answer = prompt.string('Answer: ')
        print(response_comparison(answer, correct_answer, name))
        if not answer.lower() == str(correct_answer):
            break
        i += 1
        if i == COUNT_OF_ROUNDS:
            print(f'Congratulations, {name}!')
            break


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def response_comparison(answer, correct_answer, name):
    if answer.lower() == str(correct_answer):
        return 'Correct!'

    a = f"'{answer}' is wrong answer ;(. "
    b = f"Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
    return a + b
