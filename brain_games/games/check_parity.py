import prompt

from brain_games.engine import correct_response, push, random_values, task


def check_parity():
    push.greet()

    name = push.welcome_user()

    task.task_check_pariti()

    start = 1
    finish = 3

    while start <= finish:
        number = random_values.random_number()
        print(f'Question: {number}')
        response = prompt.string('Your answer: ')
        if correct_response.response_parity(number) == response:
                push.correct()
                start += 1
        else:
            push.loss(response, correct_response.response_parity(number), name)
            break

    if start > finish:
        push.victory(name)