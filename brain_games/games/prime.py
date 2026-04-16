import prompt

from brain_games.engine.correct_response import response_prime
from brain_games.engine.push import correct, greet, loss, victory, welcome_user
from brain_games.engine.random_values import random_number
from brain_games.engine.task import task_prime


def prime():
    greet()

    name = welcome_user()

    task_prime()
    
    start = 1
    finish = 3

    while start <= finish:
        prime_question = random_number()
        print(f'Question: {prime_question}')
        response = prompt.string('Your answer: ')
        if response_prime(prime_question) == response:
            correct()
            start += 1
        else:
            loss(response, response_prime(prime_question), name)
            break

    if start > finish:
        victory(name)