# a simple game for guessing the number 

import random

num = random.randint(1,100)
guess = 0

while (guess != num):
    guess = int(input("Enter guess "))

    if(guess < num):
        print("Guess higher ")
    
    elif(guess > num):
        print("Guess lower ")

    else:
        print("You won!")
