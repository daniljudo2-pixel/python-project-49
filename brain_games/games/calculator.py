import prompt
from brain_games.engine import push, question_response, random_values, task
from brain_games.scripts import brain_games


def check_calculator():
    push.greet()

    name = push.welcome_user()

    task.task_calc()

    start = 1
    finish = 3

    while start <= finish:
        calculation = random_values.random_calculator()
        print(f'Question: {calculation}')
        response = prompt.string('Your answer: ')
        if question_response.response_calc(calculation) == response:
                push.correct()
                start += 1
        else:
             push.loss(response, question_response.response_calc(calculation), name )
             break
        
        if start > finish:
             push.victory(name)