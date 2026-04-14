import prompt

from brain_games.engine import correct_response, push, random_values, task


def progression():
    push.greet()

    name = push.welcome_user()

    task.task_progression()

    start = 1
    finish = 3

    while start <= finish:
        progression = random_values.random_progression()
        print(f'Question: {progression}')
        response = prompt.string('Your answer: ')
        correct_resp = correct_response.response_progression(progression)
        if correct_resp == response:
            push.correct()
            start += 1
        else:
            push.loss(response, correct_resp, name)
            break
        
        if start > finish:
             push.victory(name)