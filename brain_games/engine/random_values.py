import itertools
import random


def random_number():
    return abs(random.randint(1, 100))


def random_choice():
    return random.choice(['+', '-', '*'])
    

def random_calculator():
    num1 = random_number()
    num2 = random_number()
    calc = random_choice()
    question = f'{num1} {calc} {num2}'
    return question


def random_progression():
    # создаем прогрессию
    counter = itertools.count(random_number(), random.randint(2, 5))
    list = []
    for i in range(10):
       list.append(str(next((counter))))

    # заменяем рандомный элемнент для задачи пользователю
    list_question = list.copy()
    index = random.randint(0, 9)
    list_question[index] = '..'

    question = ' '.join(list_question)

    return question