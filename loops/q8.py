# Print each character of a string using a loop.
name ="Raman shArma"
length = len(name)
i =0 
vowelcount = 0 
while( i<length):
    if(name[i] in "aeiouAEIOU"):
        vowelcount = vowelcount+1
    print(name[i])
    i=i+1
print("totanl no of vowel in name are ",vowelcount)
# for i in name :
#     print(i)