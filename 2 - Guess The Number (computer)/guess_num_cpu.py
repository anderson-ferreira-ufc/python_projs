# 2 - Guess The Number (computer)

import random

def guess(n):
    rand_num = random.randint(0, n)
    guess = 0

    while rand_num != guess:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        if guess < rand_num:
            print(f"Sorry, try again! Too low!")
        elif guess > rand_num:
            print(f"Sorry, try again! Too high! ")

    print(f"Yay! You've guessed the right number, which is {rand_num}!")

guess(10)