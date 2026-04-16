import prompt

from brain_games.engine.correct_response import response_calc
from brain_games.engine.push import correct, greet, loss, victory, welcome_user
from brain_games.engine.random_values import random_calculator
from brain_games.engine.task import task_calc


def check_calculator():
    greet()

    name = welcome_user()

    task_calc()

    start = 1
    finish = 3

    while start <= finish:
        calculation = random_calculator()
        print(f'Question: {calculation}')
        response = prompt.string('Your answer: ')
        if response_calc(calculation) == response:
            correct()
            start += 1
        else:
            loss(response, response_calc(calculation), name)
            break
    
    if start > finish:
        victory(name)