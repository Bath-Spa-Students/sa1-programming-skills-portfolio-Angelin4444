# 5) Control Structures:
"""
Imagine an alien was just shot down in a game. Create a variable called alien_color 
and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien's color is green. If it is, print a message
that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)
"""

#Creating a variable named alien_color.
alien_color = ("Green") #the first test where the color is same with the answer.

if alien_color.strip().lower() == "green":#strip and lower is wrote so that what ever the input is if its lower or uppercase it wont matter.
# if the answer  is correct then will print this 
    print("You have earned 5 points.")

#Creating a variable named alien_color.
alien_color = ("Red") #the first test where the color is same with the answer.

if alien_color.strip().lower() == "green":#strip and lower is wrote so that what ever the input is if its lower or uppercase it wont matter.
# if the answer  is correct then will print this 
    print("You have no points.")
    

