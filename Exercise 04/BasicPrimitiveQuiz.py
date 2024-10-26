### Steps:
#1. write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

#Writing the question to the variable 
Answer = input("What is the capital of France?:")
if Answer == "Paris": #(writing the answer for the question)
    print("The answer is correct") #(if the answer is correct then show'the answer is correct')
else:
     print("The answer is wrong") #(if the answer is wrong then show ' the answer is wrong)