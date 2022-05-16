from random import randint


def get_var_progress():
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

    task = progress_str
    correct_answer = progress[x]
    return (task, correct_answer)
