import random

def guess(x):
    rando_number = random.randint(1,x)
    guess = 0
    while(guess!= rando_number):
        
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if(guess>rando_number):
            print("Sorry, your guess is too high.")
        elif(guess<rando_number)  :
            print("Sorry, your guess is too low.")
    print(f"Yay, you have guessed the number {rando_number} correctly")
if __name__ == "__main__":
    guess(10)