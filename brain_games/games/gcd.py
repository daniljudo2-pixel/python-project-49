import prompt

from brain_games.engine import correct_response, push, random_values, task


def gcd():
    push.greet()

    name = push.welcome_user()

    task.task_gcd()

    start = 1
    finish = 3

    while start <= finish:
        number_one = random_values.random_number()
        number_two = random_values.random_number()
        print(f'Question: {number_one} {number_two}')
        response = prompt.string('Your answer: ')
        if correct_response.response_gcd(number_one, number_two) == response:
            push.correct()
            start += 1
        else:
            push.loss(response, correct_response.response_gcd(number_one, number_two), name)
            break
        
    if start > finish:
        push.victory(name)

    
