import prompt
from brain_games.engine import correct_response, push, task, random_values


def check_parity():
    push.greet()

    name = push.welcome_user()

    task.task_check_pariti()

    for n in range(3):
        number = random_values.random_number()
        print(f'Question: {number}')
        response = prompt.string('Your answer: ')
        if correct_response.response_parity(number) == response:
                push.correct()
        else:
            push.loss(response, correct_response.response_parity(number), name)
            break

        
        if n == 2:
            push.victory(name)