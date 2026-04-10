import prompt


def victory(name):
    print(f'Congratulations, {name}!')


def loss(resp, answer, name):
    print(f''''{resp}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {name}!''')
    

def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def correct():
    print('Correct!')