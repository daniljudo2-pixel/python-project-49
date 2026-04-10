import itertools
import random


def random_randit():
    return abs(random.randint(0, 50))


def random_choice():
    return random.choice(['+', '-', '*'])
    

def random_calculator():
    num1 = random_randit()
    num2 = random_randit()
    calc = random_choice()
    question = f'{num1} {calc} {num2}'
    return question

def random_progression():
    #создаем прогрессию
    counter = itertools.count(random_randit(),random.randint(2, 5))
    list = []
    for i in range(10):
       list.append(str(next((counter))))

    #заменяем рандомный элемнент для задачи пользователю
    #и записываем ответ в correct_responce
    list_question = list.copy()
    index = random.randint(0, 9)
    correct_responce = list_question[index]
    list_question[index] = '..'

    result = ' '.join(list_question)

    return result, correct_responce