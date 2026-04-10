import prompt

from brain_games.engine import push, random_values, task, correct_response
from brain_games.scripts import brain_games


def gcd():
    push.greet()

    name = push.welcome_user()

    task.task_gcd()

    start = 1
    finish = 3

    while start <= finish:
        number_one = random_values.random_randit()
        number_two = random_values.random_randit()
        print(f'Question: {number_one} {number_two}')
        response = prompt.string('Your answer: ')
        if correct_response.response_gcd(number_one, number_two) == response:
            push.correct()
            start += 1
        else:
            push.loss(response, correct_response.response_gcd(number_one, number_two), name)
            brain_games.main()
            break
        
        if start > finish:
             push.victory(name)
             brain_games.main()

    
