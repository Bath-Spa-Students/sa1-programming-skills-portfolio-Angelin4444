#Advanced Requirements:
"""
Have the user input their name, hometown, and age instead of hardcoding the values. 
Try giving both your first and second name when asked for your name. What happens? 
How can you handle multiple words in Python? 
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
"""
#Asking the user for their 'Full Name'.
user_name = input("Enter your full name: ").strip() 
#'strip()' is used in here so that we could remove the extra spaces around the input.

#Asking the user for their 'Hometown'.
user_hometown = input("Enter your hometown: ").strip() 
#.strip() is used for removing the extra spaces.

#Asking the user for their 'Age'. (Here we will let the user write their age in loop until they give a numerical value).
while True: #for asking the question in loops.
    try: #helps in checking if the input added by the user is correct or wrong.
        user_age = int(input("Enter your age: ")) #Asking the user for their age (from input to an integer 'int').
        break #"the loop is breaked since the answer is correct"
    except ValueError: #helps in finding the error and asks the user to display their input into an integer 
        print("The input you have entered in not valid. Please enter a number for your age.")

print("\nInformations about the User:") #this print a heading (\n helps in leaving a place and writing the heading.)
print(f"Name: {user_name}")
print(f"Hometown: {user_hometown}")
print(f"Age: {user_age}")
#the above prints displays the collected information about the user.