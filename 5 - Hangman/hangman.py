#5 - Hangman

import random, string
from words import words #Accessing the list variable "words" within words.py
from hangman_visual import tries_visual_dict

#Function which only picks words that doesn't contains '-' or ' ' and
#return them uppercased.
def valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

#Contains the Hangman script.
def hangman():
    word = valid_word(words)
    word_letters = set(word) #List variable containing the letters from the chosen word.
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    tries = 6

    #Loop determined to finish if neither all the word letters are correctly guessed
    #or if the player ran out of tries.
    while len(word_letters) > 0 and tries > 0:
        print('You have', tries, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        #List variable which displays the word letters in its correct position, or
        #displays '-' for the remaining ones
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print(tries_visual_dict[tries])
        print("Current word", ' '.join(word_list))

        user_letters = input('Guess a letter: ').upper()

        #Condition which builds the set of used letter by the player
        if user_letters in alphabet - used_letters: #Checks if the player input is in the remaining alphabet letters set
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                tries = tries - 1
                print("\nThis letter is not in the word!")

        elif user_letters in used_letters: #Informs the player he has entered that letter already
            print("\nYou have used this letter already!")
        else:
            print("Invalid character, please, try again!")
        
    if tries == 0:
        print(tries_visual_dict[tries])
        print("You died, sorry! The word was: ", word)
    else:
        print("You guessed the word", word, "!!")
#Calling out the game
if __name__ == '__main__':
    hangman()