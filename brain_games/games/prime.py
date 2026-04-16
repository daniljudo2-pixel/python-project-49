import prompt

from brain_games.engine import correct_response, push, random_values, task


def prime():
    push.greet()

    name = push.welcome_user()

    task.task_prime()
    
    start = 1
    finish = 3

    while start <= finish:
        prime_question = random_values.random_number()
        print(f'Question: {prime_question}')
        response = prompt.string('Your answer: ')
        if correct_response.response_prime(prime_question) == response:
            push.correct()
            start += 1
        else:
            push.loss(response, correct_response.response_prime(prime_question), name)
            break

    if start > finish:
        push.victory(name)