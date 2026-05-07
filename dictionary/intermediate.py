# Add a new student and update their marks in the dictionary.
# hint students[key] = "value" print dictionary

# Increase all students' marks by 5 using a loop. 
# hint: access all the students key,value then set
#  sutdent[key = valyue+5
# students={"aman":35,"Ronit":25,"Raman":52}
# for k,v in students.items():
#     students[k]= v+5
# print(students)
# Create a new dictionary where marks are converted into grades 
# (A, B, C, Fail).
# hint : generate grade based on marks using nested if inside loop
# students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
# studentsGrade={}
# for k,v in students.items():
#     if(v>59):
#         studentsGrade[k] = "A"
#     elif(v>45):
#         studentsGrade[k] = "B"
#     elif(v>34):
#         studentsGrade[k] = "C"
#     else:
#         studentsGrade[k] = "Fail"
# print(studentsGrade)
# Create a list of student names who scored above average.
# students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
# marks = list(students.values())
# totalmarks = sum(marks)
# avg= totalmarks/ len(marks)
# aboveavg= []
# for k,v in students.items():
#     if(v>avg):
#         aboveavg.append(k)
# print(aboveavg)


# Remove students who scored less than 40 marks.
# students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
# studentscopy = students.copy()
# for k,v in students.items():
#     if(v<40):
#         del studentscopy[k]
# print(studentscopy)
# Reverse the dictionary (marks as keys, names as values).
# hint create a new revered dictionary
# students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
# newdictionary = {}
# for k,v in students.items():
#     newdictionary[v] = k
# print(newdictionary)
# Sort students based on marks (ascending and descending).

# students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
# asc  ={k:v for k,v in sorted(students.items(),key=lambda item:item[1])}
# print(asc)
# marks = list(asc.values())
# print(marks[-2])

# marks =[25,45,96,12,3]
# sortedmarks = sorted(marks)
# print(sortedmarks)
# Find the second highest marks in the dictionary.
# Check if a particular student exists in the dictionary.
# Split students into passed and failed groups.
# students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
# pass1={}
# fail = {}
# for k,v in students.items():
#     if(v>=35):
#         pass1[k] = v
#     else:
#         fail[k] = v
# print(students)
# print(pass1)
# print(fail)
# Calculate percentage contribution of each student’s marks.

students={"aman":35,"Ronit":25,"Raman":52,"Ron":75}
total = sum((list(students.values())))
for k,v in students.items():
    print(f"contribution of marks of {k} is {(v/total)*100}")