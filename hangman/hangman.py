import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_valid_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    while(len(word_letters)>0 and lives>0): 
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current Word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet-used_letters:

            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print(lives_visual_dict[lives])
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        
    if lives == 0:
        print("Sorry you died. The word was ",word)
    else:
        print(f"You guessed the word '{word}'")
hangman()