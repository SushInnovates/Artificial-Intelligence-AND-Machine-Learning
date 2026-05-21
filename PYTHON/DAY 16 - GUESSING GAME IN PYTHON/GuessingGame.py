import random
jackpot = random.randint(1,100)
guess = int(input("Guess the number : "))
counter = 1
while guess != jackpot:
    if guess > jackpot:
        print("try again , pick a lower number")
    else:
        print("try again , pick a higher number")
   
    guess = int(input("Guess the number : "))
    counter += 1
print("Correct Guess")
print("you took ",counter,"Attempts")
    