

import random

def welcome_user():
    print("Welcome to the Brain Games!")
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    name = input("May I have your name? ")
    
    print(f'Hello, {name}!')



    for i in range(3):
        random_number = random.randint(1, 100)

        question_answer = f'Question: {random_number}'
        
        print(f'{question_answer}')

        your_num = input(f'Your answer: ').strip().lower()

        correct_answer = 'no' or 'yes'
    
        if your_num == 'yes' and random_number % 2 == 0 or your_num == 'no' and random_number % 2 != 0:
            print('Correct!')
            
            
        
        else:  
            your_num != question_answer .strip().lower()
            
            print(f"{your_num} is wrong answer ;(. Correct answer was {correct_answer}.")
            
            print (f"Let's try again, {name}!")
    
    print(f'Congratulations, {name}!')

welcome_user()




