import random

roll = random.randint(1,6)

guess = int(input('Guess the dice roll:\n'))
if guess == roll:
    print("Correct! The computer rolled a " + str(roll))
else:
    print("Sorry, the computer rolled a " + str(roll) + "." + " You lose sukka!!")