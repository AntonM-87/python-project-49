import math
import random

def main():
    print("uv run brain-gcd")

def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    return name

def math_game():
    name = welcome_user()
    
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        result = math.gcd(num1, num2)
        answ_question = f'Question: {num1} {num2}'
        print(f'{answ_question}')
        your_answer = input('Your answer: ').lower().strip()
        if int(result) == int(your_answer):
            print("Correct!")
        else:
            print(f"{your_answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
        
    
math_game()
    
if __name__ == "__main__":
    main()













