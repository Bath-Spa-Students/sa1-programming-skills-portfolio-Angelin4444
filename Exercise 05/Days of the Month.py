#Write a program that tells a user how many days there are in a specific month.
#Use a dictionary to map the month numbers (1-12) to the number of days in each month.
"""
Instructions:
Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
Input Handling: Ask the user to input the month number.
Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
"""

#Writing the number of days in each month using dictionary.
Day_of_the_month = {
    1 : 31,   # January
    2 : 28,   # February (assuming a non-leap year)
    3 : 31,   # March
    4 : 30,   # April
    5 : 31,   # May
    6 : 30,   # June
    7 : 31,   # July
    8 : 31,   # August
    9 : 30,   # September
    10 : 31,  # October
    11 : 30,  # November
    12 : 31   # December 
} #we are writing the 12 months and their last dates(here february is assumed as a non-leap year).
# We have given each month a serial no. as a key instead of writing the months. 

# asking the user to input a months serial no. so the output comes as 'how many days are there in a number.'
try :
    serialno_of_month = int(input("Enter the serial number of the month(1-12): ").strip()) #Asking the question without any extra spaces.

    if serialno_of_month in Day_of_the_month : #if the serial no.is valid, then print:
        print(f"The number of days in that month is {Day_of_the_month[serialno_of_month]}.")
    else: #if the serial no. is not valid, then print: 
        print("Sorry!The input you gave is not a month . Please enter a number between 1 and 12 to get your answer.")
#the above if else statement is done only if the input given by the user is a no. and is 'in' or 'not in' the no. between 1-12. 

#the except valueerror is done to correct the input given by the user if its not a numerical value.
except ValueError:
    print("It's an Invalid input. Please enter a numerical value between 1 and 12 to get your answer.")




