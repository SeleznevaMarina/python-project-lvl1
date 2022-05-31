import prompt
COUNT_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)

    for i in range(COUNT_OF_ROUNDS):
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
