import prompt

from brain_games.engine.correct_response import response_gcd
from brain_games.engine.push import correct, greet, loss, victory, welcome_user
from brain_games.engine.random_values import random_number
from brain_games.engine.task import task_gcd


def gcd():
    greet()

    name = welcome_user()

    task_gcd()

    start = 1
    finish = 3

    while start <= finish:
        number_one = random_number()
        number_two = random_number()
        print(f'Question: {number_one} {number_two}')
        response = prompt.string('Your answer: ')
        if response_gcd(number_one, number_two) == response:
            correct()
            start += 1
        else:
            loss(response, response_gcd(number_one, number_two), name)
            break
        
    if start > finish:
        victory(name)

    
