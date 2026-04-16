import prompt

from brain_games.engine.correct_response import response_parity
from brain_games.engine.push import correct, greet, loss, victory, welcome_user
from brain_games.engine.random_values import random_number
from brain_games.engine.task import task_check_pariti


def check_parity():
    greet()

    name = welcome_user()

    task_check_pariti()

    start = 1
    finish = 3

    while start <= finish:
        number = random_number()
        print(f'Question: {number}')
        response = prompt.string('Your answer: ')
        if response_parity(number) == response:
            correct()
            start += 1
        else:
            loss(response, response_parity(number), name)
            break

    if start > finish:
        victory(name)