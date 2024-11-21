#Write a program that searches for a specific string within a list of strings.
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

#Writing the list of names as given.
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Writing the a name to check if the name is there on the list or not.
name_to_find = ("Mia") #the name we have to find is 'Sam'.

#Finding if the name searched is there on the list or not.
if name_to_find in Names:
    print(f"'{name_to_find} is there in this list")
else:
    print(f"'{name_to_find} is not there in this list")

