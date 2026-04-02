age = int(input("Enter age"))
if(age>=18 and age<120):
    print("Eligible to vote")
else:
    if(age<0 or age>120):
        print("invalid age")
    else:
        print("not eligible to vote")

