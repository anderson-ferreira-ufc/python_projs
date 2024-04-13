# 3 - Guess The Number (computer)

import random

def cpu_guess(n):
    low = 1
    high = n
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, n)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?: ".lower())

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Yay! The computer guessed your number right, which is {guess}")

cpu_guess(30)