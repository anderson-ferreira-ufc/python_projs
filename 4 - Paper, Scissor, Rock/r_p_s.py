#4 - Rock, Paper, Scissor

import random

def winner(p1, cpu):
    if p1 == 'R' and cpu == 'S' or p1 == 'P' and cpu == 'R' or p1 == 'S' and cpu == "P":
        return True

def game():
    p1 = input("Make your choice:\n(R) for rock;\n(P) for paper;\n(S) for scissor.\n".upper())
    cpu = random.choice(['R', 'P', 'S'])

    if p1 == cpu:
        return 'Draw!'
    
    if winner(p1, cpu):
        return 'You win!!'
    return 'You lose!!'

print(game())