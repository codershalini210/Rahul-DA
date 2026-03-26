age  = int(input("enter age"))
if(age>17):
    if(age<121):
        print("you are eligible to vote")
    else:
        print("Invalid age")    
else:
    if(age<=0):        
        print("Invalid")    
    else:
        print("you are not eligible to vote ")

