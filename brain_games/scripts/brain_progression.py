import random


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(2, 3)
    lenght = random.randint(5, 10)
    play_gen = [start + i * step for i in range(lenght)]
    hide_element = random.randint(0, lenght - 1)
    correct_answer = play_gen[hide_element]
    play_gen[hide_element] = ".."
    progression_str = " ".join(map(str, play_gen))
    return progression_str, correct_answer
    
def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")

    for _ in range(3):
        progression_str, correct_answer = generate_progression()
        answ_question = f'Question: {progression_str}'
        print(f'{answ_question}')
        your_answer = input('Your answer: ').lower().strip()
        if int(correct_answer) == int(your_answer):
            print('Correct!')
        else:
            print(f"{your_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

welcome_user()