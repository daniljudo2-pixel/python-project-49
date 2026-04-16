import prompt

from brain_games.engine.correct_response import response_progression
from brain_games.engine.push import correct, greet, loss, victory, welcome_user
from brain_games.engine.random_values import random_progression
from brain_games.engine.task import task_progression


def progression():
    greet()

    name = welcome_user()

    task_progression()

    start = 1
    finish = 3

    while start <= finish:
        progression = random_progression()
        print(f'Question: {progression}')
        response = prompt.string('Your answer: ')
        correct_resp = response_progression(progression)
        if correct_resp == response:
            correct()
            start += 1
        else:
            loss(response, correct_resp, name)
            break
    
    if start > finish:
        victory(name)