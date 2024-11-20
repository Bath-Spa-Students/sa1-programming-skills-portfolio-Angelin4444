"""
In this exercise, you'll create a program that stores and prints your name, 
hometown, and age to the console using a Python dictionary.
"""
#Steps:
#Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#Print the values on separate lines using a single print() statement.
#Use variables with appropriate data types for each piece of information.

#Storing the personal information with the help of normal varible names(name, homwtown, and age).
Name = "Angelin"
Hometown = "India"
Age = "18"

#Storing the same personal information into dictionary using keys(A, B, and C).
Information = {
    "A": Name,  #Used "A" as the key for the value Name.
    "B": Hometown, #Used "B" as the key for the value Hometown.
    "C":Age #Used "C" as the key for the value Age.
    }

#Printing the values on separate lines using a signle print statement.
print((f"{Information['A']}\n{Information['B']}\n{Information['C']}"))
