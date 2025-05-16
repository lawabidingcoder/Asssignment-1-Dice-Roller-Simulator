## Assignment 1
## Stimulating rolling a dice
import random
input("Press enter to roll the dice")
dice = random.randint(1, 6)
## The random module is used to generate random numbers
print("You rolled a " + str(dice))
## Concatenate the string with the number
## The str() function is used to convert the number to a string
answer = input("Do you want to roll again? Yes or No: ")
## Ask the user if they want to roll again
while answer.lower() == "yes":
  dice = random.randint(1, 6)
  print("You rolled a " + str(dice))
  answer = input("Do you want to roll again? Yes or No: ")
## Loop until the user enters "no"
print("Thank you for playing!")
