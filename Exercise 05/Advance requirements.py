#Advanced Requirement:
"""
Leap Year Adjustment: Modify the program to account for leap years. 
For February, ask the user if the year is a leap year and adjust the number of days accordingly.
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
 
# Checking if the entered entered input by the user is within the number 1 to 12.
    if 1 <= serialno_of_month <= 12:
        
# For the month february we have to check if the user wants it to be in leap or non leap year.       
        if serialno_of_month == 2:
# Ask the user if they are choosing the leap year or not.
            leap_ornot = input("Do you want to know about the leap year? (yes/no): ").strip().lower()
# If user choose leap year, then February will have 29 days; otherwise, it will have 28 days.
            days = 29 if leap_ornot == "yes" else 28
        else:
# For all the other months, look up the serial no. 
            days = Day_of_the_month[serialno_of_month]
        
# show the user the out put they asked for from the serial month
        print(f"The number of days in month is {days}.")
    else: #if the serial no. is not valid, then print: 
        print("Sorry!The input you gave is not a month . Please enter a number between 1 and 12 to get your answer.")

except ValueError:
# the except valueerror is done to correct the input given by the user if its not a numerical value.
    print("It's an Invalid input. Please enter a numerical value between 1 and 12 to get your answer.")
