### Advanced Requirements:
# 1) Ignore Capitalization: Modify your program to accept answers regardless of the capitalization
#(e.g., "paris", "Paris", and "PaRis" should all be considered correct).

# 2) Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries.
#  Provide feedback for each question.

#Writing the question to the variable and modifying it to answer it no matter if it is capital or lower case 
Answer = input("What is the capital of France?:")
if Answer.strip().lower() == "paris": #(writing the answer for the question without mattering if its in lower or upper case)
    print("The answer you have given is correct") #(if the input given by the user is right then this is printed')
else:
     print("The answer you have given is wrong") #(if the answer is wrong then show ' the answer is wrong)

#Writing the 1st question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Austria?:") #(writing the 1st question)
if Answer.strip().lower() == "vienna": #(writing the answer for the question without mattering if its in lower or upper case)
    print("The answer you have given is correct") #(if the answer is correct then show this)
else:
     print("The answer you have given is wrong") #(if the answer is wrong then show this)

#Writing the 2nd question to the variable ( after modification on upper and lower case)
Answer = input("What is the capital of Belgium?:") #(writing the 2nd question)
if Answer.strip().lower() == "brussels": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 3rd question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Croatia?:") #(writing the 2nd question)
if Answer.strip().lower() == "zagreb": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 4th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Cyprus?:") #(writing the 2nd question)
if Answer.strip().lower() == "nicosia": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 5th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Denmark?:") #(writing the 2nd question)
if Answer.strip().lower() == "copenhagen": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 6th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Finland?:") #(writing the 2nd question)
if Answer.strip().lower() == "helsinki": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 7th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Greece?:") #(writing the 2nd question)
if Answer.strip().lower() == "athens": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 8th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Latvia?:") #(writing the 2nd question)
if Answer.strip().lower() == "rigga": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 9th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Ireland?:") #(writing the 2nd question)
if Answer.strip().lower() == "dublin": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)

#Writing the 10th question to the variable ( with modification on upper and lower case)
Answer = input("What is the capital of Italy?:") #(writing the 2nd question)
if Answer.strip().lower() == "rome": #(writing the answer for the question)
     print("The answer you have given is correct") #(if the answer is right then print this)
else:
    print("The answer you have given is wrong") #(if the answer is wrong then print this)