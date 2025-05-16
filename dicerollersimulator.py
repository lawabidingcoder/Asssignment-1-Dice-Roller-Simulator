# Assignment 1
# Dice Roller Simulator
import random # loads the built-in random module 

def roll_the_dice():
    random_number = random.randint(1, 6) # generates random number
    print("You rolled:", random_number)  # from given range

# Program Loop
while True:
    roll_the_dice()
    again = input("Do you want to roll again? (yes/no): ")
    if again != "yes":
        print("Goodbye!") # Breaks the program if no or if other charcter written 
        break     