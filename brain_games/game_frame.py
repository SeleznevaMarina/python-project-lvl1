import prompt
COUNT_OF_ROUNDS = 3


def run(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    question = game.QUESTION
    print(question)

    for i in range(0, COUNT_OF_ROUNDS):
        variables = game.get_task_answer()
        (task, correct_answer) = variables
        print(f'Question: {task}')
        answer = prompt.string('Answer: ')

        if not answer.lower() == correct_answer:
            a = f"'{answer}' is wrong answer ;(. Correct answer was "
            b = f"'{correct_answer}'.\nLet's try again, {name}!"
            print(a + b)
            break
        else:
            print('Correct!')

    else:
        if i == COUNT_OF_ROUNDS - 1:
            print(f'Congratulations, {name}!')
