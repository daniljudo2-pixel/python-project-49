import prompt


def welcome_user():
    # Библиотека prompt предоставляет функции, которые запрашивают ввод строк, чисел, паролей. 
    # При этом вводимый пароль не будет отображаться в консоли.
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
    