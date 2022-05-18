from random import randint
QUESTION = 'What number is missing in the progression?'


def get_var():
    progress_length = randint(5, 11)
    progress_range = randint(2, 10)
    first_element = randint(1, 10)
    progress = []
    progress_str = ''
    x = randint(0, progress_length - 1)

    for j in range(0, progress_length + 1):
        progress.append(first_element + j * progress_range)

    for n in range(0, progress_length + 1):
        if n == x:
            progress_str += '.. '
        else:
            progress_str += str(progress[n]) + ' '

    task = progress_str
    correct_answer = progress[x]
    return (task, correct_answer)
