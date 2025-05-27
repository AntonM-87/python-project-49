import random

def main():
    print("uv run brain-cacl")

def welcome_user():
    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    return name
    
def oper_name():  
    operators = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator_ran = random.choice(operators)
    
    result = f'{num1} {operator_ran} {num2} '
    correct_answer = eval(result)
    return correct_answer, result


def game_cacl():
    name = welcome_user()
    
    for _ in range(3):
        correct_answer, result = oper_name()
        question_answer = f'Question: {result}'
        print(f'{question_answer}')
        your_a = input('Your answer: ').lower().strip()
        
        if str(correct_answer) == your_a:
            print('Correct!')
            
        else: 
            correct_answer != your_a
            print(f'{your_a} is wrong answer ;(. Correct answer was "{correct_answer}"')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    
if __name__ == "__main__":
    main()




    



    






    







    




