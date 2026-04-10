import prompt
from brain_games.engine import push, task, correct_response
from brain_games.engine.random_values import random_randit
from brain_games.scripts import brain_games


def check_parity():
    push.greet()

    name = push.welcome_user()

    task.task_check_pariti()

    start = 1
    finish = 3

    while start <= finish:
        number = random_randit()
        print(f'Question: {number}')
        response = prompt.string('Your answer: ')
        if correct_response.response_parity(number) == response:
                push.correct()
                start += 1
        else:
            push.loss(response, correct_response.response_parity(number), name)
            brain_games.main()
            break

        
        if start > finish:
            push.victory(name)
            brain_games.main()