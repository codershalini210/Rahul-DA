# for i in range(5):
#     print(i)
# for i in range(5,11):
#     print(i)
# for i in range (1,20,3):
#     print(i)
# for i in range (0,21,2):
#     print(i)
# start = int(input("enter start no "))
# end = int(input("Enter end no "))
# for i in range(start,end):
#     if(i%2==0):
#         print(i)
# a = int(input("Enter any no "))
# for n in range(1,11):
#     print(a*n)
n =list(range(1,11))
print(n)
l = n.__len__()
for i in range(0,l):
    n[i]= (n[i])*2
print(n)