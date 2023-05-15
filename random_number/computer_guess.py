import random

def computer_guess(x):
    high = x
    low = 1
    random_num =0

    while(high!=random_num):
        if(high!=low):
            random_num = random.randint(low,high)
        else:
            random_num = high #or even low as high = low
        
        ver = input(f"Is {random_num} too high(h) or too low(l) or correct(c): ").lower()
        if(ver=='h'):
            high = random_num-1
        elif(ver == 'l'):
            low = random_num +1
        elif(ver == 'c'):
            print(f"Yay, the computer guessed your number, {random_num}, correctly")
            break
        else:
            print("Kindly enter a correct input")
            computer_guess(high)
            break
    

if __name__ == "__main__":
    string = input("Think of a number between 1 to 100(Ok/Exit): ").lower()
    if string == 'ok':
        computer_guess(100)
    elif(string == 'exit'):
        print("Exited")
