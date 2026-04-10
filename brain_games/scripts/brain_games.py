from brain_games.games import check_parity, calculator, gcd, prime, progression
from brain_games.engine.push import greet
import prompt

def main():

    greet()
    
    main_menu = ['brain-even', 'brain-calc', 'brain-gcd', 'brain-progression', 'brain-prime', 'exit']
    print(f'What are we going to play?: {" ".join(main_menu)}')
    response = prompt.string('Your answer: ')
   

    match response:
        case 'brain-even':
            check_parity.check_parity()
        case 'brain-calc':
            calculator.check_calculator()
        case 'brain-gcd':
            gcd.gcd()
        case 'brain-progression':
            progression.progression()
        case 'brain-prime':
            prime.prime()
        case 'exit':
            print('See you at the brain games!')
        
            

        
if __name__ == "__main__":
    main()