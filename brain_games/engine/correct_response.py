import operator
from brain_games.engine import push

def response_gcd(num1, num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


OPERATIONS = {
'+': operator.add,
'-': operator.sub,
'*': operator.mul,
}

def response_calc(response):
    
    num1_str, calc, num2_str = str(response).split()
    correct_response = OPERATIONS[calc](int(num1_str), int(num2_str))
    return str(correct_response)

def response_parity(response):
    
    if response % 2 == 0:
        correct_response = 'yes'
    elif response % 2 != 0:
        correct_response = 'no'
    
    return correct_response

def response_prime(response):
    
    prime_numbers = [2,	3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
47,	53,	59,	61,	67,	71, 73,	79,	83,	89,	97,	101]
    
    if response in prime_numbers:
        correct_response = 'yes'
    else:
        correct_response = 'no'
    
    return correct_response