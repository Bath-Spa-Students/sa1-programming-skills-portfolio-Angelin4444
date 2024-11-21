#Diffenrent functions have same local variables name - No syntax error 

def print_message():
  message ="Hello"
  print(message)
  
def print_message_2():
  message ="My Name is Angelin"
  print(message)

print_message()
print_message_2()