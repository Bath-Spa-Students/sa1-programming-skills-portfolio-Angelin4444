#Optional Requirements:
#Modify the program to include a maximum of 5 password attempts. 
#If the user enters the wrong password,inform them of the remaining attempts.
#If the maximum number of attempts is reached,inform the user that the authorities have been alerted.

#below password is the correct one
login_password = "1234"

#writing how many times the user can try to enter the password.
max_attempts = 5

#the starting count will be 0 and each time it will increase by one
attempts = 0

# Starting a loop which will only break if the user gives the correct ans or the maximun limit is over
while attempts < max_attempts:
#asking the user to give an input.
    user_password = input("Please enter the  correct password: ").strip()
    
#if the answer is wrong then each time it will increase by 1 the attempts.
    attempts += 1

#if the answer is correct then the loop breaks.
    if user_password == login_password:
#loops stops now and this output is printed.
        print("Correct password")
        break
    else:
#if the answer is wrong the attempts decrease by one 
        remaining_attempts = max_attempts - attempts
#after checking how many more attempts are left it will be printed to show the user how many attempts are left for them.
        print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        
#if the user has only 1 more attempt then this output prints telling them they dont have anymore attempts.
        if attempts == max_attempts:
            print("Maximum number of attempts reached.")