import prompt

from brain_games.engine import push, random_values, task, correct_response


def progression():
    push.greet()

    name = push.welcome_user()

    task.task_progression()

    start = 1
    finish = 3

    while start <= finish:
        progression_question = random_values.random_progression()
        print(f'Question: {progression_question[0]}')
        response = prompt.string('Your answer: ')
        if progression_question[1] == response:
            push.correct()
            start += 1
        else:
            push.loss(response, progression, name)
            break
        
        if start > finish:
             push.victory(name)