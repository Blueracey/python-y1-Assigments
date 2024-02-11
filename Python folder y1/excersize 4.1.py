import random

Seccret=random.randint(0.10)



Guess = int(input("Guess a number between 0  and 10"))



while Guess !='Q':
    
    if (int(Guess) == Seccret):
        print("correct")
    elif(int(Guess) > Seccret):
        print("your guess was larger then the secret")
    elif(int(Guess) < Seccret):
     print("your guess was smaller then the secret")
Guess = int(input("Guess a number between 0  and 10")) 