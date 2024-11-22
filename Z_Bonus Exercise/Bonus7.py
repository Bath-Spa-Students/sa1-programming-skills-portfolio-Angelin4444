# 7) Loops- Pizza Toppings :
"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you'll add that topping to their pizza.
"""
#asking the user to input their favorite pizza toppings.
while True :
     Pizza = input(" Enter your favorite pizza toppings,if not necessary type quite to stop: ")
     
     if Pizza.strip().lower() == 'quite':
          print("Thankyou for your order.The pizza will be ready soon.")
          break 
     #if the output is 'quite' then print the message and break the loop.
print(f"I'll add the topping you want to your pizza!")



