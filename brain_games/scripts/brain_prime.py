import random

def main():
    print("uv run brain-prime")

def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def game_prime():
    
    name = welcome_user()
    for _ in range(3):
        number = random.randint(1, 100)
        answ_question = f'Question: {number}'
        print(f'{answ_question}')
        your_answer = input('Your answer: ').lower().strip()
        correct_answer = 'yes' if is_prime(number) else 'no'
        if your_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{your_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

game_prime()

if __name__ == "__main__":
    main()




    
