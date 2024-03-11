# 2 - Guess The Number (computer)

import random

def guess(n):
    rand_num = random.randint(0, n)
    guess = 0
    tries = 3

    while tries > 0:
        guess = int(input(f"Guess a number between 1 and {n} ({tries} tries): "))
        if guess < rand_num:
            tries-=1
            print(f"Sorry, try again! Too low! ({tries} tries):(")
        elif guess > rand_num:
            tries-=1
            print(f"Sorry, try again! Too high! ({tries} tries)")
        else:
            break
    
    if tries == 0:
        print(f"You lose, the correct number is {rand_num} :(")
    else:
        print(f"Yay! You've guessed the right number, which is {rand_num}!")

guess(10)