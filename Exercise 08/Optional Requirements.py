#Optional Requirements:
#Allow the user to input the search term instead of using a predefined value.
#Implement the search functionality based on user input.

#Writing the list of names as given.
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Asking the user to enter an input they are looking for 
input_name = input("Enter a name you want to find from the list: ").strip()
#The question is asked to the user to input the name they want to find. 
# Adding '.strip() will remove all the extra spaces created by the user.

#Giving the output to the users as per their search. 
if input_name.lower() in [name.lower() for name in Names]:#this line search if the name searched is there on the list and give the answer.
# this line also let the user write the same name in different ways so it doesnt matter if its capital or lower case.
    print(f"Good Job!The name your looking for is there on the list.")
#if the input given by the user is there on the list then this will print.
else:
    print(f"Sorry.The name you searched is not there on the list")
#if the input given by the user is not there on the list then this will print.
