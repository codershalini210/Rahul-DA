# Create a dictionary of 5 students with their marks and print each student's name with marks using a loop.
# Write a program to print only the names of all students from a dictionary.
# Print only the marks of all students using values().
# Count how many students are present in the dictionary.
# Find the total sum of all marks using a loop.
students ={"Raman":45,"MAria":25,"John":36,"Ron":75,"Sam":86}
# for key,value in students.items():
#     print(key, value)
# -------------------------------
# for key in students:
#     print(key)
# ---------------------------------
# for value in students.values():
#     print(value)
# -----------------------
# n = len(students)
# print("no of students in dict are ",n)
# -----------------------------
# sum = 0 
# n= len(students)
# for value in students.values():
#     sum=sum+value
# print("sum of all the marks ",sum)
# avg = sum/n
# print("average marks ",avg)
# -------------------------------
#4 Print the name of the student who scored the highest marks.
max= 0
sname = ""
for key,value in students.items():
    if(value>max):
        max=value
        sname=key
print("highest marks :",max," of ",sname)

# print(students)
# print(students.keys())
# print(students.items())
# print(students.values())