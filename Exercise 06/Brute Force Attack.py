#Write a program that simulates a password entry system. 
# The correct password is defined as 12345.
#  The program should keep asking the user to enter the password until they provide the correct one.

#Basic Requirements:
'''
Define the correct password.
Use a while loop to repeatedly ask the user for the password until the correct one is entered.
Output an appropriate message when the correct password is entered.
'''

#In this activity we will be asking the user to give the password and checking if its correct or wrong.
def password_varification():
    login_password = ("12345")
#(The above varible stores the correct password) 

    while True: #(This code is used so that the user can try the password again until its correct. "loops function is used in this" )
      user_password = input("Please enter the correct password:") # asking the user to enter the password.

      if user_password == login_password:
#(if the answer is correct then print)
         print("Login Successful")
         break #(if the answer is correct then break the loop by adding the function "break")
      else:
         print("Login Failed:Check Your Password")
#(if the password is wrong then print the above words , indicating that the password is wrong.)

password_varification()



