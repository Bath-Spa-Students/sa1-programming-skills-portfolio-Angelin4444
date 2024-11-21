#Write a program that tests if a value is even or odd. Follow the instructions outlined below:
"""
Instructions:
The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function.
"""
#The below functions let the user know if the number is even or odd.
def check_number(number):
# If a number is divisible by 2, then its even
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
# If its not divisible by 2, then it's odd
        return f"{number} is a odd number."

#Main function helps to display the main part of the program. her the main part is to ask the user for an input number.
def main():
# The bellow method is asking the user to enter a number which they want to if its even or odd.
    try:
        input_number = int(input("Please enter a number you want to know if its even or odd: "))#asking the user to enter the number.
# checking if the input is even or not.
        result_output = check_number(input_number)
# giving the output to the user if it even or odd 
        print(result_output)
    except ValueError:
# except valueerror method is used here to correct the user if they made a mistake to type a word instead of a number
        print("The input is Invalid. Please enter a numerical value to get your answer.")

#this function helps in the running the main program directly before any other .
if __name__ == "__main__":
    main()
