import numpy as np
colors = ['R', 'G', 'B', 'Y', 'O', 'W']
code = np.random.choice(colors, 4).tolist()
count = 0
max_tries = 10
print('')
print(f"Welcome to Mastermind! You have {max_tries} tries to guess the code...")
while True:
    if count == 10:
        print("Better luck next time...")
        break
    print()
    guess = input("Guess: ")
    correctcolors = 0
    correctposition = 0
    guess = [*guess.upper()]
    print('')
    print(''.join(guess))
    code_copy = code.copy()
    for i in range(4):
        if guess[i] == code[i]:
            correctposition += 1
        if guess[i] in code_copy:
            correctcolors += 1
            code_copy.remove(guess[i])
    print(f'Correct colors: {correctcolors} | Correct positions: {correctposition}')
    if correctposition == 4:
        print('')
        print(f"YOU CRACKED THE CODE IN {count + 1} GUESSES!!!")
        break
    count += 1



    



