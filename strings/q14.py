# 
list = ["Raman","NA","John","NA"]
length = len(list)
for i in range(0,length):
    if(list[i]=="NA"):
        list[i]="NOT Available"
print(list)