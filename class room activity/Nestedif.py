Salary = int (input("enter your salary:"))
if Salary >= 30000:
    years_on_job = float(input("Enter the years of the job:"))
    if years_on_job >= 2:
         print("You qualify for the job")
    else: 
         print("experience is less than 2")

else:
         print ("you should earn atlest 30k to qualify")