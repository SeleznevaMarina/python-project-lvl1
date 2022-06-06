import prompt
ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    for _ in range(ROUNDS_COUNT):
        (task, correct_answer) = game.get_task_answer()
        print(f'Question: {task}')
        answer = prompt.string('Answer: ')

        if not answer.lower() == correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was ")
            print(f"'{correct_answer}'.\nLet's try again, {name}!")
            break
        print('Correct!')

    else:
        print(f'Congratulations, {name}!')
